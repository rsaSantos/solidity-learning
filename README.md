# solidity-learning

**solidity-learning** is a repository that compiles Solidity & General Blockchain begginer projects.

Inspired by https://www.youtube.com/watch?v=M576WGiDBdQ & https://github.com/smartcontractkit/full-blockchain-solidity-course-py

# Lesson 1: [Simple Storage Contract](https://github.com/rsaSantos/solidity-learning/tree/main/basic-solidity)

💻 Code: https://github.com/rsaSantos/solidity-learning/tree/main/basic-solidity

### Everything in this section can be read about in the [Solidity Documentation](https://docs.soliditylang.org/en/v0.8.11/index.html)

Always check the latest version of the documentation!

### [Remix](https://remix.ethereum.org/)

### Basic Solidity

- Versioning
- Compiling
- Contract Declaration
- [Types & Declaring Variables](https://docs.soliditylang.org/en/v0.8.11/types.html)
  - `uint256`, `int256`, `bool`, `string`, `address`, `bytes32`
- Default Initializations
- Comments
- Functions
- Deploying a Contract
- Calling a public state-changing Function
- [Visibility](https://docs.soliditylang.org/en/v0.8.11/contracts.html#visibility-and-getters)
- Scope
- View & Pure Functions
- Structs
- Intro to Storage
- Arrays - Dynamic & Fixed sized
- Compiler Errors and Warnings
- Memory
- Mappings
- SPDX License
- Recap

### Deploying to a "Live" network

- A testnet or mainnet
- [Find a faucet here](https://docs.chain.link/docs/link-token-contracts/#rinkeby)
- Connecting Metamask
- Interacting with Deployed Contracts
- The EVM

# Lesson 2: [Storage Factory](https://github.com/rsaSantos/solidity-learning/tree/main/basic-solidity)

💻 Code: https://github.com/rsaSantos/solidity-learning/tree/main/basic-solidity

### Inheritance, Factory Pattern, and Interacting with External Contracts

- Factory Pattern
- Imports
- Deploy a Contract From a Contract
- Interact With a Deployed Contract
- Recap

# Lesson 3: [Fund Me](https://github.com/rsaSantos/solidity-learning/tree/main/fund-me-contract)

💻 Code: https://github.com/rsaSantos/solidity-learning/tree/main/fund-me-contract

### Payable, msg.sender, msg.value, Units of Measure

- Payable
- [Wei/Gwei/Eth Converter](https://eth-converter.com/)
- msg.sender & msg.value

### Chainlink Oracles

- Decentralized Oracle Network Chainlink
  - Blockchains can't make API calls
  - Centralized Nodes are Points of Failure
- [data.chain.link](https://data.chain.link/)
- Getting External Data with Chainlink Oracles
  - [Chainlink](https://docs.chain.link/)
  - [Faucets and Contract Addresses](https://docs.chain.link/docs/link-token-contracts/)
    - [Kovan](https://docs.chain.link/docs/link-token-contracts/#kovan)
  - [Getting Price Information](https://docs.chain.link/docs/get-the-latest-price/)

### Importing from NPM and Advanced Solidity

- Decimals/Floating Point Numbers in Solidity
- latestRoundData
- Importing from NPM in Remix
- Interfaces
  - Introduction to ABIs
- [Getting Price Feed Addresses](https://docs.chain.link/docs/reference-contracts/)
- getPrice
- Tuples
  - Unused Tuple Variables
- Matching Units (WEI/GWEI/ETH)
- getConversionRate
- Matching Units (Continued)
- SafeMath & Integer Overflow
  - using keyword
  - [Libraries](https://docs.soliditylang.org/en/v0.8.6/contracts.html#libraries)
  - SafeMath PSA
- Setting a Threshold
- Require
- Revert
- Withdraw Function
- Transfer
- Balance
- this
- Contract Owners
- Constructor
- ==
- Modifiers
- Resetting
- for loop
- Array Length
- Forcing a Transaction
- Recap

# Lesson 4: [Web3.py Simple Storage](https://github.com/rsaSantos/solidity-learning/tree/main/Web3.py)

💻 Code: https://github.com/rsaSantos/solidity-learning/tree/main/Web3.py

### Installing VSCode, Python, and Web3

- [Developer Bootcamp Setup Instructions (metamask, vscode, python, nodejs..)](https://chain.link/bootcamp/brownie-setup-instructions)
- [VSCode](https://code.visualstudio.com/download)
- [VSCode Crash Course](https://www.youtube.com/watch?v=WPqXP_kLzpo)
- Extensions
- Short Cuts:
  - [VSCode Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
  - [VSCode MacOS Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [Python](https://www.python.org/downloads/)
  - Install Troubleshooting
- Terminal
- Making a directory/Folder
- Opening the folder up with VSCode
- Creating a new file
- Syntax Highlights
- Remember to save!
- Setting linting compile version
- VSCode Solidity Settings
  - Formatting & Format on Save
  - Solidity Prettier
  - [Python Black](https://pypi.org/project/black/)
  - [pip](https://pypi.org/project/pip/)

### Our First Python Script with Web3.py - Deploying a Contract

- Reading our solidity file
- Running a Python Script in the Terminal
- [MaxOS Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [Windows Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [Linux Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
- Compiling in Python
- [py-solc-x](https://pypi.org/project/py-solc-x/)
  - compile_standard
- Colorized Brackets
- JSON ABI
- Saving Compiled Code
- Formatting JSON
- Deploying in Python
  1. Get Bytecode
  2. Get ABI
  3. Choose Blockchain to Deploy To
  - Local Ganache Chain
    - [Ganache UI](https://www.trufflesuite.com/ganache)
    - [Ganache Command Line](https://github.com/trufflesuite/ganache-cli)
- [Web3.py](https://web3py.readthedocs.io/en/stable/)
- HTTP / RPC Provider
- Private Keys MUST start with "0x"
- Contract Object
- Building a Transaction
- Account Nonce
- Calling "Constructor"
- Transaction Parameters
- Signing the Transaction
- NEVER put your private key directly in your code
- [Setting Environment Variables (Windows, Linux, MacOS)](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
  - [More on Windows Environment Variables](https://www.youtube.com/watch?v=tqWDiu8a4gc&t=40s)
- Exported Environment Variables Only Last the Duration of the Shell/Terminal
- Private Key PSA
- .env file
- .gitignore
- Loading .env File in Python
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
- Viewing our Transaction / Deployment in Ganache
- Waiting for Block Confirmations

### Interacting with Our Contract in Python & Web3.py

- 2 Things you always need
  1. Contract Address
  2. Contract ABI
- Getting address from transaction receipt
- Calling a view function with web3.py
  - Call vs Transact
- Updating State with Web3.py
- [ganache-cli](https://github.com/trufflesuite/ganache-cli)
  - Installing Ganache
    - [Install Nodejs](https://nodejs.org/en/)
    - [Install Yarn](https://classic.yarnpkg.com/en/docs/install)
- Working with ganache-cli
- Open a new terminal in the same window
- Deploying to a testnet
- [Infura](https://infura.io/)
- [Alchemy](https://www.alchemy.com/)
- Using Infura RPC URL / HTTP Provider
- [Chain Ids](https://chainlist.org/)
- Wow this seems like a lot of work... Is there a better way?
