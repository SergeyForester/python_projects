# coding:utf-8
import os
import sqlite3


def init_tables():
    conn = sqlite3.connect('db.sqlite3', check_same_thread=False)

    cur = conn.cursor()

    # creating tables
    print(os.getcwd())

    cur.execute(""" CREATE TABLE IF NOT EXISTS `mainapp_room` (
                    id integer PRIMARY KEY ,
                    name  text (55) NOT NULL UNIQUE,
                    price integer NOT NULL,
                    adults integer not null,
                    kids integer not null,
                    infants integer not null,
                    extraPerson integer not null,
                    image1 blob not null,
                    image2 blob not null,
                    description text not null
                    );
    """)

    cur.execute(""" CREATE TABLE IF NOT EXISTS `mainapp_dateitem` (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    date_item DATE    NOT NULL,
                    is_busy   BOOL    NOT NULL,
                    room_id   INTEGER NOT NULL
                          REFERENCES timetable_room (id) DEFERRABLE INITIALLY DEFERRED
    );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS `mainapp_data` (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nameOfText  text (70)   NOT NULL,
                valueOfText text (5000) NOT NULL
    );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS `mainapp_dataimages` (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        image VARCHAR (100) NOT NULL,
        nameOfImage VARCHAR (50)  NOT NULL
    );
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS `mainapp_data` (
    id          INTEGER        NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    nameOfText  VARCHAR (70)   NOT NULL,
    valueOfText VARCHAR (5000) NOT NULL
);
""")
    del cur
    del conn


def fill_data(rooms, data, image_data):
    conn = sqlite3.connect('db.sqlite3', check_same_thread=False)

    cur = conn.cursor()

    # fill rooms
    for room in rooms:
        cur.execute("""INSERT INTO `mainapp_room`(name, price, adults, kids, infants, extraPerson, image1, image2, description)
        VALUES (?,?,?,?,?,?,?,?,?)""",
                    [room['name'], room['price'], room['adults'], room['kids'], room['infants'], room['extraPerson'],
                     room['image1'], room['image2'], room['description']])

        conn.commit()


    # fill data
    for el in data:
        kv = list(el.items())
        cur.execute("""INSERT INTO `mainapp_data`(nameOfText, valueOfText) VALUES (?,?)""", [kv[0][0], kv[0][1]])
        conn.commit()

    # fill image_data
    for el in image_data:
        kv = list(el.items())
        cur.execute("""INSERT INTO `mainapp_dataimages`(image, nameOfImage) VALUES (?,?)""", [kv[0][0], kv[0][1]])
        conn.commit()
