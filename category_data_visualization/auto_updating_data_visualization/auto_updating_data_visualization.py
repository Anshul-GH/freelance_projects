import pandas as pd
import matplotlib.pyplot as plt
from config import get_config
import os

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# read the secret key from config file
secret_key = get_config('SECRET', default='dummy')

# stocks will contain the list of stocks that is configurable
stocks = get_config('STOCKS', default=['JPM','BAC'])

# from the documentation of the IEX API, format of the api request:
# <url>?symbols=<comma_separated_stock_list>&types=<endpoint>&range=<time_period_in_years>&cache=<true_false>&token=<secret>

base_url = get_config('BASE_URL', default='https://cloud.iexapis.com/stable/stock/market/batch')

# concatenated string of stocks
stock_list = ''
for stock in stocks:
    stock_list += stock + ','
# skip the last comma
stock_list = stock_list[:-1]

# as per the documentation, endpoint for historical data
endpoint = 'chart'

# number of years in a string with y suffixed
years = '5y'

# cache flag
cache_flag=True

# final url
url = f'{base_url}?symbols={stock_list}&types={endpoint}&range={years}&cache={cache_flag}&token={secret_key}'


# hittng the url will send an api request automatically, storing the result in a dataframe
stock_json = pd.read_json(url)


# save the data from the dataframe in a csv file for reference
# stock_json.to_csv(os.path.join(__location__)+'/stock_data.csv')

# empty list to hold the price information for the stocks extracted from json
price_list = []

# for each stock, read the closing price and append to list
for stock in stocks:
    price_list.append(pd.DataFrame(stock_json[stock]['chart'])['close'])


# add an additional date column with blank data
price_list.append(pd.DataFrame(stock_json['JPM']['chart'])['date'])

# create a list of headers for the final dataframe - stocks + additional date column
stocks.append('Date')

# create the final version dataframe with columns and an index on 'Date'
master_data = pd.concat(price_list, axis=1) #headers=column_names, set_index='Date'
master_data.columns = stocks

# set and index on the 'Date' column
master_data.set_index('Date', inplace=True)

# print(master_data.head(5))