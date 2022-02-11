# Importing solc-x
# Check it out at https://pypi.org/project/py-solc-x/
from solcx import compile_standard, install_solc

# So that we can create a file with the compiled contract aka bytecode.
import json

# Read the docs at https://web3py.readthedocs.io/en/stable/
from web3 import Web3

# Get environment variables with getenv.
import os

# Get private keys from .env file.
from dotenv import load_dotenv

# Import keys and other environment variables from .env file.
load_dotenv()

# Open SimpleStorage contract.
with open("./SimpleStorage.sol", "r") as file:
    # Reading the file. Test with print(simple_storage_file)
    simple_storage_file = file.read()

# Installing solidity compiler...
print("Installing...")
install_solc("0.8.0")

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "metadata",
                        "evm.bytecode",
                        "evm.bytecode.sourceMap",
                    ]
                }
            }
        },
    }
)

# Contract was compiled. Print the compiled code to a file.
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# To deploy the contract, first let's get the bytecode.
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# Get abi -
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


# Where do we deploy the contract?
# We will deploy this contract in Ganache!
# Check it out at https://trufflesuite.com/ganache/

# Let's use an HTTP provider to connect to the blockchain.
# We can use infura or alchemy to get a testnet/mainnet url.
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

# If we choose to use infura or alchemy use the address and private key from metamask/other wallet.
# Save another usefull information about our ganache blockchain.
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"

# NEVER HARDCODE THE PRIVATE KEY...alternatives ahead!
# my_private_key = "0xcb5b17ec09e7f966a07e1325feef6973bc87c586494453129e30dac43004d2cc"
# my_private_key = os.getenv("PRIVATE_KEY_GANACHE")
# Create .env file and store the variables there. Create .gitignore and add .env.
my_private_key = os.getenv("PRIVATE_KEY")

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# Steps to follow in order to deploy the contract.
# 1. Build a transaction.
# 2. Sign a transaction.
# 3. Send a transaction.

# 1. Create the transaction that deploys the contract
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

# 2. Sign the transaction.
signed_txn = w3.eth.account.sign_transaction(transaction, my_private_key)

# 3. Send the transaction.
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Get the transaction receipt - wait a few block confirmations...
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")


# Working with deployed Contracts
# To work with the contract we need
# Contract ABI
# Contract Address
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)


# Call      : Simulate making the call and getting a return value (read-only).
# Transact  : Making a state change.

# Let's call the retrieve function and print the result.
# Since this function is view and doesn't make a state change, we use the call method.
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")

# Let's now try to call the store function.
# This function will store a value in the contract, so it will be a Transact.
# Transact will need to follow
#   Create the transaction
#   Sign the transaction
#   Send the transaction

# Building the transaction.
greeting_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)

# Signing the transaction.
signed_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=my_private_key
)

# Sending the transaction.
tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)

# Get the receipt.
print("Updating stored Value...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

# Get latest contract status via retrieve function call.
print(simple_storage.functions.retrieve().call())
