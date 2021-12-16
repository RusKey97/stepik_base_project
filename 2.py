
import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def insert_type(names):
    values = [(idx, value) for idx, value in enumerate(names, 1)]
    cursor.execute(f"""
                        INSERT INTO types VAlUES {', '.join(str(i) for i in values)}
                   """)
    conn.commit()


insert_type(['Абиссинская кошка', 'Австралийский мист', 'Американская жесткошёрстная'])