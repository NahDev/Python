import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_keywords(keywords, websites):
    data = []
    for website in websites:
        page = requests.get(website)
        soup = BeautifulSoup(page.content, 'html.parser')
        for keyword in keywords:
            matches = soup.find_all(string=lambda text: keyword in text)
            for match in matches:
                data.append({'Website': website, 'Title': soup.title.string, 'Keyword': keyword})
    return data

keywords = ['scraping', 'python']
websites = ['https://www.example1.com', 'https://www.example2.com']

data = scrape_keywords(keywords, websites)
df = pd.DataFrame(data)
df.to_csv('scraped_data.csv', index=False)

