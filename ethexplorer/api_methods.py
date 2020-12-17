from .client import Client

class ApiMethods(Client):
    '''Handles ethexplorer API calls.'''

    def __init__(self, api_key = 'freekey'):
        super().__init__(api_key = api_key)

    def get_last_block(self):
        '''
        Response
            {
                lastBlock:     # last scanned block number,
            }
        '''

        api_method = 'getLastBlock'

        req = self.connect(api_method)
        return req
    
    def get_token_info(self, token_address):
        '''
        Reponse
            {
                address:             # token address,
                totalSupply:         # total token supply,
                name:                # token name,
                symbol:              # token symbol,
                decimals:            # number of significant digits,
                price: {             # token price (false, if not available)
                    rate:            # current rate
                    currency:        # token price currency (USD)
                    diff:            # 24 hours rate difference (in percent)
                    diff7d:          # 7 days rate difference (in percent)
                    diff30d:         # 30 days rate difference (in percent)
                    marketCapUsd:    # market cap (USD)
                    availableSupply: # available supply
                    volume24h:       # 24 hours volume
                    ts:              # last rate update timestamp
                },
                owner:               # token owner address,
                countOps:            # total count of token operations
                totalIn:             # total amount of incoming tokens
                totalOut:            # total amount of outgoing tokens
                transfersCount:      # total number of token operations
                ethTransfersCount:   # total number of ethereum operations, optional
                holdersCount:        # total numnber of token holders
                issuancesCount:      # total count of token issuances
                image:               # token image url, optional
                description:         # token description, optional
                website:             # token website url, optional
                lastUpdated:         # last update timestamp
            }
        '''

        api_method = 'getTokenInfo'

        req = self.connect(api_method, address_or_txhash = token_address)
        return req

    def get_address_info(self, address, params = None):
        ''' 
        Additional Params:
            token: show balances for specified token address only
            showETHTotals: request total incoming and outgoing ETH values [true/false, default = false]

        Response
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

        '''

        api_method = 'getAddressInfo'

        req = self.connect(api_method, address_or_txhash = address, params=params)
        return req

    def get_tx_info(self, tx_hash):
        '''
        Response
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

        req = self.connect(api_method, address_or_txhash = tx_hash)
        return req

    def get_token_history(self, address, params = None):
        ''' 
        Additional Params:
            type:      show operations of specified type only ( default = transfer)
            limit:     maximum number of operations [1 - 1000, default = 10]
            timestamp: starting offset for operations [optional, unix timestamp]

        Response
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

        api_method = 'getTokenHistory'

        req = self.connect(api_method, address_or_txhash = address, params = params)
        return req


    def get_address_history(self, address, params = None):
        '''
        Additional Params
            token:     show only specified token address operations
            type:      show operations of specified type only
            limit:     maximum number of operations [1 - 10, default = 10]
            timestamp: starting offset for operations [optional, unix timestamp]

        Response
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

        api_method = 'getAddressHistory'

        req = self.connect(api_method, address_or_txhash = address, params = params)
        return req

    def get_address_transactions(self, address, params = None):
        pass
