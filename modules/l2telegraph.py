import random
from typing import Dict

from loguru import logger

from utils.gas_checker import check_gas
from utils.helpers import retry
from utils.sleeping import sleep
from .account import Account
from config import (
    L2TELEGRAPH_MESSAGE_CONTRACT,
    L2TELEGRAPH_NFT_CONTRACT,
    L2TELEGRAPH_MESSAGE_ABI,
    L2TELEGRAPH_NFT_ABI
)


class L2Telegraph(Account):
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

        self.chains_id = {
            "bsc": 102,
            "optimism": 111,
            "avalanche": 106,
            "arbitrum": 110,
            "polygon": 109,
            "linea": 183,
            "moonbeam": 126,
            "kava": 177,
            "telos": 199,
            "klaytn": 150,
            "gnosis": 145,
            "moonriver": 167,
        }

    async def get_estimate_fee(self, contract_address: str, abi: dict, chain_id: int):
        contract = self.get_contract(contract_address, abi)

        fee = await contract.functions.estimateFees(
            chain_id,
            self.address,
            "0x",
            False,
            "0x"
        ).call()

        return int(fee[0] * 1.2)

    async def get_nft_id(self, txn_hash: str):
        receipts = await self.w3.eth.get_transaction_receipt(txn_hash)

        nft_id = int(receipts["logs"][0]["topics"][-1].hex(), 0)

        return nft_id

    @retry
    @check_gas
    async def send_message(self, use_chain: list):
        random_chain = random.choice(use_chain)

        logger.info(f"[{self.account_id}][{self.address}] Send message to {random_chain.title()}")

        l0_fee = await self.get_estimate_fee(
            L2TELEGRAPH_MESSAGE_CONTRACT,
            L2TELEGRAPH_MESSAGE_ABI,
            self.chains_id[random_chain]
        )

        tx_data = await self.get_tx_data(self.w3.to_wei(0.00025, "ether") + l0_fee)

        contract = self.get_contract(L2TELEGRAPH_MESSAGE_CONTRACT, L2TELEGRAPH_MESSAGE_ABI)

        transaction = await contract.functions.sendMessage(
            ' ',
            self.chains_id[random_chain],
            "0xdc60fd9d2a4ccf97f292969580874de69e6c326e9f63dbdf90837384872828d1ed6eb424a7f7f939"
        ).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

    async def mint(self):
        logger.info(f"[{self.account_id}][{self.address}] Mint NFT")

        tx_data = await self.get_tx_data(self.w3.to_wei(0.0005, "ether"))

        contract = self.get_contract(L2TELEGRAPH_NFT_CONTRACT, L2TELEGRAPH_NFT_ABI)

        transaction = await contract.functions.mint().build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

        nft_id = await self.get_nft_id(txn_hash.hex())

        return nft_id

    @retry
    @check_gas
    async def bridge(self, use_chain: list, sleep_from: int, sleep_to: int):
        random_chain = random.choice(use_chain)

        l0_fee = await self.get_estimate_fee(
            L2TELEGRAPH_MESSAGE_CONTRACT,
            L2TELEGRAPH_MESSAGE_ABI,
            self.chains_id[random_chain]
        )

        nft_id = await self.mint()

        await sleep(sleep_from, sleep_to)

        tx_data = await self.get_tx_data(l0_fee)

        logger.info(f"[{self.account_id}][{self.address}] Bridge NFT [{nft_id}] to {random_chain.title()}")

        contract = self.get_contract(L2TELEGRAPH_NFT_CONTRACT, L2TELEGRAPH_NFT_ABI)

        transaction = await contract.functions.crossChain(
            self.chains_id[random_chain],
            "0xc162cf8c4c6697ab8e613ce0cd37c0ab97ba5a60dc60fd9d2a4ccf97f292969580874de69e6c326e",
            nft_id
        ).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
