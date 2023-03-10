import sqlite3
import time
from bs4 import BeautifulSoup
import requests
from database import check_database

url='https://it-events.com'

def get_json(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_ = "event-list-item")  #  'event-list-item__title'   'event-list-item__info'
        return items

#допилить
def get_event(item):
        event = {}
        event['title'] = item.find(class_ = 'event-list-item__title').text
        event['date'] = item.find(class_ ='event-list-item__info').text
        event['pay'] = item.find(class_ ="event-list-item__type").text
        url2 = item.find(class_ = 'event-list-item__title').get('href')
        event['url'] = url + url2
        event['event_id'] = event['url'].split('/')[-1]
        return event



def get_events(items):
    for item in items:
        event = get_event(item)

        check_database(event)



def main():
    data = get_json(url)
    get_events(data)

if __name__ == '__main__':
        while True:
            main()
            time.sleep(20)
            break
