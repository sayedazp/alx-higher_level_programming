#!/usr/bin/python3
"""basic sql query using mysqldb"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name\
                 FROM `states` as `s` \
                INNER JOIN `cities` as `c` \
                   ON `c`.`state_id` = `s`.`id` \
                    WHERE `s`.`name` = %(var)s \
                ORDER BY `c`.`id`",
                {'var': sys.argv[4]})
    list = cur.fetchall()
    print(", ".join([ct[0] for ct in list]))
    cur.close()
    db.close()
