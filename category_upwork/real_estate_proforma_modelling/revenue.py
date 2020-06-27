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

    aggr_data['Agg_Dollar_PSF'] = format(float(aggr_data['Total_RPM'] / aggr_data['Avg_SF']), '.2f')

    # export calculated revenue data
    # rev_file_name = r'target/rev_curr_inplace_rents_op.csv'
    rev_fname = r'target/rev_curr_inplace_rents_op.csv'
    rev_fpath = get_file_path(rev_fname)
    rev_data.to_csv(rev_fpath)

    # export aggregated revenue data
    rev_fname = r'target/rev_curr_inplace_rents_agg_op.csv'
    rev_fpath = get_file_path(rev_fname)
    df = pd.DataFrame(aggr_data.items())
    df.to_csv(rev_fpath)
    

def xlsx_iferror_div(a, b):
    return a / b if b else 0


def process_rev_data(rev_fpath):
    rev_data = pd.read_csv(rev_fpath, sep='\t')
    gen_rev_aggr(rev_data)


def process_post_renov_rent(renov_data_fpath):
    rev_data = pd.read_csv(renov_data_fpath)
    print(rev_data)
    # gen_rev_aggr(rev_data)



if __name__ == "__main__":

    # Table 1 - Current In-Place Rents #
    # tab seperated file - hence named with .tsv extension
    rev_fname = r'source/rev_curr_inplace_rents_inp.tsv'
    rev_fpath = get_file_path(rev_fname)
    # read the source data and generate the calculated fields
    process_rev_data(rev_fpath)


    # Table 2 - Post-Renovation Rents #
    renov_data_fname = r'rev_curr_inplace_rents_op.csv'
    renov_data_fpath = get_file_path(renov_data_fname)

    process_post_renov_rent(renov_data_fpath)

