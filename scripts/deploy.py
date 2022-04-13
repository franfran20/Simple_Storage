from brownie import SimpleStorage

from scripts.helpful_scripts import get_account


def deploy():
    print("Deploying...")
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # we return because we use this function for testing!
    return simple_storage


def main():
    deploy()
