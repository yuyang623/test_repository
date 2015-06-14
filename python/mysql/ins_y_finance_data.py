#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb as mysql

argvs = sys.argv
argc = len(argvs)
if(argc != 4):
    print 'Usage: # python %s <stock_id> <mysql user> <mysql password>' % argvs[0]
    quit()

mstock=argvs[1]
muser=argvs[2]
mpwd=argvs[3]

cn = mysql.connect(host="localhost", db="stock", user=muser, passwd=mpwd, charset="utf8")
cur = cn.cursor()

icnt = 0;
for line in sys.stdin:
    if(icnt==0):
        icnt += 1
        continue
    line = line.rstrip()
    date, opening, high, low, close, volume, adj_close = line.split(',')
    query = "insert into daily_stock values ('" + date + "'," + mstock + "," + opening + "," + high + "," + low + "," + close + "," + volume + "," + adj_close + ")"
    try:
        cur.execute(query)
    except:
        continue

cn.commit()

quit()
