# coding: utf-8
import sqlite3

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)

cur = conn.cursor()


def get_object_or_404(table, query):
    try:
        cur.execute(f"""SELECT * FROM `{table}` WHERE {query}""")
        return cur.fetchall()[0]
    except Exception as err:
        raise Exception(err)


def all(table):
    cur.execute(f"""SELECT * FROM {table}""")

    return cur.fetchall()


def filter(table, query):
    print('query', f"""SELECT * FROM `{table}` WHERE {query}""")
    cur.execute(f"""SELECT * FROM `{table}` WHERE {query}""")
    return cur.fetchall()


def insert(table, data, cols=None):
    vals = '('

    for x in range(1, len(data)+1):
        print(x , len(data))
        s = '?)' if x == len(data) else '?, '
        vals += s

    print(f"INSERT INTO `{table}`{cols} VALUES {vals}")

    if cols:
        cur.execute(f"""INSERT INTO `{table}`{cols} VALUES {vals} """, data)
    else:
        cur.execute(f"""INSERT INTO `{table}` VALUES  {vals}""", data)
    conn.commit()


def update(table, list, condition):
    for dict in list:
        for k,v in dict.items():
            print(f"""UPDATE `{table}` SET {k} = {v} WHERE {condition};""")
            cur.execute(f"""UPDATE `{table}` SET {k} = {v} WHERE {condition};""")

    conn.commit()