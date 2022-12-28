import sqlite3

def main():
    connection = sqlite3.connect('events.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT,
    title TEXT,
    date TEXT,
    url TEXT)""")

    connection.close()

if __name__ == '__main__':
    main()
