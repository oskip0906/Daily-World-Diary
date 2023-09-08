import requests
from bs4 import BeautifulSoup
from googlesearch import search

query = "world news"

search_params = {
    "query": query,
    "stop": 10,   
    "pause": 1,  
}

search_results = search(**search_params)

news_data = []

for result in search_results:

    try:
        response = requests.get(result)

        soup = BeautifulSoup(response.text, 'html.parser')

        print(f"URL: {result}")

    except Exception as e:
        print(f"Error scraping {result}: {str(e)}")