from .client import Client

class ApiMethods(Client):
    '''Handles everything related to one address'''

    def __init__(self, api_key = 'freekey'):
        super().__init__(api_key = api_key)

    def get_address_info(self, address, params = None):
        ''' Response
            {
                address: # address,
                ETH: {   # ETH specific information
                    balance:  # ETH balance
                    totalIn:  # Total incoming ETH value (showETHTotals parameter should be set to get this value)
                    totalOut: # Total outgoing ETH value (showETHTotals parameter should be set to get this value)
                },
                contractInfo: {  # exists if specified address is a contract
                   creatorAddress:  # contract creator address,
                   transactionHash: # contract creation transaction hash,
                   timestamp:       # contract creation timestamp
                },
                tokenInfo:  # exists if specified address is a token contract address (same format as token info),
                tokens: [   # exists if specified address has any token balances
                    {
                        tokenInfo: # token data (same format as token info),
                        balance:   # token balance (as is, not reduced to a floating point value),
                        totalIn:   # total incoming token value
                        totalOut:  # total outgoing token value
                    },
                    ...
                ],
                countTxs:    # Total count of incoming and outgoing transactions (including creation one),
            }

            Additional Params:

            token: show balances for specified token address only
            showETHTotals: request total incoming and outgoing ETH values [true/false, default = false]

        '''
        api_method = 'getAddressInfo'

        req = self.connect(api_method, address, params=params)
        return req

    def get_tx_info(self, tx_hash):
        '''Response
            {
                operations: [
                    {
                        timestamp:       # operation timestamp
                        transactionHash: # transaction hash
                        tokenInfo:       # token data (same format as token info),
                        type:            # operation type (transfer, approve, issuance, mint, burn, etc),
                        address:         # operation target address (if one),
                        from:            # source address (if two addresses involved),
                        to:              # destination address (if two addresses involved),
                        value:           # operation value (as is, not reduced to a floating point value),
                    },
                    ...
                ]
            }
        '''
        
        api_method = 'getTxInfo'

        req = self.connect(api_method, tx_hash)
        return req
