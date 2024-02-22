from typing import Dict

from loguru import logger
from config import AAVE_CONTRACT, AAVE_WETH_CONTRACT, AAVE_ABI
from utils.gas_checker import check_gas
from utils.helpers import retry
from utils.sleeping import sleep
from .account import Account


class Aave(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

        self.contract = self.get_contract(AAVE_CONTRACT, AAVE_ABI)

    async def get_deposit_amount(self):
        aave_weth_contract = self.get_contract(AAVE_WETH_CONTRACT)

        amount = await aave_weth_contract.functions.balanceOf(self.address).call()

        return amount

    @retry
    @check_gas
    async def deposit(
            self,
            min_amount: float,
            max_amount: float,
            decimal: int,
            sleep_from: int,
            sleep_to: int,
            make_withdraw: bool,
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

        logger.info(f"[{self.account_id}][{self.address}] Make deposit on Aave | {amount} ETH")

        tx_data = await self.get_tx_data(amount_wei)

        transaction = await self.contract.functions.depositETH(
            self.w3.to_checksum_address("0x11fCfe756c05AD438e312a7fd934381537D3cFfe"),
            self.address,
            0
        ).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

        if make_withdraw:
            await sleep(sleep_from, sleep_to)

            await self.withdraw()

    @retry
    @check_gas
    async def withdraw(self) -> None:
        amount = await self.get_deposit_amount()

        if amount > 0:
            logger.info(
                f"[{self.account_id}][{self.address}] Make withdraw from Aave | " +
                f"{self.w3.from_wei(amount, 'ether')} ETH"
            )

            await self.approve(amount, "0xf301805be1df81102c957f6d4ce29d2b8c056b2a", AAVE_CONTRACT)

            tx_data = await self.get_tx_data()

            transaction = await self.contract.functions.withdrawETH(
                self.w3.to_checksum_address("0x11fCfe756c05AD438e312a7fd934381537D3cFfe"),
                amount,
                self.address
            ).build_transaction(tx_data)

            signed_txn = await self.sign(transaction)

            txn_hash = await self.send_raw_transaction(signed_txn)

            await self.wait_until_tx_finished(txn_hash.hex())
        else:
            logger.error(f"[{self.account_id}][{self.address}] Deposit not found")
