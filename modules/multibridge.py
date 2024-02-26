import random
from typing import Union

from loguru import logger
from config import SCROLL_TOKENS
from modules import *
from utils.sleeping import sleep


class Multibridge(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

        self.bridge_modules = {
            "nitro": Nitro,
        }

    def get_bridge_module(self, use_bridge: str):
        return self.bridge_modules[use_bridge]

    async def get_native_balances(self, chains: list, min_chain_balance: float):
        chain_list = []

        for chain in chains:
            chain_acc = Account(self.account_id, self.private_key, chain, self.recipient)

            balance = await chain_acc.w3.eth.get_balance(self.address)

            print({"chain": chain, "balance_wei": balance, "balance": self.w3.from_wei(balance, "ether")})

            if balance > self.w3.to_wei(min_chain_balance, "ether"):
                chain_list.append(chain)

        return chain_list

    async def bridge(
            self,
            use_bridge: str,
            source_chain: list,
            destination_chain: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int,
            min_chain_balance: float
    ):

        chain_list = await self.get_native_balances(source_chain, min_chain_balance)

        source_chain = random.choice(chain_list)

        bridge_module = self.get_bridge_module(use_bridge)(
            self.account_id, self.private_key, source_chain, self.recipient
        )
        await bridge_module.bridge(
            destination_chain,
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )
