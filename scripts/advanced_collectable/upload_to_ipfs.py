from pathlib import Path
import requests

def upload_to_ipfs(filepath):
    with Path(filepath).open('rb') as fp:
        image_binary = fp.read()
        ipfs_url = ' http://127.0.0.1:5001'
        add_endpoint = '/api/v0/add'
        response = requests.post(ipfs_url + add_endpoint, files={'file': image_binary})
        ipfs_hash = response.json()['Hash']
        filename = filepath.split('/')[-1]
        image_uri = f"ipfs://ipfs/{ipfs_hash}?filename={filename}"
        print(f"Image URI: {image_uri}")
        return image_uri