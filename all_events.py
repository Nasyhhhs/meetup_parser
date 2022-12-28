# -*- coding: utf-8 -*-
import sqlite3
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests

def check_database(item):
    event_id = item['event_id']
    connection = sqlite3.connect('../db/events.db')
    cursor = connection.cursor()
    cursor.execute(""" 
    SELECT event_id FROM events WHERE event_id =(?)""",
                   (event_id, ))
    result = cursor.fetchone()
    #print(result)
    if not result:

        #TODO send_telegram(event)

        #запишем в БД
        cursor.execute(""" 
        INSERT INTO events
        VALUES (
        NULL, :event_id, :title, :date, :url)
        """, item)

        connection.commit() #save data in our db
        print(f"Event {event_id} added into database")
    connection.close()


def get_json():
    url = 'https://all-events.ru/events/calendar/theme-is-informatsionnye_tekhnologii/'
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

        #print(event['title'])
        check_database(event)


def main():
    data = get_json()
    get_events(data)


if __name__ == '__main__':
    main()
#