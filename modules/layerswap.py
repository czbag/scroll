from typing import Union, Dict

import aiohttp
from loguru import logger

from settings import LAYERSWAP_API_KEY
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class LayerSwap(Account):
    def __init__(self, account_id: int, private_key: str, chain: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain=chain, recipient=recipient)

        self.networks = {
            "ethereum": "ETHEREUM_MAINNET",
            "arbitrum": "ARBITRUM_MAINNET",
            "optimism": "OPTIMISM_MAINNET",
            "avalanche": "AVAX_MAINNET",
            "polygon": "POLYGON_MAINNET",
            "base": "BASE_MAINNET",
            "zksync": "ZKSYNCERA_MAINNET",
            "scroll": "SCROLL_MAINNET",
        }

        self.headers = {"X-LS-APIKEY": LAYERSWAP_API_KEY}

    async def check_available_route(self, from_chain: str, to_chain: str) -> Union[Dict, bool]:
        url = "https://api.layerswap.io/api/available_routes"

        params = {
            "source": self.networks[from_chain],
            "destination": self.networks[to_chain],
            "sourceAsset": "ETH",
            "destinationAsset": "ETH",
        }

        async with aiohttp.ClientSession() as session:
            response = await session.get(url=url, params=params)

            if response.status == 200:
                transaction_data = await response.json()

                if transaction_data["data"]:
                    return transaction_data["data"]
                else:
                    logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Layerswap path not found")

                    return False
            else:
                logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Bad layerswap request")

                return False

    async def get_swap_rate(self, from_chain: str, to_chain: str) -> Union[Dict, bool]:
        url = "https://api.layerswap.io/api/swap_rate"

        params = {
            "source": self.networks[from_chain],
            "source_asset": "ETH",
            "destination": self.networks[to_chain],
            "destination_asset": "ETH",
            "refuel": False
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=url, json=params)

            if response.status == 200:
                transaction_data = await response.json()

                if transaction_data["data"]:
                    return transaction_data["data"]
                else:
                    logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Layerswap swap rate error")

                    return False
            else:
                logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Bad layerswap request")

                return False

    async def create_swap(self, from_chain: str, to_chain: str, amount: float) -> Union[Dict, bool]:
        url = "https://api.layerswap.io/api/swaps"

        params = {
            "source": self.networks[from_chain],
            "source_asset": "ETH",
            "destination": self.networks[to_chain],
            "destination_asset": "ETH",
            "refuel": False,
            "amount": float(amount),
            "destination_address": self.address
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=url, headers=self.headers, json=params)

            if response.status == 200:
                transaction_data = await response.json()

                if transaction_data["data"]:
                    return transaction_data["data"]["swap_id"]
                else:
                    logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Layerswap swap rate error")

                    return False
            else:
                logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Bad layerswap request")

                return False

    async def prepare_transaction(self, from_chain: str, to_chain: str, amount: float) -> Union[Dict, bool]:
        swap_id = await self.create_swap(from_chain, to_chain, amount)

        url = f"https://api.layerswap.io/api/swaps/{swap_id}/prepare_src_transaction"

        params = {
            "from_address": self.address
        }

        async with aiohttp.ClientSession() as session:
            response = await session.get(url=url, headers=self.headers, params=params)

            if response.status == 200:
                transaction_data = await response.json()

                if transaction_data["data"]:
                    return transaction_data["data"]
                else:
                    logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Layerswap swap rate error")

                    return False
            else:
                logger.error(f"[{self.account_id}][{self.address}][{self.chain}] Bad layerswap request")

                return False

    @retry
    @check_gas
    async def bridge(
            self,
            from_chain: str,
            to_chain: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ):
        amount_wei, amount, balance = await self.get_amount(
            "ETH",
            min_amount,
            max_amount,
            decimal,
            all_amount,
            min_percent,
            max_percent
        )

        available_route = await self.check_available_route(from_chain, to_chain)

        if available_route is False:
            return

        swap_rate = await self.get_swap_rate(from_chain, to_chain)

        if amount < swap_rate["min_amount"] or amount > swap_rate["max_amount"]:
            logger.error(
                f"[{self.account_id}][{self.address}][{self.chain}] Limit range amount for bridge " +
                f"{swap_rate['min_amount']} – {swap_rate['max_amount']} ETH | {amount} ETH"
            )
            return

        if swap_rate is False:
            return

        prepare_transaction = await self.prepare_transaction(from_chain, to_chain, amount)

        if prepare_transaction is False:
            return

        logger.info(f"[{self.account_id}][{self.address}] Bridge {from_chain} –> {to_chain} | {amount} ETH")

        tx_data = await self.get_tx_data(amount_wei)
        tx_data.update({"to": self.w3.to_checksum_address(prepare_transaction["to_address"])})

        signed_txn = await self.sign(tx_data)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
