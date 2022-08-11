# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# URL of the youtube channel
url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

# Intitilizing chromedriver
driver = webdriver.Chrome()
driver.get(url)

# tag in which all videos reside
video_tag = 'ytd-grid-video-renderer'

# Fetching all videos
videos = driver.find_elements(By.TAG_NAME,video_tag)
print(f'Found {len(videos)} videos.')

# Intitializing an empty list for data to be stored
video_list = []

# For loop to get data for each video on videos
for video in videos:
    title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    age = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    # Writing data in a dictionary
    video_itmes = {
        'title':title,
        'views':views,
        'posted':age
    }
    # Storing scraped data in a list before reintilizing the loop
    video_list.append(video_itmes)

# Creating a dataframe with 'video_list'
df = pd.DataFrame(video_list)
print(df.head())