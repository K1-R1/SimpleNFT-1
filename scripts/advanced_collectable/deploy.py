from scripts.general_scripts import opensea_url, get_account, get_contract, fund_with_link
from brownie import AdvancedCollectable, config, network


def main():
    account = get_account()
    advanced_collectable = AdvancedCollectable.deploy(
        get_contract('vrf_coordinator'),
        get_contract('link_token'),
        config['networks'][network.show_active()]['vrf_key_hash'],
        config['networks'][network.show_active()]['vrf_fee'],
        {'from': account})
    fund_with_link(advanced_collectable.address)
    advanced_collectable.createCollectable({'from': account}).wait(1)
    print('New collectable has been created ...\n')