#!/usr/bin/python3
""" SQL injection safe filter states """


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
                ORDER BY states.id ASC", (argv[4],))
    states = cur.fetchall()

for row in states:
    print(row)
"""print("('%s')" % cur.fetchone())"""
cur.close()
db.close()
