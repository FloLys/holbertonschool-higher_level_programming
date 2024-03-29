#!/usr/bin/python3
""" Cities by states """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states\
                JOIN cities ON states.id = cities.state_id\
                ORDER BY cities.id")
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
