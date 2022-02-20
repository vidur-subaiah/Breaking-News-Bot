import sys
import requests
import json
from datetime import date

print("Welcome to Command Line News!\n")

choice = input("Please make a choice: [1] Top headlines [2] Search ")

if choice == "1":
    http = "https://newsapi.org/v2/top-headlines?country=us&q=&pageSize=10&apiKey="
    api_key = "enter_your_api_key_here"
    http = http + api_key
    category = input("""Select which category you would like to see headlines for:
                        [1] business
                        [2] entertainment 
                        [3] general
                        [4] health 
                        [5] science 
                        [6] sports 
                        [7] technology
                         """)
    if category == '1':
        http = http.replace("q=", "category=business")
    if category == '2':
        http = http.replace("q=", "category=entertainment")
    if category == '3':
        http = http.replace("q=", "category=general")
    if category == '4':
        http = http.replace("q=", "category=health")
    if category == '5':
        http = http.replace("q=", "category=science")
    if category == '6':
        http = http.replace("q=", "category=sports")
    if category == '7':
        http = http.replace("q=", "category=technology")
    result = requests.get(http)
    json_object = result.json()
    for item in json_object['articles']:
        title = item['title']
        source = item['source']['name']
        description = item['description']
        date_published = item['publishedAt']
        date_published_year = int(date_published[:4])
        date_published_month = int(date_published[5:7])
        date_published_day = int(date_published[8:10])
        date_published_formatted = date(day = date_published_day, month = date_published_month, year = date_published_year).strftime('%B %d, %Y')
        if source == "":
            source = " "
        if description == "":
            description = " "
        print("* " + title + " - " + source + " (" + date_published_formatted + ")")
        print(description)
        print("\n\n")


    
if choice == "2":
    http = "https://newsapi.org/v2/everything?q=&sortBy=popularity&pageSize=10&apiKey="
    api_key = "enter_your_api_key_here"
    http = http + api_key
    search_term = input("Please enter your search term: ")
    print("\n")
    http = http.replace("q=", "q=" + search_term)
    result = requests.get(http)
    json_object = result.json()
    for item in json_object['articles']:
        title = item['title']
        source = item['source']['name']
        description = item['description']
        date_published = item['publishedAt']
        date_published_year = int(date_published[:4])
        date_published_month = int(date_published[5:7])
        date_published_day = int(date_published[8:10])
        date_published_formatted = date(day = date_published_day, month = date_published_month, year = date_published_year).strftime('%B %d, %Y')
        if source == "":
            source = " "
        if description == "":
            description = " "
        print("* " + title + " - " + source + " (" + date_published_formatted + ")")
        print(description)
        print("\n\n")
