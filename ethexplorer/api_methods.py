from .client import Client

class ApiMethods(Client):
    """Handles ethexplorer API calls."""

    def __init__(self, api_key = 'freekey'):
        super().__init__(api_key = api_key)

    def get_last_block(self):
        """Get last scanned block.
        Response
            {
                lastBlock:     # last scanned block number,
            }
        """

        api_method = 'getLastBlock'

        req = self.connect(api_method)
        return req
    
    def get_token_info(self, token_address):
        """Get information about token for given token_address.
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
        """

        api_method = 'getTokenInfo'

        req = self.connect(api_method, address_or_txhash = token_address)
        return req

    def get_address_info(self, address, params = None):
        """ Get information about address given by address.
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

        """

        api_method = 'getAddressInfo'

        req = self.connect(api_method, address_or_txhash = address, params=params)
        return req

    def get_tx_info(self, tx_hash):
        """Get information of transaction for given tx_hash.
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
        """
        
        api_method = 'getTxInfo'

        req = self.connect(api_method, address_or_txhash = tx_hash)
        return req

    def get_token_history(self, token_address, params = None):
        """Show last (default 10) transfers for token at token_address. 
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
        """

        api_method = 'getTokenHistory'

        req = self.connect(api_method, address_or_txhash = token_address, params = params)
        return req

    def get_address_history(self, address, params = None):
        """Show last transfers for given address.
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
        """

        api_method = 'getAddressHistory'

        req = self.connect(api_method, address_or_txhash = address, params = params)
        return req

    def get_address_transactions(self, address, params = None):
        """Returns list of address transactions.
        Additional Params
            limit:          maximum number of operations [1 - 50, default = 10]
            timestamp:      starting offset for operations [optional, unix timestamp]
            showZeroValues: show transactions with zero ETH value, default = 0

        Response
            [
                {
                    timestamp:       # operation timestamp
                    from:            # source address (if two addresses involved),
                    to:              # destination address (if two addresses involved),
                    hash:            # transaction hash
                    value:           # ETH value (as is, not reduced to a floating point value),
                    input:           # input data
                    success:         # true if transactions was completed, false if failed
                },
            ]
        """

        api_method = 'getAddressTransactions'

        req = self.connect(api_method, address, params = params)
        return req

    def get_top(self, params = None):
        """Shows top (default 50) tokens by capitalization.
        Additional Params
            criteria: sort tokens by criteria [optional, trade/cap/count, trade - by trade volume, cap - by capitalization, count - by operations, default = trade]
            limit:    maximum number of tokens [optional, 1 - 50, default = 50]

        Response
            {
                tokens: [
                    {
                        # token data (same format as token info),
                        # token data by criteria and period (e.g. volume-7d-current - trade volume by latest 7 days, volume-7d-previous - trade volume by previous 7 days etc.)
                    },
                    ...
                ]
            }
        """

        api_method = 'getTop'

        req = self.connect(api_method, params = params)
        return req

    def get_top_tokens(self):
        """Shows top 50 of the most active tokens for the last 30 days period.
        Response
            {
                tokens: [
                    {
                        # token data (same format as token info)
                    },
                    ...
                ]
            }
        """

        api_method = 'getTopTokens'

        req = self.connect(api_method)
        return req

    def top_token_holders(self, token_address, params = None):
        """
        Additional Params
            limit:   maximum number of holders [1 - 1000 , default = 10].
            *for freekey maximum is 100

        Response
            {
                holders: [
                    {
                        address:   # address of holder,
                        balance:   # token balance,
                        share:     # share of holder in percent
                    },
                    ...
                ]
            }
        """

        api_method = 'topTokenHolders'

        req = self.connect(token_address, params = params)
        return req

    def get_grouped_token_history(self, token_address, params = None):
        """Show operations for token at given token_address.

        Additional Params
            period:  show operations of specified days number only [optional, 30 days if not set, max. is 90 days]

        Response
            {
                countTxs: [        # grouped token history
                    {
                        _id: {
                            year:  # transaction year
                            month: # transaction month
                            day:   # transaction day
                        },
                        ts:        # timestamp of the first transaction in group
                        cnt:       # number of transaction in group
                    },
                    ...
                ]
            }
        """

        api_method = 'getTokenHistoryGrouped'

        req = self.connect(token_address, params = params)
        return req

    def get_grouped_token_price_history(self, token_address, params = None):
        """Get price history for the token at given token_address.
        Additional Params
            period:  show price history of specified days number only [optional, 365 days if not set]       

        Response
            {   history
                {
                    countTxs: [        # grouped token history
                        {
                            _id: {
                                year:  # transaction year
                                month: # transaction month
                                day:   # transaction day
                            },
                            ts:        # timestamp of the first transaction in group
                            cnt:       # number of transaction in group
                        },
                        ...
                    ],
                    prices: [                 # grouped token price history
                        {
                            ts:               # timestamp of the token price
                            date:             # date of the token price in YYYY-MM-DD format
                            open:             # open token price
                            close:            # close token price
                            high:             # hign token price
                            low:              # low token price
                            volume:           # volume
                            volumeConverted:  # volume in USD
                            average:          # average token price
                        },
                        ...
                    ]
                }
            }
        """

        api_method = 'getTokenPriceHistoryGrouped'

        req = self.connect(token_address, params = params)
        return req

