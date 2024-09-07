# News app 7af864e81d0c48688cd88858f0869998
import requests
import json
query=input("what news you want: ")
url=(f"https://newsapi.org/v2/everything?q={query}&from=2024-06-26&sortBy=publishedAt&apiKey=7af864e81d0c48688cd88858f0869998")
r= requests.get(url)
news= json.loads(r.text)
for article in news["articles"]:
    print("\n")
    print(article["title"])
    print(article["description"])