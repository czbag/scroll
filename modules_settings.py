import asyncio
from modules import *


async def deposit_scroll(account_id, key, recipient):
    """
    Deposit from official bridge
    ______________________________________________________
    all_amount - bridge from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 1
    max_percent = 1

    scroll = Scroll(account_id, key, "ethereum", recipient)
    await scroll.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def withdraw_scroll(account_id, key, recipient):
    """
    Withdraw from official bridge
    ______________________________________________________
    all_amount - withdraw from min_percent to max_percent
    """

    min_amount = 0.0012
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 10
    max_percent = 10

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.withdraw(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_orbiter(account_id, key, recipient):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync, scroll | Select one
    to_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync, scroll | Select one
    """

    from_chain = "scroll"
    to_chain = "base"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

    orbiter = Orbiter(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_layerswap(account_id, key, recipient):
    """
    Bridge from Layerswap
    ______________________________________________________
    from_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll
    to_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll

    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.003
    max_amount = 0.004

    decimal = 5

    all_amount = True

    min_percent = 5
    max_percent = 5

    layerswap = LayerSwap(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await layerswap.bridge(
        from_chain, to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent
    )


async def bridge_nitro(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def wrap_eth(account_id, key, recipient):
    """
    Wrap ETH
    ______________________________________________________
    all_amount - wrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 5
    max_percent = 10

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.wrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def unwrap_eth(account_id, key, recipient):
    """
    Unwrap ETH
    ______________________________________________________
    all_amount - unwrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.unwrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_skydrome(account_id, key, recipient):
    """
    Make swap on Skydrome
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    skydrome = Skydrome(account_id, key, recipient)
    await skydrome.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_zebra(account_id, key, recipient):
    """
    Make swap on Zebra
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    zebra = Zebra(account_id, key, recipient)
    await zebra.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_syncswap(account_id, key, recipient):
    """
    Make swap on SyncSwap

    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer – Don't use stable coin in from and to token | from_token USDC to_token USDT DON'T WORK!!!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 1
    max_amount = 2
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    syncswap = SyncSwap(account_id, key, recipient)
    await syncswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_xyswap(account_id, key, recipient):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    xyswap = XYSwap(account_id, key, recipient)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def deposit_layerbank(account_id, key, recipient):
    """
    Make deposit on LayerBank
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_aave(account_id, key, recipient):
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    aave = Aave(account_id, key, recipient)
    await aave.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def mint_zerius(account_id, key, recipient):
    """
    Mint + bridge Zerius NFT
    ______________________________________________________
    chains - list chains for random chain bridge: arbitrum, optimism, polygon, bsc, avalanche
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    chains = ["arbitrum"]

    sleep_from = 10
    sleep_to = 20

    zerius = Zerius(account_id, key, recipient)
    await zerius.bridge(chains, sleep_from, sleep_to)


async def mint_l2pass(account_id, key, recipient):
    """
    Mint L2Pass NFT
    """

    contract = "0x0000049f63ef0d60abe49fdd8bebfa5a68822222"

    l2pass = L2Pass(account_id, key, recipient)
    await l2pass.mint(contract)


async def mint_nft(account_id, key, recipient):
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    contracts - list NFT contract addresses
    """

    contracts = [
        "0x9f739d133689244a0Ff2752eB1796D385C0Ca358",
        "0x7301a42D2d58e702C2439fBE8925D9Ad9d2Cc264",
        "0x2B7128e8c493e18759c5346AE68B3a53645A8568",
        "0x818CeE34a3a4cD0B465028C6200A2656480C88ce",
        "0xbDa15D2f6d9b0177b31574E50A6e4eC0f2f5CE74",
        "0xC87CE5B3648Ef8ea832b18e44020eB0cF3D8642e",
        "0xED3aE48d051e1b8EecE2b4AFaA485641398f5984",
        "0x6C02Eae312d466549380Cc344456F85c158434de",
        "0xC48182c7b60E03908e7D966Db2caf91E26bB4cFE",
        "0xf4e7eBcA3C4EAe2ee937c80d24F7593226068c73",
        "0x3f7099923c98E2FFCe08acd241FDFeDb0e1BBBb3",
        "0x1DfaDd24Eec719Ea4E451a603bf302e11f810183",
        "0x68E63042789966765A5eF89a3A8bdEf4f8b8A81D",
        "0xE59ECCeEBDE3f0063f2FcBf71eDfB6855EC662ac",
        "0x0fe92b4cb60aFafdbf63b396A553288e1b138e5A",
        "0xf4d4e95c1A35381da8E2dA1062dCabe9d58fCC9C",
        "0x4e9E3AAeF27fb4b39B6df9af6c83DBDa4ca2A3ea",
        "0x5520f2cD1F119f242CFAE54309F2518e66f48D4E",
        "0x9751686A5bE48b89929667c92c3d2e1EaA2F6f4d",
        "0x474a65B257DD2F918b3f2c58092D86F58AaF59D0",
        "0xaE9F1386e511D6D678C01Cb04e079BE04a19ED33",
        "0xE7a9d25159F5d7032a5Aec16269443B5ee26502C",
        "0xF41716cF7214BF319B8D914312D225cbB91e0FdA",
        "0x7e8Ab3A1f112E50B0595B1eed80c3859a15ed40A",
        "0xcCF35758aBdE587a4A5F552Cc9EE8Ff60086065F",
        "0x09BD34B9C8049e23984E9D09821Eb2AE0693ab45",
        "0x251c07a78832f53471460D34c93974825791cecf",
        "0x4C826C813f7D622EDAccE46abe0d89BE3478aA45",
        "0x97d976568A36bAC0bAD93B3FB9452b461EDf1DbE",
        "0x1150E28602b673226F1627c6493E869AF1e26f34",
        "0x200c7C35936c807354a0a5905d8c9F7BBBfAb5bE",
        "0x01517f5C684A82C773D290Ccb82FBc2D53958774",
        "0x819bf0616f030cB4F19D8a2b636D42701Af22B43",
        "0xd1f612e1531E1F25ec851B8D7160F9e10F6Ca289",
        "0x624CA1be563d74aE16393200B81f8dFa1a41643b",
        "0x9bF210F821F5FD62E539cd00BAb1e056900A2313",
        "0xf70F60144A608001941Be3569b42C5eb9DbdD82a",
        "0x9A37AA46179635304CDE84D6a74B7139CD566Daf",
        "0x0dA9ac979b01ad5029E13A9C24FFC70f7a087176",
        "0x1f1AFe43B8278adf0D89f4960507b731454Ba1c8",
        "0x53fbd662B453344603aAF23caF79EB78A7F375fE",
        "0x7fBa1e70D645b3AfF359C360C91acFc3b8D42Ee6",
        "0x134C53C4310AC4a3D8e64DA4E72B7D23ad7038F6",
        "0x1C5A64725f0cFD6D059B049E14d7800a639B9517",
        "0x15e6E3256F4A919438a2BF7d6CFE99cAE53eb1A1",
        "0xA67e2cd55dD9F2c183cfA4400DCa9F92f86E84C7",
        "0xE5D0Ec076a3A94C6174b63C50A6918A4511241a7",
        "0x07bD384F702EbAD9Da8Bd66e2274841f42C88597",
        "0x19Fa769FA67663BA72865CA555D6A86a986442a5",
        "0x63FC03FfabbF53Ed1de9DAB6B80aDBe4Ce85443B"
                ]

    minter = Minter(account_id, key, recipient)
    await minter.mint_nft(contracts)


async def mint_zkstars(account_id, key, recipient):
    """
    Mint ZkStars NFT
    """

    contracts = [
        "0x609c2f307940b8f52190b6d3d3a41c762136884e",
        "0x16c0baa8a2aa77fab8d0aece9b6947ee1b74b943",
        "0xc5471e35533e887f59df7a31f7c162eb98f367f7",
        "0xf861f5927c87bc7c4781817b08151d638de41036",
        "0x954e8ac11c369ef69636239803a36146bf85e61b",
        "0xa576ac0a158ebdcc0445e3465adf50e93dd2cad8",
        "0x17863384c663c5f95e4e52d3601f2ff1919ac1aa",
        "0x4c2656a6d1c0ecac86f5024e60d4f04dbb3d1623",
        "0x4e86532cedf07c7946e238bd32ba141b4ed10c12",
        "0x6b9db0ffcb840c3d9119b4ff00f0795602c96086",
        "0x10d4749bee6a1576ae5e11227bc7f5031ad351e4",
        "0x373148e566e4c4c14f4ed8334aba3a0da645097a",
        "0xdacbac1c25d63b4b2b8bfdbf21c383e3ccff2281",
        "0x2394b22b3925342f3216360b7b8f43402e6a150b",
        "0xf34f431e3fc0ad0d2beb914637b39f1ecf46c1ee",
        "0x6f1e292302dce99e2a4681be4370d349850ac7c2",
        "0xa21fac8b389f1f3717957a6bb7d5ae658122fc82",
        "0x1b499d45e0cc5e5198b8a440f2d949f70e207a5d",
        "0xec9bef17876d67de1f2ec69f9a0e94de647fcc93",
        "0x5e6c493da06221fed0259a49beac09ef750c3de1"
    ]

    mint_min = 1
    mint_max = 1

    mint_all = False

    sleep_from = 5
    sleep_to = 10

    zkkstars = ZkStars(account_id, key, recipient)
    await zkkstars.mint(contracts, mint_min, mint_max, mint_all, sleep_from, sleep_to)


async def send_message(account_id, key, recipient):
    """
    Send message with L2Telegraph
    ______________________________________________________
    chain - select need chain to send message, you can specify several, one will be selected randomly

    availiable chaines: bsc, optimism, avalanche, arbitrum, polygon, linea, moonbeam, kava, telos, klaytn, gnosis, moonriver
    """
    use_chain = ["gnosis", "moonriver"]

    l2telegraph = L2Telegraph(account_id, key, recipient)
    await l2telegraph.send_message(use_chain)


async def bridge_nft(account_id, key, recipient):
    """
    Make mint NFT and bridge NFT on L2Telegraph
    ______________________________________________________
    chain - select need chain to send message, you can specify several, one will be selected randomly

    availiable chaines: bsc, optimism, avalanche, arbitrum, polygon, linea
    """
    use_chain = ["polygon"]

    sleep_from = 5
    sleep_to = 20

    l2telegraph = L2Telegraph(account_id, key, recipient)
    await l2telegraph.bridge(use_chain, sleep_from, sleep_to)


async def make_transfer(_id, key, recipient):
    """
    Transfer ETH
    """

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    all_amount = True

    min_percent = 10
    max_percent = 10

    transfer = Transfer(_id, key, recipient)
    await transfer.transfer(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_tokens(account_id, key, recipient):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    """

    use_dex = [
        "syncswap", "skydrome", "zebra"
    ]

    use_tokens = ["USDC"]

    sleep_from = 1
    sleep_to = 5

    slippage = 0.1

    min_percent = 100
    max_percent = 100

    swap_tokens = SwapTokens(account_id, key, recipient)
    await swap_tokens.swap(use_dex, use_tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def swap_multiswap(account_id, key, recipient):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    quantity_swap - Quantity swaps
    ______________________________________________________
    If back_swap is True, then, if USDC remains, it will be swapped into ETH.
    """

    use_dex = ["syncswap", "skydrome", "zebra"]

    min_swap = 3
    max_swap = 4

    sleep_from = 3
    sleep_to = 7

    slippage = 0.1

    back_swap = True

    min_percent = 5
    max_percent = 10

    multi = Multiswap(account_id, key, recipient)
    await multi.swap(
        use_dex, sleep_from, sleep_to, min_swap, max_swap, slippage, back_swap, min_percent, max_percent
    )


async def multibridge(account_id, key, recipient):
    """
    MultriBridge - Makes a bridge from a random network where there is a minimum acceptable balance
    ______________________________________________________
    use_bridge - right now only nitro

    source_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one or more
    destination_chain - ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one

    min_chain_balance - minimum acceptable balance for bridge
    """

    use_bridge = "nitro"

    source_chain = ["optimism", "zksync", "base", "linea"]
    destination_chain = "scroll"

    min_amount = 0.005
    max_amount = 0.006
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

    min_chain_balance = 0.006

    multibridge = Multibridge(account_id=account_id, private_key=key, recipient=recipient)
    await multibridge.bridge(use_bridge, source_chain, destination_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, min_chain_balance)


async def custom_routes(account_id, key, recipient):
    """
    BRIDGE:
        – deposit_scroll
        – withdraw_scroll
        – bridge_orbiter
        – bridge_layerswap
        – bridge_nitro
    WRAP:
        – wrap_eth
        – unwrap_eth
    DEX:
        – swap_skydrome
        – swap_syncswap
        – swap_zebra
        – swap_xyswap
    LIQUIDITY:
    LANDING:
        – depost_layerbank
        – withdraw_layerbank
        – deposit_aave
        – withdraw_aave
    NFT/DOMAIN:
        – mint_zerius
        – mint_zkstars
        – create_omnisea
        – mint_nft
        – mint_l2pass
    ANOTHER:
        – swap_multiswap
        – multibridge
        – swap_tokens
        – send_mail (Dmail)
        – create_safe
        – rubyscore_vote
        – deploy_contract
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4

    You can also specify None in [], and if None is selected by random, this module will be skipped

    You can also specify () to perform the desired action a certain number of times
    example (send_mail, 1, 10) run this module 1 to 10 times
    """

    use_modules = [
        create_omnisea,
        [create_omnisea, mint_zerius, None],
        (create_omnisea, 1, 3),
    ]

    sleep_from = 300
    sleep_to = 700

    random_module = True

    routes = Routes(account_id, key, recipient)
    await routes.start(use_modules, sleep_from, sleep_to, random_module)


#########################################
########### NO NEED TO CHANGE ###########
#########################################

async def withdraw_layerbank(account_id, key, recipient):
    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.withdraw()


async def withdraw_aave(account_id, key, recipient):
    aave = Aave(account_id, key, recipient)
    await aave.withdraw()


async def send_mail(account_id, key, recipient):
    dmail = Dmail(account_id, key, recipient)
    await dmail.send_mail()


async def create_omnisea(account_id, key, recipient):
    omnisea = Omnisea(account_id, key, recipient)
    await omnisea.create()


async def create_safe(account_id, key, recipient):
    gnosis_safe = GnosisSafe(account_id, key, recipient)
    await gnosis_safe.create_safe()


async def deploy_contract(account_id, key, recipient):
    deployer = Deployer(account_id, key, recipient)
    await deployer.deploy_token()


async def rubyscore_vote(account_id, key, recipient):
    rubyscore = RubyScore(account_id, key, recipient)
    await rubyscore.vote()


async def nft_origins(account_id, key, recipient):
    nft = NftOrigins(account_id, key, recipient)
    await nft.mint()


def get_tx_count():
    asyncio.run(check_tx())
