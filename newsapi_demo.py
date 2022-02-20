import sys
import requests
import json

# Technology headlines
url = "https://newsapi.org/v2/top-headlines?country=us&category=technology&pageSize=5&apiKey=XXX"

# Search headlines with a query (q)
#url = "https://newsapi.org/v2/everything?q=coronavirus&sortBy=publishedAt&pageSize=5&apiKey=XXX"

# Request URL Data
r = requests.get(url)

# Convert into JSON
json_data = r.json()
#print(json_data)

# Newapi query information
status = json_data["status"]
total_results = json_data["totalResults"]
articles = json_data["articles"]

# Caveman debugging
#print("Status:" + status)
#print("Total Results:", total_results)

#print(articles[0]["description"])

# Note the `pageSize` argument in the API can be used to limit the result that
# are returned
for article in articles:
    print("*",article['title'],article['publishedAt'])
    print("\t",article['description'])
    print("-----------------------------------------------\n")

