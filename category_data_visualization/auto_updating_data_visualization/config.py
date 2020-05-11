import os

config = {
    "SECRET": 'sk_51a174cb98214884901b5413c875daa2', # this is a dummy key, please use your own
    "PUBLIC": 'pk_f74e1f5b0e8d45c2bc66ba2c5a9621c0', # this is a dummy key, please use your own
    "STOCKS": ['JPM','BAC','C','WFC','GS'],
    "BASE_URL": 'https://cloud.iexapis.com/stable/stock/market/batch'
}

# method to expose the configuration variables
def get_config(param, default=None):
    cv = config.get(param)
    return cv 