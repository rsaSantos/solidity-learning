# Lets read a value from an already deployed contract.
# Run with "brownie run scripts/read_value.py --network kovan"

# Import brownie accounts, config file and the smart contract from /contracts
from brownie import accounts, config, SimpleStorage  # type: ignore


def read_contracts():
    # Get the latest deployment (address at /build/deployments/map.json)
    simple_storage = SimpleStorage[-1]
    print("latest_value=", simple_storage.retrieve())


def main():
    read_contracts()
