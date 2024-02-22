from loguru import logger
from config import L2PASS_ABI
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class L2Pass(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

    @staticmethod
    async def get_mint_price(contract):
        price = await contract.functions.mintPrice().call()

        return price

    @retry
    @check_gas
    async def mint(self, contract: str):
        logger.info(f"[{self.account_id}][{self.address}] Mint L2Pass NFT")

        contract = self.get_contract(contract, L2PASS_ABI)

        mint_price = await self.get_mint_price(contract)

        tx_data = await self.get_tx_data(mint_price)

        signed_txn = await self.sign(tx_data)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
