import requests
import json
from datetime import date, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
newskey = os.getenv("NEWS_API_KEY")

query = "trump"
yesterday = str(date.today()-timedelta(1))

news = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={yesterday}&sortBy=publishedAt&apiKey={newskey}")
news_dict = json.dumps(news.json(),indent=2,ensure_ascii=True)
print(news.json()['articles'][:10])
# print(news_dict)