# -*- coding: utf-8 -*-
import sqlite3
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from database import check_database


url = 'https://all-events.ru/events/calendar/theme-is-informatsionnye_tekhnologii/'
def get_json(url):
    response = requests.get(url)
    #print(response.text) текст выводит адекватно

    soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')

    items = soup.find_all('div', class_="event")
    return items


def get_event(item):
    event = {}
    link_ = item.find(class_="event-name").get("href")
    event['event_id'] = item.get("id")
    event['title'] = item.find(class_="event-name").text      #.strip()
    event['date'] = item.find(class_="event-date").text[:-3]   #.strip()
    event['url'] = "https://all-events.ru" + link_

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
