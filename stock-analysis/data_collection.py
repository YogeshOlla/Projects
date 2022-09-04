import pandas as pd
import yfinance as yf
import time


def get_nse_listings():
    # Downloads the current listings from NSE official website
    listings_url = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
    return pd.read_csv(listings_url, index_col='SYMBOL')

def getStockHistory(tickers,sleep=0):
    for ticker in tickers:
        time.sleep(sleep)
        stock = ticker + ".NS"
        yf.Ticker(stock).history(period="11y",interval="1d").to_csv(f'Stock History/{stock}.csv')
        
def getStockInfo(tickers,sleep=0):
    
    stocks_info_list = list()
    
    for ticker in tickers:
        time.sleep(sleep)
        stock = ticker + ".NS"
        stock_info = yf.Ticker(stock).info
        stocks_info_list.append(stock_info)
        return stocks_info_list
    
print(yf.Ticker('3PLAND.NS').info)['sector']