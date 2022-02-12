# Let's deplay the fundMe contract.
# Use "brownie run scripts/deploy.py --network kovan"

# Imports
from brownie import FundMe, network, config, MockV3Aggregator  # type: ignore
from scripts.helpfull_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


# Deploy FundMe contract.
def deploy_fund_me():
    account = get_account()

    # Pass the price feed address to our FundMe contract.
    current_network = network.show_active()
    if current_network not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][current_network]["eth_usd_price_feed"]
    else:
        # This is a mock, since we are in development network.
        deploy_mocks(current_network)
        # Using the latest mock aggregator!
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fund_me.address}")

    return fund_me


def main():
    deploy_fund_me()
