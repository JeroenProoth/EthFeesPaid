'''Took https://github.com/corpetty/py-etherscan-api as a learning experience.'''

from secrets import API_KEY, ADDRESS, ADDRESS_ALT
from calculator import Calculator

if __name__ == "__main__":
    calc = Calculator(ADDRESS, API_KEY)

    print(calc.calculate_total_eth_fees())
