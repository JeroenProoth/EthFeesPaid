'''Took https://github.com/corpetty/py-etherscan-api as a learning experience.'''

from secrets import API_KEY, ADDRESS, ADDRESS_ALT, ORN_CONTRACTADDRESS
from calculator import Calculator

from ethexplorer.client import Client

if __name__ == "__main__":
    calc = Calculator(ADDRESS, API_KEY)
    print(calc.api_methods.get_tx_info(ADDRESS))
    # print(calc.calculate_total_eth_fees())
    # print(calc.account.get_token_balance(ORN_CONTRACTADDRESS))
