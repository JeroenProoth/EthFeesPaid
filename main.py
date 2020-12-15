'''Took https://github.com/corpetty/py-etherscan-api as a learning experience.'''

from secrets import API_KEY, ADDRESS
from etherscan.account import Account

if __name__ == "__main__":
    account = Account(ADDRESS, api_key = API_KEY)
    print(account.get_balance())
