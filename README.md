# SimpleNFT-1
<br/>
<p align="center">
<a href="https://chain.link" target="_blank">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/nft-mix/main/img/shiba-inu.png" width="225" alt="NFT Shiba Inu">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/nft-mix/main/img/pug.png" width="225" alt="NFT Pug">
<img src="https://raw.githubusercontent.com/PatrickAlphaC/nft-mix/main/img/st-bernard.png" width="225" alt="NFT St.Bernard">
</a>
</p>
<br/>

This is a repo to work with and use NFTs smart contracts in a python environment, using the Chainlink-mix as a starting point.

There are 2 types of NFTs here. 
1. `SimpleCollectibles.sol`
2. `AdvancedCollectibles.sol`

They each deploy unique dogs. The advanced version gives you a random breed (out of a Pug, Shiba Inu, and St. Bernard).

The advanced collection uses a [Chainlink VRF](https://docs.chain.link/docs/get-a-random-number) to deploy the random dog. 

The advanced collectables are deployed to testnet opensea

The contract is designed to be deployed and tested on multiple networks, currently those networks are:

- Ethereum mainnet
- Rinkeby test network

The contract has been unit tested locally, with intergration testing performed on Rinkeby.

## Made with
- solidity
- python
- brownie
- ipfs

### This repo is a project created during the course;
- smartcontractkit/full-blockchain-solidity-course-py
