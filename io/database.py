import sqlite3
from fios.io import console


"""
..............................................................................................................
................................................ INIT ........................................................
..............................................................................................................
"""

THREAD_NAME = "DB"
connection = sqlite3.connect("")
cursor = connection.cursor()


# TODO: WHERE, SET function with kwargs
# TODO: Dyn init later...
# TODO: Dyn create table
def init(database_path):
    # TODO: not necessary: temp db
    global connection, cursor
    connection = sqlite3.connect(database_path, check_same_thread=False)
    # connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    # print("{cn} | {name}".format(cn=connection, name="init"))


# TODO: reset id
# TODO: set/where dict direct parameters
"""
..............................................................................................................
................................................ CRUD SUMMARY ................................................
..............................................................................................................
"""


def create(table, notify=True, **kwargs):
    """ Add instance to DB """
    # print("{cn} | {name}".format(cn=connection, name="create"))
    sql = "INSERT INTO {table}({keys}) VALUES({values})".format(
        table=table,
        keys=", ".join(list(kwargs.keys())),
        values=", ".join(["?"] * len(kwargs.keys())),
    )
    cursor.execute(sql, tuple(kwargs.values()))
    connection.commit()
    if notify:
        console.log("Created: %s" % str(kwargs), thread=THREAD_NAME)

    return cursor.lastrowid


def read(table, notify=True, **kwargs):
    """ Get instance from DB """
    # print("{cn} | {name}".format(cn=connection, name="read"))
    sql = "SELECT * FROM {table}{where}{order_by}".format(
        table=table,
        where="" if kwargs.get("where") is None else " WHERE %s" % kwargs["where"],
        order_by="" if kwargs.get("order_by") is None else " ORDER BY %s" % kwargs["order_by"],
    )
    # print(sql)
    # console.log(sql, thread=THREAD_NAME)
    cursor.execute(sql)
    if notify:
        console.log("Has read: %s" % str(kwargs), thread=THREAD_NAME)
    return cursor.fetchall()


def update(table, notify=True, **kwargs):
    """ Update instance in DB """
    # print("{cn} | {name}".format(cn=connection, name="update"))
    sql = "UPDATE {table} SET {set} WHERE {where}".format(
        table=table,
        set=kwargs["set"],
        where=kwargs["where"],
    )
    # console.log(sql, thread=THREAD_NAME)
    cursor.execute(sql)
    connection.commit()
    if notify:
        console.log("Updated: %s" % str(kwargs), thread=THREAD_NAME)


def delete(table, notify=True, **kwargs):
    """ Remove instance from DB """
    # print("{cn} | {name}".format(cn=connection, name="delete"))
    sql = "DELETE FROM {table} WHERE {where}".format(
        table=table,
        where=kwargs["where"],
    )
    # print(sql)
    cursor.execute(sql)
    connection.commit()
    if notify:
        console.log("Deleted: %s" % str(kwargs), thread=THREAD_NAME)


"""
..............................................................................................................
................................................ YTD SUMMARY .................................................
..............................................................................................................
"""


def exists(table, **kwargs):
    """ If exist certain instance """
    # print("{cn} | {name}".format(cn=connection, name="exists"))
    response = list(read(table, notify=False, **kwargs))
    return len(response) > 0


if __name__ == '__main__':
    # url = "https://www.youtube.com/playlist?list=PL3LQJkGQtzc4gsrFkm4MjWhTXhopsMgpv"
    # create(table="playlist", url=url, priority="3")
    # read(table="playlist", order_by="position", where="isChecked IS TRUE")
    # update(table="playlist", set="isChecked = 1", where="id IS 3")
    # delete(table="playlist", where="id == 7")

    # init(__database__)
    results = read("playlist")
    # results = read("video")
    for item in results:
        print(item)
