import sqlite3
import webbrowser
from datetime import datetime

def setup_website_database():
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS websites(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        link TEXT NOT NULL,
        usage_count INTEGER DEFAULT 0,
        last_opened TEXT
    )
    """)


    conn.commit()
    conn.close()

def add_website(name,link):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO websites(name,link,last_opened)
    VALUES(?,?,?)
    """,(name.lower(),link,"NULL"))

    conn.commit()
    conn.close()

def website_opener_from_database(name):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,name,link,usage_count,last_opened
    FROM  websites
    """)
    website_database = cursor.fetchall()

    if len(website_database) ==0:
        print("no websites available")
    else:
        for website in website_database :
            if(website[1]==name.lower()):
                webbrowser.open(website[2])
                cursor.execute("""
                UPDATE websites
                SET usage_count = usage_count + 1,
                last_opened = ?
                WHERE name = ?
                """, (datetime.now(), name.lower()))
                conn.commit
                print(f"opening {name}")
            else:
                print("website not found")
                
        conn.close

def show_saved_websites():
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,name,link,usage_count,last_opened
    FROM  websites
    """)
    website_database = cursor.fetchall()

    if len(website_database) == 0:
        print("no data base available")
    else:
        for website in website_database:
            print(f"ID: {website[0]}")
            print(f"Name: {website[1]}")
            print("--------------------")
    conn.close

    