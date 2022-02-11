from scripts.general_scripts import get_account, get_contract
from brownie import network, config
import pytest
from scripts.advanced_collectable.deploy import deploy_and_create


def test_can_create_advanced_collectible():
    #Arrange
    if not config['networks'][network.show_active()]['local'] is True:
        pytest.skip('Only tested on local networkss')
    account = get_account()
    #Act
    advanced_collectable, creat_tx = deploy_and_create()
    request_id = creat_tx.events['requestedCollectable']['requestId']
    static_rng = 777
    get_contract('vrf_coordinator').callBackWithRandomness( request_id, static_rng, advanced_collectable.address, {'from': account}).wait(1)
    #Assert
    assert advanced_collectable.tokenCounter() > 0
    assert advanced_collectable.tokenIdToBreed(0) == static_rng % 3
