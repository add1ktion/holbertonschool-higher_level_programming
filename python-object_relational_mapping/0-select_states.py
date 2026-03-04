#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC;")

    query_rows = cur.fetchall()

    for rows in query_rows:
        print(rows)

    cur.close()
    db.close()
