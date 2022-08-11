# Requests will help us with fetching the HTML page from a website.
import requests
# Next,we will use BeautifulSoup to process the HTML formated text file for data extraction.
from bs4 import BeautifulSoup
# After the data has been parsed and stored, we will use pandas to extract it into a '.csv' file
import pandas as pd

def get_page(url):
    
    # requests.get returns a response object containing the data from the web page.
    response = requests.get(url)
    
    # status_code is used to check if the request was successful and if it's not then we will raise an exception.
    if response.status_code != 200:
        
        # Exception will be raised if the status code is not 200
        raise Exception ("Unable to fetch page " + url)
    
    # At the end of function it will return a beautifulsoup doc
    return BeautifulSoup(response.text,'html.parser')

def get_page(url):
    
    # requests.get returns a response object containing the data from the web page.
    response = requests.get(url)
    
    # status_code is used to check if the request was successful and if it's not then we will raise an exception.
    if response.status_code != 200:
        
        # Exception will be raised if the status code is not 200
        raise Exception ("Unable to fetch page " + url)
    
    # At the end of function it will return a beautifulsoup doc
    return BeautifulSoup(response.text,'html.parser')

def get_restaurant_listings(doc):
    ''''''
    # Declaring a variable selector that contains class for name tag.
    selector = 'padding-10 radius-4 bg-white restaurant margin-b-10'
    
    # Returning the restaurant lising tags
    return  doc.find_all('div',class_=selector)


def get_restaurant_data(listing,info,base_url):
    
    # Parsing the information from lising
    restaurant_name = listing.find('h3',class_='grey res_name font-20 bold inline-block')
    restaurant_location = listing.find('h3',class_='margin-t-5 res_loc')
    cost_for_2 = listing.find('span',class_='padding-l-10 grey cost_for_two')
    cusisine = listing.find('div',class_='grey padding-l-10 res_cuisine')
    rating = listing.find('span',class_='critic')
    restaurant_img = listing.find('img',class_='radius-4 res_name lazy')
    restaurant_href = listing.find('a',class_='btn btn-primary height-40 block bold padding-10 font-14 apxor_click')

    # Appending the extracted info to dictionary
    info['restaurant_names'].append(restaurant_name.text.strip() if restaurant_name else 'N/A')
    info['restaurant_locations'].append(restaurant_location.text.strip() if restaurant_location else 'N/A')
    info['costs_for_2'].append(cost_for_2.text[:-7] if cost_for_2 else 'N/A')
    info['cusisines'].append(cusisine.text.strip() if cusisine else 'N/A')
    info['ratings'].append(rating.text.strip() if rating else 'N/A')
    info['restaurant_imgs'].append(restaurant_img['data-src'] if restaurant_img else 'N/A')
    info['restaurant_pages'].append(base_url+restaurant_href['href'] if restaurant_href else 'N/A')
    
    return info

def intialize_dictionary():
    
    return {'restaurant_names': [], 'restaurant_locations': [], 'costs_for_2': [], 'cusisines': [], 'ratings': [], 'restaurant_imgs': [], 'restaurant_pages': []}

def page_parser(x,max_page,website_page_base_url,info,base_url):
    
    while True: # Keep the loop running till a break condition is met
        
        # Adding if condition to stop the function if the requested number of pages have been scraped
        if x > int(max_page): 
            print(f"Process completed!, No more data to scrape after page {x - 1}")
            break

        page_url = website_page_base_url + str(x) # Creating page url
        print(f"Scraping Page {x}.")
        doc = get_page(page_url) # Calling function to get bs4 doc
        doc_listings = get_restaurant_listings(doc) # geting all the listing on the page

        if len(doc_listings) < 1: # Stop the loop if no data to scrape
            print(f"No more listings left to scrape, pages scraped successfully {x - 1}")
            break

        # Starting a for loop to get data from page
        for listing in doc_listings:           
            info = get_restaurant_data(listing,info,base_url) # Extracting data from all listing using a for loop

        print(f"{len(info['restaurant_names'])} listings scraped")
        print(f"Page {x} completed \n")

        # Increasing the page number
        x = x + 1

    return info

def website_scraper():
    
    # Assigning values to variables that will be used in the function
    x = 1 # x is the starting page number
    base_url = "https://www.eazydiner.com"
    website_page_base_url = f'{base_url}/restaurants?location=delhi-ncr&pax=2&total=281&page='


    # Intitalizing a new dictionary for stong the values
    info = intialize_dictionary()
    print("Initializing a new database \n")

    # Asking user for input
    max_page = input("Please enter the number of pages you want to scrape: ")

    # Calling previously defined function to get the data from the page
    info = page_parser(x,max_page,website_page_base_url,info,base_url)

    return info

def get_restaurant_csv():
    
    # Variable ourput calls the function get_restaurants() and stores it's value inside it.
    output = website_scraper()
    
    # Convering the dictionary outpt to a pandas dataframe
    df = pd.DataFrame(output)
    
    # Adding current date 
    
    # returning restaurants.csv file
    return df.to_csv('restaurants.csv', index=None),print("Task Completed")

if __name__ == "__main__":
    get_restaurant_csv()