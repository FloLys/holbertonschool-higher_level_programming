#!/usr/bin/python3
""" Filter states by user input """


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name='{argv[4]}'\
                ORDER BY states.id ASC")
    states = cur.fetchall()

for row in states:
    print(row)
cur.close()
db.close()
