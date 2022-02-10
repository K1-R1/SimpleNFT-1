import imp
from scripts.general_scripts import get_account
from brownie import SimpleCollectable


sample_token_uri = "ipfs://ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
opensea_url = 'https://testnets.opensea.io/assets/{}/{}'


def main():
    account = get_account()
    simple_collectable = SimpleCollectable.deploy({'from': account})
    tx = simple_collectable.createCollectable(sample_token_uri, {'from': account})
    tx.wait(1)

    print(f"NFT viewable at {opensea_url.format(simple_collectable.address, (simple_collectable.tokenCounter() - 1))}")

    return simple_collectable