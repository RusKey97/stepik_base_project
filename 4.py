
import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def delete_type(idx):
    cursor.execute(f"""
                        DELETE FROM types where id = {idx}
                   """)
    conn.commit()

def update_type(idx, new_type):
    cursor.execute(f"""
                        UPDATE types set type="{new_type}" where id = {idx}
                   """)
    conn.commit()


delete_type(58)
update_type(2, 'Австралийский мистик')
