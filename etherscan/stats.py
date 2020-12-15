from .client import Client

class Stats(Client):
    def __init__(self, address = '', api_key = ''):
        super().__init__(address, api_key = api_key)
        self.url_dict[self.MODULE] = 'stats'

    def get_ether_last_price(self):
        self.url_dict[self.ACTION] = 'ethprice'
        self.build_url()
        req = self.connect()
        return req['result']