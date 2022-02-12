from scripts.general_scripts import opensea_url, get_account, get_breed
from scripts.advanced_collectable.create_metadata import breed_to_image_uri
from brownie import AdvancedCollectable


def main():
    set_token_uri()

def set_token_uri():
    advanced_collectable = AdvancedCollectable[-1]
    number_of_tokens = advanced_collectable.tokenCounter()
    print(f"{number_of_tokens} token(s) in this collection have been minted ...\n")
    for token_id in range(number_of_tokens):
        breed = get_breed(advanced_collectable.tokenIdToBreed(token_id))
        if not advanced_collectable.tokenURI(token_id).startswith('https://'):
            account = get_account()
            set_uri_tx = advanced_collectable.setTokenURI(token_id, breed_to_image_uri[breed], {'from': account})
            set_uri_tx.wait(1)
            print(f"NFT viewable at {opensea_url.format(advanced_collectable.address, token_id)}")