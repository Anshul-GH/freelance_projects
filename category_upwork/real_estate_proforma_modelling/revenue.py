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
    rev_data = rev_data.drop('SF_SP', 1)
    aggr_data['Avg_SF'] = square_feet

    # avg rent/month (XLSX - SUMPRODUCT)
    # remove the $ and comma notation from rent data and convert to float
    rev_data['Rent/Month'] = [str(val).replace('$','') for val in rev_data['Rent/Month']]
    rev_data['Rent/Month'] = [float(str(val).replace(',','')) for val in rev_data['Rent/Month']]
    rev_data['RPM_SP'] = rev_data['Rent/Month'] * rev_data['# of Units'].astype(int)
    rent_per_month = rev_data['RPM_SP'].sum() / no_of_units
    rev_data = rev_data.drop('RPM_SP', 1)
    aggr_data['Total_RPM'] = rent_per_month

    # dollar per SF calculation (XLSX - IFERROR)
    rev_data['Dollar_PSF'] = [xlsx_iferror_div(x, y) for x, y in zip(rev_data['Rent/Month'], rev_data['SF'])]

    # export calculated revenue data
    # rev_file_name = r'target/rev_curr_inplace_rents_op.csv'
    rev_file_name = r'rev_curr_inplace_rents_op.csv'
    rev_data.to_csv(rev_file_name)

    # export aggregated revenue data
    # rev_file_name = r'target/rev_curr_inplace_rents_agg_op.csv'
    # rev_file_name = r'rev_curr_inplace_rents_agg_op.csv'
    # df = pd.DataFrame(aggr_data) 
    # print(df)
    # .to_csv(rev_file_name, index=[0])

    # print(rev_data)
    print(aggr_data)


def xlsx_iferror_div(a, b):
    return a / b if b else 0


def process_rev_data(rev_file_path):
    rev_data = pd.read_csv(rev_file_path, sep='\t')
    gen_rev_aggr(rev_data)


if __name__ == "__main__":
    # tab seperated file - hence named with .tsv extension
    rev_file_name = 'source/rev_curr_inplace_rents_inp.tsv'
    rev_file_path = get_file_path(rev_file_name)

    process_rev_data(rev_file_path)
