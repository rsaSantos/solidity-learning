# Compilation of helpfull scripts.

# Import brownie accounts, config file and the smart contract from /contracts
from brownie import accounts, config, network, MockV3Aggregator  # type: ignore
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "solidity-learn"]

DECIMALS = 8
STARTING_PRICE = 200000000000


# If we're using a development network, use ganache account, else use config file.
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        print(network.show_active())
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(current_network):
    print(f"The active network is {current_network}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
        print("Mocks deployed!")
