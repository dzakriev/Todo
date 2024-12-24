import sqlite3

def init():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute(
            '''
            create table if not exists Items
            (id integer primary key,
            title text not null,
            description text,
            completed boolean);
            ''')
    connection.commit()
    connection.close()

def insert_item(title:str, description:str, completed:bool):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        Insert into Items(title, description, completed) VALUES
        ('{title}', '{description}', {completed});
        '''.format(title=title, description=description, completed=completed))
    connection.commit()
    connection.close()
    return(get_item(cursor.lastrowid))

def get_items():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row 
    cursor = connection.cursor()
    return cursor.execute('select * from "Items";').fetchall()

def get_item(id: int):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return cursor.execute('select * from "Items" where id = {id};'.format(id=id)).fetchone()

def update_item(id: int, data: dict):
    query = "UPDATE 'Items' SET " + ', '.join(
        "{}='{}'".format(k,v) for k,v in data.items()) + f" WHERE id={id}"
    print(query)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return cursor.rowcount > 0

def delete_item(id:int):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('delete from "Items" where id = {id};'.format(id=id))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0
