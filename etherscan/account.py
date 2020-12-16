from .client import Client

class Account(Client):
    '''Handles everything related to one address'''

    def __init__(self, address, api_key = ''):
        super().__init__(address, api_key = api_key)
        self.set_query_param(module='account')

    def get_balance(self) -> int:
        '''Get the latest balance on address.'''
        params = {
            'action': 'balance',
            'tag': 'latest',
        }

        req = self.connect(params=params)
        return req['result']

    def get_transaction_page(self) -> list:
        '''Get the latest transactions on address'''
        params = {
            'action': 'txlist',
            'sort': 'desc',
        }

        req = self.connect(params=params)
        return req['result']

    def get_token_balance(self, contract_address):
        params = {
            'action': 'tokenbalance',
            'contractaddress': contract_address,
        }

        req = self.connect(params=params)
        return req['result']
