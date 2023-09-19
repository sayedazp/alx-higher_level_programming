#!/usr/bin/python3
"""basic sql query using mysqldb"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = %(name)s", {'name': sys.argv[4]})
    list = cur.fetchall()
    for row in list:
        print(row)
    print(cur._executed)
    cur.close()
    db.close()
