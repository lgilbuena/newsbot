import requests
import json
from datetime import date, timedelta

query = "trump"
yesterday = str(date.today()-timedelta(1))

news = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={yesterday}&sortBy=publishedAt&apiKey={newsapikey}")
news_dict = json.dumps(news.json(),indent=2,ensure_ascii=True)
print(news.json()['articles'][:10])
# print(news_dict)