from scripts.general_scripts import opensea_url, get_account, get_contract, fund_with_link
from brownie import AdvancedCollectable, config, network


def deploy_and_create():
    account = get_account()
    advanced_collectable = AdvancedCollectable.deploy(
        get_contract('vrf_coordinator'),
        get_contract('link_token'),
        config['networks'][network.show_active()]['vrf_key_hash'],
        config['networks'][network.show_active()]['vrf_fee'],
        {'from': account})
    fund_with_link(advanced_collectable.address)
    creat_tx = advanced_collectable.createCollectable({'from': account})
    creat_tx.wait(1)
    print('New collectable has been created ...\n')
    return advanced_collectable, creat_tx

def main():
    deploy_and_create()