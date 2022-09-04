import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time

def get_nse_listings():
    # Downloads the current listings from NSE official website
    listings_url = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
    return pd.read_csv(listings_url, index_col='SYMBOL')

def getData(ticker):
    # Collecting info about a stock using it's ticker
    print(f'\nCollecting data on {ticker}.')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}
    
    url = 'https://finance.yahoo.com/quote/'+str(ticker)+'.NS/profile?'
    print(f'\nCollecting data from {url}.')
    
    response = requests.get(url, headers=headers)
    #print(response.status_code)
    soup = bs(response.text, 'html.parser')
    print(f'\nParsing Data')
    
    try:name = soup.find('h3',{'class': 'Fz(m) Mb(10px)'}).text.strip()
    except:name = 'N/A'
    
    try:sector = soup.find('p',{'class': "D(ib) Va(t)"}).find_all('span',{'class': 'Fw(600)'})[0].text.strip()
    except:sector = 'N/A'
    
    try:industry = soup.find('p',{'class': "D(ib) Va(t)"}).find_all('span',{'class': 'Fw(600)'})[1].text.strip()
    except:industry = 'N/A'
    stock_info = {
        'ticker': ticker,
        'name': name,
        'sectors': sector,
        'industry': industry
    }
    return stock_info


def collect_stock_info():
    
    df = get_nse_listings()

    tickers = df.index.to_list()

    stock_info = list()

    for ticker in tickers:
        data = getData(ticker)
        print(f'\n{data}')
        stock_info.append(data)
        time.sleep(5)

    stock_info_df = pd.DataFrame(stock_info)
    
    stock_info_df.to_csv('NSE-Listings-Info.csv')
    
if __name__ == "__main__":
    collect_stock_info()