from scripts.deploy import deploy
import pytest
from scripts.helpful_scripts import get_account


def test_contract():
    account = get_account()
    simple_storage = deploy()
    tx_store = simple_storage.store(37, {"from": account})
    tx_store.wait(1)

    # expected value
    expected_value = 37
    assert expected_value == simple_storage.retrieve()
