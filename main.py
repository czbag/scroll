import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Union

import questionary
from loguru import logger
from questionary import Choice

from config import ACCOUNTS, RECIPIENTS
from settings import (
    RANDOM_WALLET,
    SLEEP_TO,
    SLEEP_FROM,
    QUANTITY_THREADS,
    THREAD_SLEEP_FROM,
    THREAD_SLEEP_TO, REMOVE_WALLET
)
from modules_settings import *
from utils.helpers import remove_wallet
from utils.sleeping import sleep


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice("1) Deposit to Scroll", deposit_scroll),
            Choice("2) Withdraw from Scroll", withdraw_scroll),
            Choice("3) Bridge Orbiter", bridge_orbiter),
            Choice("4) Bridge Layerswap", bridge_layerswap),
            Choice("5) Bridge Nitro", bridge_nitro),
            Choice("6) Wrap ETH", wrap_eth),
            Choice("7) Unwrap ETH", unwrap_eth),
            Choice("8) Swap on Skydrome", swap_skydrome),
            Choice("9) Swap on Zebra", swap_zebra),
            Choice("10) Swap on SyncSwap", swap_syncswap),
            Choice("11) Swap on XYSwap", swap_xyswap),
            Choice("12) Deposit LayerBank", deposit_layerbank),
            Choice("13) Deposit Aave", deposit_aave),
            Choice("14) Withdraw LayerBank", withdraw_layerbank),
            Choice("15) Withdraw Aave", withdraw_aave),
            Choice("16) Mint and Bridge Zerius NFT", mint_zerius),
            Choice("17) Mint L2Pass NFT", mint_l2pass),
            Choice("18) Mint ZkStars NFT", mint_zkstars),
            Choice("19) Create NFT collection on Omnisea", create_omnisea),
            Choice("20) RubyScore Vote", rubyscore_vote),
            Choice("21) Mint NFT on NFTS2ME", mint_nft),
            Choice("22) Dmail send email", send_mail),
            Choice("23) Create gnosis safe", create_safe),
            Choice("24) Deploy contract", deploy_contract),
            Choice("25) Swap tokens to ETH", swap_tokens),
            Choice("26) Use Multiswap", swap_multiswap),
            Choice("27) Use custom routes", custom_routes),
            Choice("28) Make transfer", make_transfer),
            Choice("29) Check transaction count", "tx_checker"),
            Choice("30) Exit", "exit"),
        ],
        qmark="⚙️ ",
        pointer="✅ "
    ).ask()
    if result == "exit":
        print("\n❤️ Subscribe to me – https://t.me/sybilwave\n")
        print("🤑 Donate me: 0x00000b0ddce0bfda4531542ad1f2f5fad7b9cde9")
        sys.exit()
    return result


def get_wallets(use_recipients: bool = False):
    if use_recipients:
        account_with_recipients = dict(zip(ACCOUNTS, RECIPIENTS))

        wallets = [
            {
                "id": _id,
                "key": key,
                "recipient": account_with_recipients[key],
            } for _id, key in enumerate(account_with_recipients, start=1)
        ]
    else:
        wallets = [
            {
                "id": _id,
                "key": key,
            } for _id, key in enumerate(ACCOUNTS, start=1)
        ]

    return wallets


async def run_module(module, account_id, key, recipient: Union[str, None] = None):
    try:
        await module(account_id, key, recipient)
    except Exception as e:
        logger.error(e)

    if REMOVE_WALLET:
        remove_wallet(key)

    await sleep(SLEEP_FROM, SLEEP_TO)


def _async_run_module(module, account_id, key, recipient):
    asyncio.run(run_module(module, account_id, key, recipient))


def main(module):
    if module in [make_transfer]:
        wallets = get_wallets(True)
    else:
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
                account.get("recipient", None)
            )
            time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))


if __name__ == '__main__':
    print("❤️ Subscribe to me – https://t.me/sybilwave\n")

    logger.add("logging.log")

    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        main(module)

    print("\n❤️ Subscribe to me – https://t.me/sybilwave\n")
    print("🤑 Donate me: 0x00000b0ddce0bfda4531542ad1f2f5fad7b9cde9")
