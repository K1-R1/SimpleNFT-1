from brownie import network, accounts, config, Contract, interface, VRFCoordinatorMock, LinkToken

opensea_url = 'https://testnets.opensea.io/assets/{}/{}'

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    elif id:
        return accounts.load(id)
    elif not config['networks'][network.show_active()]['local'] is False:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['dev_account_1']['private_key'])

contracts_to_mock = {'vrf_coordinator': VRFCoordinatorMock,
                     'link_token': LinkToken}

def get_contract(contract_name):
    contract_type = contracts_to_mock[contract_name]
    if config['networks'][network.show_active()]['local'] is True:
        deploy_mocks(contract_type)
        contract = contract_type[-1]
    
    else:
        contract_address = config['networks'][network.show_active()][contract_name]
        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)

    return contract

def deploy_mocks(contract_type):
    if contract_type == VRFCoordinatorMock:
        if len(contract_type) == 0:
            if len(LinkToken) == 0:
                LinkToken.deploy({'from': get_account()})
                print('LinkToken (mock) deployed')
            VRFCoordinatorMock.deploy(LinkToken[-1].address, {'from': get_account()})
            print('VRFCoordinatorMock deployed')

    elif contract_type == LinkToken:
        if len(contract_type) == 0:
            LinkToken.deploy({'from': get_account()})
            print('LinkToken (mock) deployed')

def fund_with_link(recipient_address, account=None, link_token=None, ammount=1*(10**17)):
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract('link_token')

    link_token_contract = interface.LinkTokenInterface(link_token.address)
    tx = link_token_contract.transfer(recipient_address, ammount, {'from': account}).wait(1)
    print('Contract funded with 0.1 LINK...\n')
    return tx
