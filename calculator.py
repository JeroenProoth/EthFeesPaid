import pandas as pd
from etherscan.account import Account

class Calculator():
    '''Handles calculations regarding given account.'''

    def __init__(self, address, api_key = ''):
        self.account = Account(address, api_key = api_key)


    def calculate_total_eth_fees(self) -> float:
        '''Calculates the total amount of fees paid in Eth'''
        tx_df = pd.DataFrame(self.account.get_transaction_page())

        '''Calculate the total amount of fees paid by summing over all transactions.
        Fee (ETH) paid for a transation = gasPrice * gasUsed * 1e-18
        '''
        fee_in_eth = ((pd.to_numeric(tx_df['gasPrice']) * pd.to_numeric(tx_df['gasUsed']))
            * (1e-18)).sum()

        return fee_in_eth
