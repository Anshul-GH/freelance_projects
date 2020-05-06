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

x_axis = source_data[source_data['State/UnionTerritory'] == 'Kerala']['Date']
y_axis = source_data[source_data['State/UnionTerritory'] == 'Kerala']['Confirmed']

sea.barplot(x_axis, y_axis)
plt.show()

# print(source_data[source_data['State/UnionTerritory'] == 'Kerala']['Date'])
# # print(source_data['State/UnionTerritory'])