import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cats (
                        id INTEGER PRIMARY KEY UNIQUE, 
                        name VARCHAR(20) NOT NULL,
                        type_id INTEGER NOT NULL,
                        age INTEGER NOT NULL,
                        weight DOUBLE,
                        FOREIGN KEY (type_id) REFERENCES types(id)
                        )
               """)
