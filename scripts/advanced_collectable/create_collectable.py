from scripts.general_scripts import opensea_url, get_account, get_contract, fund_with_link
from brownie import AdvancedCollectable, config, network

def main():
    create_collectable()

def create_collectable():
    account = get_account()
    advanced_collectable = AdvancedCollectable[-1]
    fund_with_link(advanced_collectable.address)
    advanced_collectable.createCollectable({'from': account}).wait(1)
    print('New collectable has been created ...\n')