#!/usr/bin/python3
""" Filter states """


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY states.id ASC")
    states = cur.fetchall()

for row in states:
    print(row)
cur.close()
db.close()
"""print("(%i, '%s')" % cur.fetchone())"""
