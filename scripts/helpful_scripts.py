from brownie import accounts, network

LOCAL_BLOCKCHAIN_ENV = ["development"]


def get_account(index=None, id=None):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
