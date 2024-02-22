from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from config import DEPLOYER_ABI, DEPLOYER_BYTECODE
from .account import Account


class Deployer(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

    @retry
    @check_gas
    async def deploy_token(self):
        logger.info(f"[{self.account_id}][{self.address}] Deploy contract")

        tx_data = await self.get_tx_data()

        contract = self.w3.eth.contract(
            abi=DEPLOYER_ABI,
            bytecode=DEPLOYER_BYTECODE
        )

        transaction = await contract.constructor().build_transaction(
            tx_data
        )

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
