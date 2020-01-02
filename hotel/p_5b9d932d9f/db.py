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