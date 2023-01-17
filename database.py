import sqlite3
import time
from datetime import datetime
import requests
from config import token, chat_id

def check_database(item):
    event_id = item['event_id']
    connection = sqlite3.connect('../db/events.db')
    cursor = connection.cursor()
    cursor.execute(""" 
    SELECT event_id FROM events WHERE event_id =(?)""",
                   (event_id, ))
    result = cursor.fetchone()
    print(result)

    if not result:
        tg_sendler(item)
        #запишем в БД
        cursor.execute(""" 
        INSERT INTO events
        VALUES (
        NULL, :event_id, :title, :date, :url)
        """, item)

        connection.commit() #save data in our db
        print(f"Event {event_id} added into database")
    connection.close()

def format_text(item):
    text = f"""
            {item["title"]} \n
            {item["date"]} \n
            {item["url"]}
            """
    return text

def tg_sendler(item):
    text = format_text(item)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    response = requests.post(url=url, data = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'})
    print(response)

def main():
    item = {'title': 'Python вечеринка!!!', 'date': '01.01', 'event_id': 1, 'url': 'https://vk.com/anima_noir1'}
    tg_sendler(item)

if __name__ == '__main__':
    main()