from brownie import LamboToken, accounts, config, network
from scripts.helpful_scripts import (
    get_account,
)

INITIAL_SUPPLY = 100 * 10 ** 18


def deploy_lambo_token():
    account = get_account()

    lambo_token = LamboToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"LamboToken contract address: {lambo_token.address}")
    return lambo_token


def main():
    """Deploys the LamboToken contract."""
    lambo_token = deploy_lambo_token()
