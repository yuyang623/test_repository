#!/usr/bin/python
# coding: utf8
import datetime
import numpy
import jsm
import talib
import matplotlib.pyplot as plt

q = jsm.Quotes()
data = q.get_historical_prices("1942", jsm.WEEKLY, start_date = datetime.datetime(2012,1,1), end_date = datetime.datetime(2013,1,1))
close = numpy.array([float(d.close) for d in data])

macd, macdsig, macdhis = talib.MACD(close)
rsi = talib.RSI(close)

ax = plt.subplot(311)
plt.plot(close)
ax.set_title("Raw data")
ax = plt.subplot(312)
plt.plot(macd)
plt.plot(macdsig)
ax.set_title("MACD")
ax = plt.subplot(313)
plt.plot(rsi)
ax.set_title("RSI")
plt.show()
