import json

with open('data/rpc.json') as file:
    RPC = json.load(file)

with open('data/abi/erc20_abi.json') as file:
    ERC20_ABI = json.load(file)

with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open('data/abi/bridge/deposit.json') as file:
    DEPOSIT_ABI = json.load(file)

with open('data/abi/bridge/withdraw.json') as file:
    WITHDRAW_ABI = json.load(file)

with open('data/abi/bridge/oracle.json') as file:
    ORACLE_ABI = json.load(file)

with open('data/abi/scroll/weth.json') as file:
    WETH_ABI = json.load(file)

with open("data/abi/syncswap/router.json", "r") as file:
    SYNCSWAP_ROUTER_ABI = json.load(file)

with open('data/abi/syncswap/classic_pool.json') as file:
    SYNCSWAP_CLASSIC_POOL_ABI = json.load(file)

with open('data/abi/syncswap/classic_pool_data.json') as file:
    SYNCSWAP_CLASSIC_POOL_DATA_ABI = json.load(file)

with open("data/abi/skydrome/abi.json", "r") as file:
    SKYDROME_ROUTER_ABI = json.load(file)

with open("data/abi/layerbank/abi.json", "r") as file:
    LAYERBANK_ABI = json.load(file)

with open("data/abi/zerius/abi.json", "r") as file:
    ZERIUS_ABI = json.load(file)

with open("data/abi/dmail/abi.json", "r") as file:
    DMAIL_ABI = json.load(file)

with open("data/abi/omnisea/abi.json", "r") as file:
    OMNISEA_ABI = json.load(file)

with open("data/abi/nft2me/abi.json", "r") as file:
    NFTS2ME_ABI = json.load(file)

with open("data/abi/gnosis/abi.json", "r") as file:
    SAFE_ABI = json.load(file)

with open("data/deploy/abi.json", "r") as file:
    DEPLOYER_ABI = json.load(file)

with open("data/deploy/bytecode.txt", "r") as file:
    DEPLOYER_BYTECODE = file.read()

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

BRIDGE_CONTRACTS = {
    "deposit": "0xf8b1378579659d8f7ee5f3c929c2f3e332e41fd6",
    "withdraw": "0x4C0926FF5252A435FD19e10ED15e5a249Ba19d79",
    "oracle": "0x987e300fDfb06093859358522a79098848C33852"
}

ORBITER_CONTRACT = "0x80c67432656d59144ceff962e8faf8926599bcf8"

SCROLL_TOKENS = {
    "ETH": "0x5300000000000000000000000000000000000004",
    "WETH": "0x5300000000000000000000000000000000000004",
    "USDC": "0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4"
}

SYNCSWAP_CONTRACTS = {
    "router": "0x80e38291e06339d10aab483c65695d004dbd5c69",
    "classic_pool": "0x37BAc764494c8db4e54BDE72f6965beA9fa0AC2d"
}

SKYDROME_CONTRACTS = {
    "router": "0xAA111C62cDEEf205f70E6722D1E22274274ec12F"
}

LAYERBANK_CONTRACT = "0xec53c830f4444a8a56455c6836b5d2aa794289aa"

LAYERBANK_WETH_CONTRACT = "0x274C3795dadfEbf562932992bF241ae087e0a98C"

ZERIUS_CONTRACT = "0xeb22c3e221080ead305cae5f37f0753970d973cd"

DMAIL_CONTRACT = "0x47fbe95e981c0df9737b6971b451fb15fdc989d9"

OMNISEA_CONTRACT = "0x46ce46951d12710d85bc4fe10bb29c6ea5012077"

SAFE_CONTRACT = "0xa6b71e26c5e0845f74c812102ca7114b6a896ab2"
