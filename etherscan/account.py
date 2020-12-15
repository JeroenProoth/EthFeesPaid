from .client import Client

class Account(Client):
    '''Handles everything related to one address'''

    def __init__(self, address, api_key = ''):
        super().__init__(address, api_key = api_key)
        self.url_dict[self.MODULE] = 'account'

    def get_balance(self) -> int:
        '''Get the latest balance on address.'''
        self.url_dict[self.ACTION] = 'balance'
        self.url_dict[self.TAG] = 'latest'

        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_page(self) -> list:
        '''Get the latest transactions on address'''
        self.url_dict[self.ACTION] = 'txlist'
        self.url_dict[self.SORT] = 'desc'

        self.build_url()
        req = self.connect()
        return req['result']

    def get_token_balance(self, contract_address):
        self.url_dict[self.ACTION] = 'tokenbalance'
        self.url_dict[self.CONTRACT_ADDRESS] = contract_address

        self.build_url()
        print(self.url)
        req = self.connect()
        return req['result']
