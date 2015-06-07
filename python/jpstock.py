#!/usr/bin/python
# coding: utf-8

import sys
import datetime
import pandas as pd
import pandas.io.data as web

class JpStock:
    def base_url(self, code):
        #日経平均の場合
        if code == 998407:
            return ('http://info.finance.yahoo.co.jp/history/?code={0}.O&{1}&{2}&tm={3}&p={4}')
        else:
            return ('http://info.finance.yahoo.co.jp/history/?code={0}.T&{1}&{2}&tm={3}&p={4}')

    def get(self, code, start=None, end=None, interval='d'):
        base = self.base_url(code)
        start, end = web._sanitize_dates(start, end)
        start = 'sy={0}&sm={1}&sd={2}'.format(start.year, start.month, start.day)
        end = 'ey={0}&em={1}&ed={2}'.format(end.year, end.month, end.day)
        p = 1
        results = []

        print(start)
        print(end)
        if interval not in ['d', 'w', 'm', 'v']:
            raise ValueError(
                "Invalid interval: valid values are 'd', 'w', 'm' and 'v'")

        while True:
            url = base.format(code, start, end, interval, p)
            print("url=", url)
            tables = pd.read_html(url, header=0)
            if len(tables) < 2 or len(tables[1]) == 0:
                break
            results.append(tables[1])
            print(tables[1])
            # 複数ページをスクレープ
            p += 1
        #ignore_index=True 行番号を先頭から振りなおす
        result = pd.concat(results, ignore_index=True)
        #欠損データ削除
        result = result.dropna()
#        print("DEBUG columns")
        #日経平均の場合
        if code == 998407:
            result.columns = ['Date', 'Open', 'High', 'Low', 'Close']
        else:
            result.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
#        print("DEBUG to_datetime")
        #python2
        if interval == "m":
            result['Date'] = pd.to_datetime(result['Date'], format=u'%Y年%m月')
        else:
            result['Date'] = pd.to_datetime(result['Date'], format=u'%Y年%m月%d日')
#        print("DEBUG set_index")
        #'Date'をindexに設定したため、columからは消える
        result = result.set_index('Date')
#        print("DEBUG sort_index")
        result = result.sort_index()
#        print("DEBUG asfreq", result)
        return result.asfreq('B')


if __name__ == '__main__':
    argsmin = 2
    version = (2, 0)
#    version = (3, 0)
    if (sys.version_info <= (version)):
        print("This program requires python > %(version)s" % locals())
        quit()

    if ((len(sys.argv)-1) != argsmin):
        print("This program needs at least %(argsmin)s arguments" % locals())
        print("python2.7 jpstock.py <stock> <start date YYYY-MM-DD>")
        quit()

    try:
        stock = sys.argv[1]
        start = sys.argv[2]
 
        jpstock = JpStock()
#        print("DEBUG get")
        stock_tse = jpstock.get(int(stock), start=start)
#        print("DEBUG to_csv")
        stock_tse.to_csv("".join(["stock_", stock, ".csv"]))

    except ValueError:
        print("Value Error occured in", stock)

