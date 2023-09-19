#!/usr/bin/python3
"""basic sql query using mysqldb"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE name LIKE 'N%'")
    list = cur.fetchall()
    for row in list:
        print(row)
    cur.close()
    db.close()
