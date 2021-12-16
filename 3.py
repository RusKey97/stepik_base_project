import sqlite3
import re

pattern = '"(.+)"'

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def insert_type(names):
    values = [(idx, value) for idx, value in enumerate(names, 1)]
    cursor.execute(f"""
                        INSERT INTO types VAlUES {', '.join(str(i) for i in values)}
                   """)
    conn.commit()


def add_all_types(filename):
    res = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            finded = re.findall(pattern, line)
            if finded:
                res.append(finded[0])
    insert_type(res)

add_all_types('types.txt')
