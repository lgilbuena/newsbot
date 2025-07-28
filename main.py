import requests
import json
from datetime import date, timedelta
from dotenv import load_dotenv
import os
import worker

load_dotenv()
newskey = os.getenv("NEWS_API_KEY")

yesterday = str(date.today()-timedelta(1))

def get_news():
    rval = ""
    queries = worker.get_data(0)
    for query in queries:
        news = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={yesterday}&sortBy=publishedAt&apiKey={newskey}&language=en")
        news_dict = json.dumps(news.json()['articles'][:2],indent=2,ensure_ascii=True)
        for x in range(5):
            title = news.json()['articles'][x]['title']
            url = news.json()['articles'][x]['url']
            rval += f"{title}: {url}\n"
    return rval