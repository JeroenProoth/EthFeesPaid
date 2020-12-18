import pandas as pd
from etherscan.account import Account
from etherscan.stats import Stats

from ethexplorer.api_methods import ApiMethods

class Calculator():
    """Handles calculations regarding given account."""

    def __init__(self, address, api_key = ''):
        self.account = Account(address, api_key = api_key)
        self.stats = Stats(api_key = api_key)

        self.address = address
        self.ethexplorer = ApiMethods()


    def calculate_total_eth_fees(self) -> tuple:
        """Calculates the total amount of fees paid in Eth"""
        tx_df = pd.DataFrame(self.account.get_transaction_page())

        '''Calculate the total amount of fees paid by summing over all transactions.
        Fee (ETH) paid for a transation = gasPrice * gasUsed * 1e-18

        returns (fee(ETH) , fee(USD))
        '''
        fee_in_eth = ((pd.to_numeric(tx_df['gasPrice']) * pd.to_numeric(tx_df['gasUsed']))
            * (1e-18)).sum()

        fee_in_usd = fee_in_eth * float(self.stats.get_ether_last_price()['ethusd'])
        
        return (fee_in_eth, fee_in_usd)

    def calculate_portfolio_value(self) -> dict:
        """Returns a dictionary of all tokens and their value."""
        tokens = {}

        address_info = self.ethexplorer.get_address_info(self.address)

        tokens['ETH'] = [address_info['ETH']['balance'], float(self.stats.get_ether_last_price()['ethusd'])]

        for tkn in address_info['tokens']:
            if 'name' in tkn['tokenInfo']:
                token_name = tkn['tokenInfo']['name']
                token_amount = float(tkn['balance']) / pow(10, float(tkn['tokenInfo']['decimals']))
                token_value = float(tkn['tokenInfo']['price']['rate'])

                tokens[token_name] = [token_amount, token_value]



        print(tokens)


        
