import sqlite3

conn = sqlite3.connect('My_cats.db')
cursor = conn.cursor()

def get_type_where(where):
    return list(cursor.execute(f"""
                                    SELECT id, type from types where {where}
                                """))

def insert_cat(name, type_, age, weight):
    type_id = get_type_where(f"type = '{type_}'")
    if not type_id:
        cursor.execute(f"""
                        INSERT INTO types (type) VALUES ('{type_}')
                   """)
        conn.commit()
        type_id = get_type_where(f"type = '{type_}'")[0][0]
    else:
        type_id = type_id[0][0]
    
    cursor.execute(f"""
                        INSERT INTO cats (name, type_id, age, weight) VALUES ('{name}', {type_id}, {age}, {weight})
                   """)
    conn.commit()


insert_cat('Ева', 'Мейн-ку́н', 5, 8)
insert_cat('Ниверин', 'Котоплепес', 1215, 9.5)
insert_cat('Борислав', 'Египетская мау', 35, 4)
