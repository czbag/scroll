import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import questionary
from questionary import Choice

from config import ACCOUNTS
from settings import (
    RANDOM_WALLET,
    SLEEP_TO,
    SLEEP_FROM,
    QUANTITY_THREADS,
    THREAD_SLEEP_FROM,
    THREAD_SLEEP_TO
)
from modules_settings import *
from utils.sleeping import sleep


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice("1) Deposit to Scroll", deposit_scroll),
            Choice("2) Withdraw from Scroll", withdraw_scroll),
            Choice("3) Bridge Orbiter", bridge_orbiter),
            Choice("4) Bridge Layerswap", bridge_layerswap),
            Choice("5) Wrap ETH", wrap_eth),
            Choice("6) Unwrap ETH", unwrap_eth),
            Choice("7) Swap on Skydrome", swap_skydrome),
            Choice("8) Swap on SyncSwap", swap_syncswap),
            Choice("9) Deposit LayerBank", deposit_layerbank),
            Choice("10) Withdraw LayerBank", withdraw_layerbank),
            Choice("11) Mint and Bridge Zerius NFT", mint_zerius),
            Choice("12) Create NFT collection on Omnisea", create_omnisea),
            Choice("13) Mint NFT on NFTS2ME", mint_nft),
            Choice("14) Dmail send email", send_mail),
            Choice("15) Create gnosis safe", create_safe),
            Choice("16) Deploy contract", deploy_contract),
            Choice("17) Use custom routes", custom_routes),
            Choice("18) Check transaction count", "tx_checker"),
            Choice("19) Exit", "exit"),
        ],
        qmark="⚙️ ",
        pointer="✅ "
    ).ask()
    if result == "exit":
        print("\n❤️ Subscribe to me – https://t.me/sybilwave\n")
        print("🤑 Donate me: 0x00000b0ddce0bfda4531542ad1f2f5fad7b9cde9")
        sys.exit()
    return result


def get_wallets():
    wallets = [
        {
            "id": _id,
            "key": key,
        } for _id, key in enumerate(ACCOUNTS, start=1)
    ]

    return wallets


async def run_module(module, account_id, key):
    await module(account_id, key)

    await sleep(SLEEP_FROM, SLEEP_TO)


def _async_run_module(module, account_id, key):
    asyncio.run(run_module(module, account_id, key))


def main(module):
    wallets = get_wallets()

    if RANDOM_WALLET:
        random.shuffle(wallets)

    with ThreadPoolExecutor(max_workers=QUANTITY_THREADS) as executor:
        for _, account in enumerate(wallets, start=1):
            executor.submit(
                _async_run_module,
                module,
                account.get("id"),
                account.get("key"),
            )
            time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))


if __name__ == '__main__':
    print("❤️ Subscribe to me – https://t.me/sybilwave\n")

    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        main(module)

    print("\n❤️ Subscribe to me – https://t.me/sybilwave\n")
    print("🤑 Donate me: 0x00000b0ddce0bfda4531542ad1f2f5fad7b9cde9")
