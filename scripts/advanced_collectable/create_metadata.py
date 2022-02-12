from scripts.general_scripts import get_breed
from scripts.advanced_collectable.upload_to_ipfs import upload_to_ipfs
from brownie import AdvancedCollectable, network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import json, os


breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def create_metadata():
    advanced_collectable = AdvancedCollectable[-1]
    number_of_tokens = advanced_collectable.tokenCounter()
    print(f"{number_of_tokens} token(s) in this collection have been minted ...\n")
    for token_id in range(number_of_tokens):
        breed = get_breed(advanced_collectable.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists ...\n")
        else:
            metadata_template['name'] = breed
            metadata_template['description'] = f"A good {breed}"
            image_path = f"./img/{breed.lower().replace('_', '-')}.png"
            if os.getenv('IPFS_UPLOAD') == 'true':
                image_uri = upload_to_ipfs(image_path)
            else:
                image_uri = breed_to_image_uri[breed]
            metadata_template['image'] = image_uri
            with open(metadata_file_name, 'w') as file:
                json.dump(metadata_template, file)
            if os.getenv('IPFS_UPLOAD') == 'true':
                upload_to_ipfs(metadata_file_name)

def main():
    create_metadata()