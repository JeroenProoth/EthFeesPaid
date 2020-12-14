# Took https://github.com/corpetty/py-etherscan-api as a learning experience.

from etherscan.account import Account
from secrets import API_KEY


if __name__ == "__main__":
	account = Account(API_KEY = API_KEY)
	account.show_api_key()