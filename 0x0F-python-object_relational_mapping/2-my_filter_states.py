#!/usr/bin/python3
""" Filter states by user input """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'\
                ORDER BY states.id".format(argv[4]))
    states = cur.fetchall()

    for row in states:
        if row[1] == argv[4]:
            print(row)

    cur.close()
    db.close()
