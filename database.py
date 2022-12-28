import sqlite3
import time
from datetime import datetime

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

