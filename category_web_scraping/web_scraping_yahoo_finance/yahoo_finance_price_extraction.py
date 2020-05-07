from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import os

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def generate_url(symbol):
    # base url
    base_url = "https://finance.yahoo.com/quote/"
    url = base_url + symbol        
    return url


def extract_data(url):
    # get the response from the url provided
    response = get(url)

    # create a BeautifulSoub object to parse HTML response
    html_soup = BeautifulSoup(response.text, 'html.parser')

    # current time as per the local timezone
    time = datetime.now()

    # extract the required price information
    price = html_soup.find('span', class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)").text
        
    return time, price


if __name__ == "__main__":
    # read the symbols from the text files
    source = open(os.path.join(__location__, 'symbols.txt'))
    symbols = source.readlines()

    # eliminate the newline characters if any
    symbols = [symbol.replace('\n', '') for symbol in symbols]

    # final list that would contain data to be written to file
    dataset = []

    for symbol in symbols:
        url = generate_url(symbol)
        time, price = extract_data(url)
        dataset.append(str(str(time) + "," + str(symbol) + "," + str(price)))

    # write the data to a text file
    out_file = open(os.path.join(__location__, 'output.txt'), 'w+')
    for data in dataset:
        out_file.write(data+'\n')
    out_file.close()