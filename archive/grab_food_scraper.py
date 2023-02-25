# Importing required libraries
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep

# Intitilizing chromedriver
driver = webdriver.Chrome()

def open_website():
    '''
    This function will open the website in chrome driver & wait 30 secfor the page to load, Then it will clear the cookies to so the data from last session is not used 
    '''
    website_url = 'https://food.grab.com/sg/en/'
    driver.set_page_load_timeout(30)
    driver.get(website_url)
    driver.delete_all_cookies()

def search_location():
    '''
    This function will enter location to the search by & then click the search button
    '''
    search_loc = '66 Bayshore Rd'
    search_box = driver.find_element(By.XPATH,'.//*[@id="location-input"]')
    search_box.send_keys(search_loc)
    
    search_button = driver.find_element(By.XPATH,'.//*[@id="page-content"]/div[2]/div/button')
    search_button.click()

def load_listings():
    '''
    This function will load the page till there are no more listings to load
    '''
    while True:
        try:
            sleep(10)
            load_more_button = driver.find_element(By.XPATH,'.//*[@id="page-content"]/div[4]/div/div/div[4]/div/button')
            load_more_button.click()
            return True

        except (TimeoutException, NoSuchElementException) as e:
            print('No more content to load')
            return False


def execute_code():
    '''
    This function will call all the previously deinfed functions & process the requests from start to end
    '''
    open_website()
    search_location()
    load_listings()

execute_code()
