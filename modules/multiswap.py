import random
from typing import Union

from loguru import logger
from config import SCROLL_TOKENS
from modules import *
from utils.sleeping import sleep


class Multiswap(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

        self.swap_modules = {
            "syncswap": SyncSwap,
            "skydrome": Skydrome,
            "zebra": Zebra,
            "xyswap": XYSwap,
        }

    def get_swap_module(self, use_dex: list):
        swap_module = random.choice(use_dex)

        return self.swap_modules[swap_module]

    async def swap(
            self,
            use_dex: list,
            sleep_from: int,
            sleep_to: int,
            min_swap: int,
            max_swap: int,
            slippage: Union[int, float],
            back_swap: bool,
            min_percent: int,
            max_percent: int
    ):
        quantity_swap = random.randint(min_swap, max_swap)

        path = ["ETH" if _ % 2 == 0 else "USDC" for _ in range(quantity_swap)]

        if back_swap and path[-1] == "ETH":
            path.append("USDC")

        logger.info(f"[{self.account_id}][{self.address}] Start MultiSwap | quantity swaps: {quantity_swap}")

        for _, token in enumerate(path):
            if token == "ETH":
                decimal = 6
                to_token = "USDC"

                balance = await self.w3.eth.get_balance(self.address)

                min_amount = float(self.w3.from_wei(int(balance / 100 * min_percent), "ether"))
                max_amount = float(self.w3.from_wei(int(balance / 100 * max_percent), "ether"))
            else:
                decimal = 18
                to_token = "ETH"

                balance = await self.get_balance(SCROLL_TOKENS["USDC"])

                min_amount = balance["balance"] if balance["balance"] <= 1 or _ + 1 == len(path) \
                    else balance["balance"] / 100 * min_percent
                max_amount = balance["balance"] if balance["balance"] <= 1 or _ + 1 == len(path) \
                    else balance["balance"] / 100 * max_percent

            swap_module = self.get_swap_module(use_dex)(self.account_id, self.private_key, self.recipient)
            await swap_module.swap(
                token,
                to_token,
                min_amount,
                max_amount,
                decimal,
                slippage,
                False,
                min_percent,
                max_percent
            )

            if _ + 1 != len(path):
                await sleep(sleep_from, sleep_to)
