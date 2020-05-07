# analysing the source data retrieved from kaggle
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sea

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# reading covid_19_india.csv
source_file = os.path.join(__location__).replace('code','source') + "/covid_19_india.csv"
source_data = pd.read_csv(source_file)

# print(source_data.columns)
# print(source_data.describe())

# plt.plot(source_data[source_data['State/UnionTerritory'] == 'Kerala']['Date'], source_data[source_data['State/UnionTerritory'] == 'Kerala']['Confirmed'], label='Cases Trend')
# plt.legend()
# plt.show()

# cases that were active on a given day
active_cases = source_data[source_data['State/UnionTerritory'] == 'Kerala']['Confirmed'] - source_data[source_data['State/UnionTerritory'] == 'Kerala']['Cured']

# date - delete year info
raw_date = source_data[source_data['State/UnionTerritory'] == 'Kerala']['Date']
split_date = [dt.split('/') for dt in  raw_date]
req_date = [str(dt[0]+'-'+dt[1]) for dt in split_date]

x_axis = req_date
y_axis = active_cases

# barchart
sea.barplot(x_axis, y_axis)

# heatmap
sea.lineplot(x_axis, y_axis)

plt.show()

# print(source_data[source_data['State/UnionTerritory'] == 'Kerala']['Date'])
# # print(source_data['State/UnionTerritory'])