#!/usr/bin/python3
""" All cities by state """


import MySQLdb
from sys import argv
from model_state import Base, State

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                ORDER BY states.id")
    table = cur.fetchall()

    try:
        for row in table:
            print(f"{row[0]}: {row[1]}")
    except Exception:
        print()

    cur.close()
    db.close()
