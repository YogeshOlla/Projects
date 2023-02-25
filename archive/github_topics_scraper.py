from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception ("Unable to fetch page " + url)
    return BeautifulSoup(response.text,'html.parser')

def get_topic_titles(doc):
    selector = 'f3 lh-condensed mb-0 mt-1 Link--primary'
    topic_tags = doc.find_all('p',{'class':selector})
    return [tag.text for tag in topic_tags]

def get_topic_descriptions(doc):
    selector = 'f5 color-fg-muted mb-0 mt-1'
    topic_descriptions = doc.find_all('p',{'class':selector})
    return [description.text.strip() for description in topic_descriptions]

def get_topic_urls(doc):
    selector = 'no-underline flex-1 d-flex flex-column'
    topic_urls = doc.find_all('a',{'class':selector})
    return ["https://github.com"+url['href'] for url in topic_urls]

def github_topics_scraper():  # sourcery skip: use-fstring-for-formatting
    
    # Intialising variable, lists and dictionaries
    i,all_titles,all_descriptions,all_urls,topics_data = 1,[],[],[],{}

    # Asking the user for input
    page_count = input("Enter then number of pages you want to scrape: ")
    page_count = int(page_count)

    # Initailising the loop
    while True:
        page_url = f'https://github.com/topics?page={str(i)}'

        # Fetching the page
        doc = get_page(page_url)

        # Getting output in form of lists
        titles = get_topic_titles(doc)

        if len(titles) < 1:
            print("No more data to scrape after page {}".format(i-1))
            break

        descriptions = get_topic_descriptions(doc)
        urls = get_topic_urls(doc)

        all_titles = all_titles + titles
        all_descriptions = all_descriptions + descriptions
        all_urls = all_urls + urls

        topics_data = {
            'Titles':all_titles,
            'Description':all_descriptions,
            'URL':all_urls}
        i = i + 1

    return topics_data,print("Task Completed")

def export_topics_csv():
    output = github_topics_scraper()
    df = pd.DataFrame(output[0])
    comment = output[1]
    return df.to_csv('topics.csv', index=None),comment

if __name__ == "__main__":
    export_topics_csv()
