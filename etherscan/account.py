from .client import Client

class Account(Client):
    '''Handles everything related to one address'''

    def __init__(self, address, api_key = ''):
        super().__init__(address, api_key = api_key)
        self.url_dict[self.MODULE] = 'account'

    def get_balance(self):
        '''Get the latest balance on address'''
        self.url_dict[self.ACTION] = 'balance'
        self.url_dict[self.TAG] = 'latest'

        self.build_url()
        req = self.connect()
        return req['result']

    def get_transaction_page(self):
        '''Get the latest transactions on address'''
