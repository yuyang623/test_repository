#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb as mysql

argvs = sys.argv
argc = len(argvs)
if(argc != 3):
    print 'Usage: # python %s <mysql user> <mysql password>' % argvs[0]
    quit()

muser=argvs[1]
mpwd=argvs[2]

cn = mysql.connect(host="localhost", db="stock", user=muser, passwd=mpwd, charset="utf8")
cur = cn.cursor()

icnt = 0;
for line in sys.stdin:
    if(icnt==0):
        icnt += 1
        continue
    line = line.rstrip()
    stock_id, stock_name, stock_market, industory, dummy = line.split(',', 4)
    query = "insert into stock_master values (" + stock_id + ",'" + stock_name + "','" + stock_market + "','" + industory + "',0)"
    try:
        cur.execute(query)
    except:
        print "ERROR:" + line
        continue

cn.commit()

quit()
