import requests
import json

def google_search(keyword):
    api_key = 'your_api_key'
    cx = 'your_cx_value'
    url = f'https://www.googleapis.com/customsearch/v1?q={keyword}&key={api_key}&cx={cx}&num=10'
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        results = response.json()['items']
    return [result['link'] for result in results]

keywords = ['scraping', 'python']

data = {}
for keyword in keywords:
    data[keyword] = google_search(keyword)

with open('search_results.json', 'w') as f:
    json.dump(data, f)

