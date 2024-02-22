from eth_utils import to_bytes
from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class Transfer(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

    @retry
    @check_gas
    async def transfer(
            self,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ) -> None:
        amount_wei, amount, balance = await self.get_amount(
            "ETH",
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )

        logger.info(f"[{self.account_id}][{self.address}] Make transfer to {self.recipient} | {amount} ETH")

        tx_data = await self.get_tx_data(amount_wei)
        tx_data.update({
            "to": self.w3.to_checksum_address(self.recipient)
        })

        signed_txn = await self.sign(tx_data)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
