import pandas as pd
from etherscan.account import Account
from etherscan.stats import Stats

from ethexplorer.api_methods import ApiMethods

class Calculator():
    """Handles calculations regarding given account."""

    def __init__(self, address, api_key = ''):
        self.account = Account(address, api_key = api_key)
        self.stats = Stats(api_key = api_key)
        self.api_methods = ApiMethods()


    def calculate_total_eth_fees(self) -> tuple:
        """Calculates the total amount of fees paid in Eth"""
        tx_df = pd.DataFrame(self.account.get_transaction_page())

        """Calculate the total amount of fees paid by summing over all transactions.
        Fee (ETH) paid for a transation = gasPrice * gasUsed * 1e-18

        returns (fee(ETH) , fee(USD))
        """
        fee_in_eth = ((pd.to_numeric(tx_df['gasPrice']) * pd.to_numeric(tx_df['gasUsed']))
            * (1e-18)).sum()

        fee_in_usd = fee_in_eth * float(self.stats.get_ether_last_price()['ethusd'])
        
        return (fee_in_eth, fee_in_usd)


        
