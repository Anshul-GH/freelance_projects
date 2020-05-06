# analysing the source data retrieved from kaggle
import pandas as pd
import os

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# reading covid_19_india.csv
source_file = os.path.join(__location__).replace('code','source') + "/covid_19_india.csv"
source_data = pd.read_csv(source_file)

print(source_data.columns)
print(source_data.describe())