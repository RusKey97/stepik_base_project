import sqlite3
import re
from random import uniform, choice, randint

pattern = '"(.+)"'

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def get_types():
    return list(i[0] for i in cursor.execute(f"""
                                                  SELECT id from types
                                              """))


def add_more_cats(n):
    types_idx = get_types()
    names = get_names('names.txt')
    
    values = [(f"{choice(names)}", choice(types_idx), randint(1, 15), round(uniform(1.5, 12), 1)) for _ in range(n)]
    
    cursor.execute(f"""
                        INSERT INTO cats (name, type_id, age, weight) VAlUES {', '.join(str(i) for i in values)}
                   """)
    conn.commit()
    
def get_names(filename):
    res = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            finded = re.findall(pattern, line)
            if finded:
                res.append(finded[0])
    return res


add_more_cats(5000)

