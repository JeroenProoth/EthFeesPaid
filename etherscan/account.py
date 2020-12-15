from .client import Client

class Account(Client):
    '''Handles everything related to one address'''

    def __init__(self, address, api_key = ''):
        super().__init__(address, api_key = api_key)
        self.set_query_param(module='account')

    def get_balance(self) -> int:
        '''Get the latest balance on address.'''
        self.set_query_param(action='balance')
        self.set_query_param(tag='latest')

        req = self.connect()
        return req['result']

    def get_transaction_page(self) -> list:
        '''Get the latest transactions on address'''
        self.set_query_param(action='txlist')
        self.set_query_param(sort='desc')

        req = self.connect()
        return req['result']

    def get_token_balance(self, contract_address):
        self.url_dict[self.ACTION] = 'tokenbalance'
        self.url_dict[self.CONTRACT_ADDRESS] = contract_address

        req = self.connect()
        return req['result']
