#!/usr/bin/python3
""" All cities by state """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities, states\
                WHERE cities.state_id = states.id AND states.name=%s\
                ORDER BY cities.id", (argv[4],))
    table = cur.fetchall()

try:
    for row in range(len(table) - 1):
        print(table[row][0], end=', ')
    print(table[row + 1][0])
except Exception:
    print()

cur.close()
db.close()
