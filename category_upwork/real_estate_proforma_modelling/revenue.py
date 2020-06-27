import pandas as pd
import os
import re

def gen_data_aggr(df_rev_data):
    aggr_data = {}

    # number of units
    no_of_units = df_rev_data['# of Units'].astype(int).sum()
    # Total_Units
    aggr_data['Total_Units'] = no_of_units
    #################

    # avg square-feet (XLSX - SUMPRODUCT)
    df_rev_data['SF_SP'] = df_rev_data['SF'] * df_rev_data['# of Units'].astype(int)
    square_feet = df_rev_data['SF_SP'].astype(float).sum() / no_of_units
    df_rev_data = df_rev_data.drop('SF_SP', 1)
    # Avg_SF
    aggr_data['Avg_SF'] = square_feet
    #################

    # avg rent/month (XLSX - SUMPRODUCT)
    df_rev_data['RPM_SP'] = df_rev_data['Rent/Month'] * df_rev_data['# of Units'].astype(int)
    rent_per_month = df_rev_data['RPM_SP'].sum() / no_of_units
    df_rev_data = df_rev_data.drop('RPM_SP', 1)
    # Total_RPM
    aggr_data['Total_RPM'] = rent_per_month
    #################

    # dollar per SF calculation (XLSX - IFERROR)
    df_rev_data['Dollar_PSF'] = [xlsx_iferror_div(x, y) for x, y in zip(df_rev_data['Rent/Month'], df_rev_data['SF'])]
    # Total_RPM
    aggr_data['Agg_Dollar_PSF'] = format(float(aggr_data['Total_RPM'] / aggr_data['Avg_SF']), '.2f')
    #################
    
    df_aggr_data = pd.DataFrame(aggr_data.items())

    return df_rev_data, df_aggr_data



# XLSX - IFERROR implementation
def xlsx_iferror_div(a, b):
    return a / b if b else 0



if __name__ == "__main__":
    
    ########################
    # Current In-Place Rents
    rev_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/source/rev_curr_inplace_rents_inp.tsv"
    rev_data = pd.read_csv(rev_fpath, sep='\t')

    # calculations
    df_rev_data, df_aggr_data = gen_data_aggr(rev_data)

    # export calculated revenue data
    rev_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/target/rev_curr_inplace_rents_op.csv"
    df_rev_data.to_csv(rev_fpath)
    # export aggregated revenue data
    rev_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/target/rev_curr_inplace_rents_agg_op.csv"
    df_aggr_data.to_csv(rev_fpath)


    ########################
    # Post-Renovation Rents
    renov_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/source/rev_curr_inplace_rents_inp.tsv"
    renov_data = pd.read_csv(renov_fpath, sep='\t')
    renov_premium_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/source/renov_premium_inp.csv"
    renov_premium_data = pd.read_csv(renov_premium_fpath)
    renov_data['Rent/Month'] = renov_data['Rent/Month'].astype(float) + renov_premium_data['Premium'].astype(float)
    
    # calculations
    df_renov_data, df_aggr_renov_data = gen_data_aggr(renov_data)    

    # export calculated renov data
    renov_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/target/rev_post_renov_rents_op.csv"
    df_renov_data.to_csv(renov_fpath)
    # export aggregated renov data
    renov_fpath = r"/home/anshul/youtube/freelance_projects/category_upwork/real_estate_proforma_modelling/target/rev_post_renov_rents_agg_op.csv"
    df_aggr_renov_data.to_csv(renov_fpath)
