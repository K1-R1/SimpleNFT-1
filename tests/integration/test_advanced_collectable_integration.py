from scripts.general_scripts import get_account
from brownie import network, config
import pytest, time
from scripts.advanced_collectable.deploy import deploy_and_create


def test_integration_can_create_advanced_collectible():
    #Arrange
    if not config['networks'][network.show_active()]['local'] is False:
        pytest.skip('Only tested on local networks')
    account = get_account()
    #Act
    advanced_collectable, creat_tx = deploy_and_create()
    time.sleep(75)
    #Assert
    assert advanced_collectable.tokenCounter() > 0
