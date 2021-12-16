import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

cursor.execute("""
                    CREATE TABLE IF NOT EXISTS types (
                        id INTEGER PRIMARY KEY UNIQUE, 
                        type VARCHAR(100) NOT NULL
                        )
               """)