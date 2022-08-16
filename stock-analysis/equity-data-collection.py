import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def get_nse_listings():
    # Downloads the current listings from NSE official website
    listings_url = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
    pd.read_csv(listings_url, index_col='SYMBOL').to_csv('NSE-Listings.csv') # Saving a csv copy in OS
    return pd.read_csv(listings_url, index_col='SYMBOL')

def info_parser(stock_profile):
    # Takes stock profile link as input and returns a dictionary 
    soup = bs(requests.get(stock_profile).content, 'html.parser')
    name = soup.select(".Mb\(10px\)").text.strip()
    sector = soup.select("span.Fw\(600\):nth-child(2)").text.strip()
    industry = soup.select("span.Fw\(600\):nth-child(5)").text.strip()
    return {'name':name, 'sector':sector, 'industry':industry}

def get_stock_info(stock_tickers):
    # Collects the sector & industry data from profile page from yahoo finance
    profile_url = 'https://finance.yahoo.com/quote/'+stock_tickers+'NS/profile?'
    stock_info = list()
    
    for ticker in stock_tickers: # Itterating though all the tickers 
        stock_profile = profile_url + stock_tickers
        ticker_info = info_parser(stock_tickers)
        ticker_info['ticker']=ticker
        stock_info.append(ticker_info)
    return stock_info

def list_to_df(list):
    # Convert the list of dictionary to a pandas df
    pass