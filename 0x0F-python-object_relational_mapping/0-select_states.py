#!/usr/bin/python3
""" Get all states """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
