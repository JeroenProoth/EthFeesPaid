import requests

class Client():

    url = 'https://api.ethplorer.io/'

    def __init__(self, api_key = 'freekey'):
        # Allows persistent cookies.
        self.http = requests.session()
        self.set_query_param(apiKey=api_key)

    def set_query_param(self, **kwargs):
        """Sets the given query parameters."""
        self.http.params.update(kwargs)

    def connect(self, method, address_or_txid, params = None):
        try:
            request = self.http.get(self.url + method + '/' + address_or_txid, params=params)
        except requests.exceptions.ConnectionError:
            print('Connection Refused')
            return

        if request.status_code == 200:
            if request.text:
                data = request.json()
                error = data.get('error')
                if not error:
                    return data
        else:
            print('Bad Request')

