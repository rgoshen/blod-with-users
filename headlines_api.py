import os
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=os.environ.get("API_KEY"))


def get_headlines():
    '''Calls news api and returns list of articles'''
    top_headlines = newsapi.get_top_headlines(country='us')

    print(top_headlines['articles'][0]['source']['name'])

    return top_headlines['articles'][:5]
