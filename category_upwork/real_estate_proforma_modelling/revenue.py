import pandas as pd
import os
import re


# function to procure the absolute path of the file to be read
def get_file_path(filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    filepath = os.path.join(__location__, filename)
    return filepath

def gen_rev_aggr(rev_data):
    aggr_data = {}

    # number of units
    no_of_units = rev_data['# of Units'].astype(int).sum()
    aggr_data['Total_Units'] = no_of_units
    
    # avg square-feet (XLSX - SUMPRODUCT)
    # remove the comma notation from square-feet data and convert to float
    rev_data['SF'] = [float(str(val).replace(',','')) for val in rev_data['SF']]
    rev_data['SF_SP'] = rev_data['SF'] * rev_data['# of Units'].astype(int)
    square_feet = rev_data['SF_SP'].astype(float).sum() / no_of_units
    aggr_data['Avg_SF'] = square_feet

    # avg rent/month (XLSX - SUMPRODUCT)
    # remove the $ and comma notation from rent data and convert to float
    repl_str = {'$': '', ',': ''}
    rev_data['SF'] = [float(str(val).replace(',','')) for val in rev_data['SF']]
    rev_data['SF_SP'] = rev_data['SF'] * rev_data['# of Units'].astype(int)
    square_feet = rev_data['SF_SP'].astype(float).sum() / no_of_units
    aggr_data['Total_SF'] = square_feet
    
    

def process_rev_data(rev_file_path):
    rev_data = pd.read_csv(rev_file_path, sep='\t')
    gen_rev_aggr(rev_data)


if __name__ == "__main__":
    # tab seperated file - hence named with .tsv extension
    rev_file_name = 'source/rev_curr_inplace.tsv'
    rev_file_path = get_file_path(rev_file_name)

    process_rev_data(rev_file_path)
