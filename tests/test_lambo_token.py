from brownie import LamboToken, accounts, network
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_lambo_token
from web3 import Web3
import pytest


def test_info():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only run this test on local blockchain")

    lambo_token = deploy_lambo_token()
    assert lambo_token.name() == "LamboToken"
    assert lambo_token.symbol() == "LAMBO"
    assert lambo_token.decimals() == 18


def test_mints_initial_supply():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only run this test on local blockchain")
    lambo_token = deploy_lambo_token()
    account = get_account()
    assert lambo_token.totalSupply() == 100 * 10 ** 18
    assert lambo_token.balanceOf(account) == 100 * 10 ** 18


def test_can_transfer_lambo_token():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only run this test on local blockchain")

    lambo_token = deploy_lambo_token()
    account0 = get_account(index=0)
    account1 = get_account(index=1)

    assert lambo_token.balanceOf(account0) == 100 * 10 ** 18
    assert lambo_token.balanceOf(account1) == 0

    lambo_token.transfer(account1, 50 * 10 ** 18, {"from": account0})

    assert lambo_token.balanceOf(account0) == 50 * 10 ** 18
    assert lambo_token.balanceOf(account1) == 50 * 10 ** 18
