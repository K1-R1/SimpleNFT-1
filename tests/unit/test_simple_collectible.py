from scripts.general_scripts import get_account
from brownie import network, config
import pytest
from scripts.deploy import main


def test_can_create_simple_collectible():
    if not config['networks'][network.show_active()]['local'] is True:
        pytest.skip('Only tested on local networkss')

    simple_collectible = main()
    
    assert simple_collectible.ownerOf(0) == get_account()