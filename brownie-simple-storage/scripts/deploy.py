# Let's deploy a contract (contracts at /contracts)
# Run scripts with brownie run scripts/deploy.py
#
# To deploy in testnet use "brownie run scripts/deploy.py --network kovan"
# Default run script will use ganache local accounts.

# .env related
import os

# Import brownie accounts, config file and the smart contract from /contracts
from brownie import accounts, config, SimpleStorage, network  # type: ignore


# Here are shown 4 ways to get an account address/private key.
def deploy_simple_storage():
    # Built-in local account
    # account = accounts[0]

    # Load our local brownie account
    # account = accounts.load("solidity-learn")

    # Import from .env file (no need to always insert password)
    # account = accounts.add(os.getenv("PRIVATE_KEY"))

    # Import from the brownie-config file.
    # account = accounts.add(config["wallets"]["from_key"])

    # Use get account function.
    account = get_account()

    # Deploy contract (no need to use all the complicated procedure from Web3.py)
    simple_storage = SimpleStorage.deploy({"from": account})

    # Get current stored value from contract.
    stored_value = simple_storage.retrieve()

    # Store transaction (wait 1 block)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    # Get the updated stored value.
    stored_value = simple_storage.retrieve()


# If we're using a development network, use ganache account, else use config file.
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        print(network.show_active())
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
