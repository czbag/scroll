# RANDOM WALLETS MODE
RANDOM_WALLET = True  # True/False

# removing a wallet from the list after the job is done
REMOVE_WALLET = False

SLEEP_FROM = 500  # Second
SLEEP_TO = 1000  # Second

QUANTITY_THREADS = 1

THREAD_SLEEP_FROM = 5
THREAD_SLEEP_TO = 5

# GWEI CONTROL MODE
CHECK_GWEI = False  # True/False
MAX_GWEI = 20

MAX_PRIORITY_FEE = {
    "ethereum": 0.01,
    "polygon": 40,
    "arbitrum": 0.1,
    "base": 0.1,
    "zksync": 0.25,
}

GAS_MULTIPLIER = 1.3

# RETRY MODE
RETRY_COUNT = 3

LAYERSWAP_API_KEY = ""
