import pandas as pd
import matplotlib.pyplot as plt
from config import get_config
import os
import boto3

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

##########################################################################
# Step 1: Gather Your Data
##########################################################################

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



##########################################################################
# Step 2: Create the Chart
##########################################################################


# Subplot-1. Boxplots
plt.subplot(2,2,1)
# Data looks like this:
'''
              JPM    BAC      C    WFC      GS
Date                                          
2015-05-13  65.52  16.47  54.20  55.60  201.43
2015-05-14  66.05  16.52  54.60  56.04  202.62
2015-05-15  65.88  16.35  54.24  55.52  202.97
2015-05-18  66.42  16.51  54.67  55.75  204.66
2015-05-19  67.01  16.77  55.33  56.40  205.40
'''
# we need to transpose the data as we want dates as rows
plt.boxplot(master_data.transpose())

# labels to the plot
plt.title('Boxplot of Stock Prices (5Y Lookback)')
plt.xlabel('Stock Name', fontsize=10)
plt.ylabel('Stock Prices', fontsize=10)

# add column specific labels to x-axis using ticks
ticks = range(1, len(master_data.columns)+1) # [1, 2, 3, 4, 5] in our sample case
plt.xticks(ticks, master_data.columns, fontsize=10)



# Subplot-2. Scatterplots - WFC
plt.subplot(2,2,2)
# Can be used to show a density trend over a varying x
# In our case, lets plot it for just one stock 'WFC' against 'Date' which is our index

# x-axis: collect dates as a series object
dates = master_data.index.to_series()
# also convert it to datetime 
dates = [pd.to_datetime(val) for val in dates]

# y-axis: WFC stock prices
wfc_stock_prices = master_data['WFC']

# generate the plot
plt.scatter(dates, wfc_stock_prices)

# add title and axes to the chart
plt.title("Wells Fargo Stock Price (5Y Lookback)", fontsize=10)
plt.xlabel('Date', fontsize=10)
plt.ylabel('Stock Prices', fontsize=10)



# Subplot-3. Scatterplots - BAC
plt.subplot(2,2,3)
# Can be used to show a density trend over a varying x
# In our case, lets plot it for just one stock 'BAC' against 'Date' which is our index

# x-axis: collect dates as a series object
dates = master_data.index.to_series()
# also convert it to datetime 
dates = [pd.to_datetime(val) for val in dates]

# y-axis: BAC stock prices
bac_stock_prices = master_data['BAC']

# generate the plot
plt.scatter(dates, bac_stock_prices)

# add title and axes to the chart
plt.title("Bank of America Stock Price (5Y Lookback)", fontsize=10)
plt.xlabel('Date', fontsize=10)
plt.ylabel('Stock Prices', fontsize=10)


# plt.show()


# Subplot-4. Histogram
plt.subplot(2,2,4)
# simplest way to print
# also change the bin-count that changes how many slices the dataset gets divided into
plt.hist(master_data.transpose(), bins=50)

# add a legend
plt.legend(master_data.columns, fontsize=10)

# adding titles and axes
plt.title("Wells Fargo Stock Price (5Y Lookback)", fontsize=10)
plt.xlabel('Stock Prices', fontsize=10)
plt.ylabel('Observations', fontsize=10)

plt.tight_layout()
plt.show()


##########################################################################
# Step 3: Utilizing AWS
##########################################################################

# Setup the crdential file - add the secret key to the ./aws/credentials file

