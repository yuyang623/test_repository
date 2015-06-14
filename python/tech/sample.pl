#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt
import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 3):
    print 'Usage: # python %s <stock_file_path> <start date (YYYY-MM-DD)>' % argvs[0]
    quit()

stock_data=argvs[1]
start_date=argvs[2]
stock=pd.read_csv(stock_data, parse_dates=True, index_col=0)

close=np.array(stock.ad_close.sort_index(ascending=True)[start_date:])

macd, macdsig, macdhis = ta.MACD(close)
time_series=close
rsi=ta.RSI(close, timeperiod=30)
sma30=ta.SMA(close, timeperiod=30)
sma75=ta.SMA(close, timeperiod=75)

#plt.figure()

#時系列、30日移動平均、75日移動平均
plt.subplot(3,1,1)
plt.plot(time_series)
plt.plot(sma30)
plt.plot(sma75)
plt.title("time series")

#MACD、シグナル
plt.subplot(3,1,2)
plt.plot(macd)
plt.plot(macdsig)
plt.title("MACD, MACDSIG")

#RSI
plt.subplot(3,1,3)
plt.plot(rsi)
plt.title("RSI")

#rsiグラフに30%、70%の線を引く
dummy=rsi
plt.plot(dummy*0+100)
plt.plot(dummy*0)
plt.plot(dummy*0+70)
plt.plot(dummy*0+30)

# タイトルの被りを防ぐ
plt.tight_layout()

plt.savefig("smp.png")
