import os, requests
from pathlib import Path

pinata_base_url = 'https://api.pinata.cloud'
pin_endpoint = '/pinning/pinFileToIPFS'
filepath = './img/pug.png'
filename = filepath.split('/')[-1]
headers = {'pinata_api_key': os.getenv('PINATA_KEY'), 'pinata_secret_api_key': os.getenv('PINATA_SECRET'),}

def main():
    with Path(filepath).open('rb') as fp:
        image_binary = fp.read()
        response = requests.post(pinata_base_url + pin_endpoint, files={'file': (filename, image_binary)}, headers=headers)
        print(response.json())