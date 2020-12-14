from .client import Client

class Account(Client):
	def __init__(self, API_KEY = ''):
		Client.__init__(self, API_KEY = API_KEY)