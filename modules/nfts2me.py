import random
from typing import List

from loguru import logger
from config import NFTS2ME_ABI
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class Minter(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

    @retry
    @check_gas
    async def mint_nft(self, contracts: List):
        logger.info(f"[{self.account_id}][{self.address}] Mint NFT on NFTS2ME")

        contract = self.get_contract(random.choice(contracts), NFTS2ME_ABI)

        tx_data = await self.get_tx_data()

        transaction = await contract.functions.mint(1).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
