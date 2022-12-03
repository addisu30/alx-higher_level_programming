#!/usr/bin/python3
"""Script takes in arguments, injection them, and display state
Takes four arguments:
    mysql username
    mysql password
    database name
    state name searched (safe from MySQL injection)
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    param = (argv[4], )
    c.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY states.id ASC", param)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
