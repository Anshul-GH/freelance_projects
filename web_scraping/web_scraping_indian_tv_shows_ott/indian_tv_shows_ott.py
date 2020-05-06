from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import os
import pandas as pd

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_platform_data():
    # read the list of ott platforms and urls into a dataframe
    platforms = pd.read_csv(
        filepath_or_buffer=os.path.join(__location__, 'ott_platforms.csv'), 
        header=None)

    # assign headers to the dataframe    
    platforms.columns = ['Platform', 'Url', 'Tag', 'Class']

    return platforms


def data_extractor(url_info, tag_name, class_name):
    # get the response from the url provided
    response = get(url_info)
    
    # create a BeautifulSoub object to parse HTML response
    html_soup = BeautifulSoup(response.text, 'html.parser')

    file_obj = open(os.path.join(__location__, 'response.txt'), 'w+')
    file_obj.write(response.text)
    # print(tag_name, class_name)


    # # extract the required series list    
    
    # series_list = html_soup.find(tag_name, class_ = class_name).text
    # print(series_list)

    # return series_list


if __name__ == "__main__":
    # call the function to read the platform names and corresponding scraping information
    # collect the information in a dataframe
    source_df = read_platform_data()
    
    # collect the list of series for each platform
    series_list = {}

    # for each platform extract the required data iteratively
    for idx in source_df.index:
        series_list[source_df['Platform'][idx]]=data_extractor(source_df['Url'][idx], source_df['Tag'][idx], source_df['Class'][idx])
        break

    print(series_list)
