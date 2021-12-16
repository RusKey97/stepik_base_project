import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def get_type(idx):
    res = list(cursor.execute(f"""
                                   SELECT type from types where id={idx}
                               """))
    try:
        return res[0][0]
    except IndexError:
        return

def get_type_where(where):
    for line in cursor.execute(f"""
                                    SELECT type from types where {where}
                                """):
        print(*line)


def get_all_types():
    for line in cursor.execute(f"""
                                    SELECT type from types
                                """):
        print(*line)


print(get_type(56))
get_type_where('id > 50')
get_type_where('type like "%н"')
get_all_types()
