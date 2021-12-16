import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def get_cat(idx):
    cat = list(cursor.execute(f"""
                        SELECT * FROM cats where id = {idx}
                   """))
    if cat:
        return cat[0]
    return None

def get_cat_where(where):
    for line in cursor.execute(f"""
                                   SELECT * FROM cats where {where}
                               """):
        print(line)


def get_all_cats():
    for line in cursor.execute(f"""
                                   SELECT * FROM cats
                               """):
        print(*line, sep='\t\t\t')


print(get_cat(15))

get_cat_where("age > 14")
get_cat_where("name like '%с'")

get_all_cats()

