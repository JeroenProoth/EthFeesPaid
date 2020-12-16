''' Took https://github.com/corpetty/py-etherscan-api as a learning experience.'''

import requests

class Client():

    url = 'https://api.etherscan.io/api'

    def __init__(self, address, api_key = ''):
        # Allows persistent cookies.
        self.http = requests.session()
        self.set_query_param(address=address, apikey=api_key)

    def set_query_param(self, **kwargs):
        """Sets the given query parameters."""
        self.http.params.update(kwargs)

    def connect(self, params):
        try:
            request = self.http.get(self.url, params=params)
            print(request.url)
        except requests.exceptions.ConnectionError:
            print('Connection Refused')
            return

        if request.status_code == 200:
            if request.text:
                data = request.json()
                status = data.get('status')
                if status == '1':
                    return data
                else:
                    print('Empty Response')
        else:
            print('Bad Request')


    def show_api_key(self):
        print(self.http.params)
