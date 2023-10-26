import asyncio
import random
import sys

import questionary
from loguru import logger
from questionary import Choice

from config import ACCOUNTS
from settings import RANDOM_WALLET, SLEEP_TO, SLEEP_FROM, QUANTITY_RUN_ACCOUNTS
from utils.helpers import get_run_accounts, update_run_accounts
from modules_settings import *


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice("1) Deposit to Scroll", deposit_scroll),
            Choice("2) Withdraw from Scroll", withdraw_scroll),
            Choice("3) Bridge Orbiter", bridge_orbiter),
            Choice("4) Wrap ETH", wrap_eth),
            Choice("5) Unwrap ETH", unwrap_eth),
            Choice("6) Swap on Skydrome", swap_skydrome),
            Choice("7) Swap on SyncSwap", swap_syncswap),
            Choice("8) Mint and Bridge Zerius NFT", mint_zerius),
            Choice("9) Create NFT collection on Omnisea", create_omnisea),
            Choice("10) Mint NFT on NFTS2ME", mint_nft),
            Choice("11) Dmail send email", send_mail),
            Choice("12) Deploy contract", deploy_contract),
            Choice("13) Use custom routes", custom_routes),
            Choice("14) Check transaction count", "tx_checker"),
            Choice("15) Exit", "exit"),
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


async def run_module(module, account_id, key, sleep_time, start_id):
    if start_id != 1:
        await asyncio.sleep(sleep_time)

    while True:
        run_accounts = get_run_accounts()

        if len(run_accounts["accounts"]) < QUANTITY_RUN_ACCOUNTS:
            update_run_accounts(account_id, "add")

            await module(account_id, key)

            update_run_accounts(account_id, "remove")

            break
        else:
            logger.info(f'Current run accounts: {len(run_accounts["accounts"])}')
            await asyncio.sleep(60)


async def main(module):
    wallets = get_wallets()

    tasks = []

    if RANDOM_WALLET:
        random.shuffle(wallets)

    sleep_time = random.randint(SLEEP_FROM, SLEEP_TO)

    for _, account in enumerate(wallets, start=1):
        tasks.append(asyncio.create_task(
            run_module(module, account["id"], account["key"], sleep_time, _)
        ))

        sleep_time += random.randint(SLEEP_FROM, SLEEP_TO)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    print("❤️ Subscribe to me – https://t.me/sybilwave\n")

    update_run_accounts(0, "new")

    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        asyncio.run(main(module))

    print("\n❤️ Subscribe to me – https://t.me/sybilwave\n")
    print("🤑 Donate me: 0x00000b0ddce0bfda4531542ad1f2f5fad7b9cde9")
