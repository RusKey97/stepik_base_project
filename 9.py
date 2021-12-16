
import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def delete_cat(idx):
    cursor.execute(f"""
                        DELETE FROM cats where id = {idx}
                   """)
    conn.commit()

def delete_cat_by_condition(where):
    cursor.execute(f"""
                        DELETE FROM cats where {where}
                   """)
    conn.commit()

def update_cat(idx, set_, where):
    cursor.execute(f"""
                        UPDATE cats set {set_}="{where}" where id = {idx}
                   """)
    conn.commit()


delete_cat(6)
delete_cat_by_condition('age > 20')
update_cat(26, 'age', 3)
