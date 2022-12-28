﻿import sqlite3
from bs4 import BeautifulSoup
import requests
from database import check_database

url='https://it-events.com/'

def get_item(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_ = "event-list-item")  #  'event-list-item__title'   'event-list-item__info'
        return items

#допилить
def get_event(item):
        event = {}
        event['event_id'] = item.get("id")
        event['title'] = item.find(class_ = 'event-list-item__title').text
        event['date'] = item.find(class_ ='event-list-item__info').text
        event['pay'] = item.find(class_ ="event-list-item__type").text
        event['url'] = item.find(class_ = 'event-list-item__title').get('href')
        print(event['title'])


def get_events(items):
    for item in items:
        event = get_event(item)

        #print(event['title'])
        check_database(event)




def main():
    data = get_json()
    get_events(data)

if __name__ == '__main__':
    main()