from .client import Client

class Stats(Client):
    def __init__(self, address = '', api_key = ''):
        super().__init__(address, api_key = api_key)
        self.set_query_param(module='stats')

    def get_ether_last_price(self):
        params = {
            'action': 'ethprice',
        }

        req = self.connect(params=params)
        return req['result']
