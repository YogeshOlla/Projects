import yfinance as yf
import pandas as pd
import time

df = pd.read_csv("NSE-Listings.csv")
tickers = list(df['SYMBOL'])

stocks_info_list = list()
start_time = time.time()

for ticker in tickers:
    ticker_time_start=time.time()
    print(f'\nCollecting Data on {ticker}')
    stock = ticker + ".NS"
    stocks_info_list.append(yf.Ticker(stock).info)
    print(f'Time taken to collect info on {ticker}: {time.time() - ticker_time_start} seconds.')
    print(f'Total processing time {time.time() - start_time}')
    
stocks_info = pd.DataFrame(stocks_info_list)
stocks_info.set_index('symbol',inplace=True)
stocks_info.to_csv('NSE-Listings-Info.csv')