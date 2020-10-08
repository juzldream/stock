#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-09 11:04
# @Author  : 小白鞋 (1576768715@qq.com)
# @Link    : https://github.com/juzldream
# @Version : v1.0

from urllib.request import urlopen, Request
import random


# 查看日K线图： http://image.sinajs.cn/newchart/daily/n/sh601006.gif
# 分时线的查询： http://image.sinajs.cn/newchart/min/n/sh000001.gif
# 日K线查询： http://image.sinajs.cn/newchart/daily/n/sh000001.gif
# 周K线查询： http://image.sinajs.cn/newchart/weekly/n/sh000001.gif
# 月K线查询： http://image.sinajs.cn/newchart/monthly/n/sh000001.gif
# https://github.com/streamlit/streamlit/

# 每周末复盘看 上证、深成、创业板 周K线
#https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/002828/displaytype/30.phtml 获取股东状况

base_url = 'http://hq.sinajs.cn/list'
sk_symbol = 'sz399006'
ua_list = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
]
ua = random.choice(ua_list)


req = Request('{}={}'.format(base_url, sk_symbol, headers={'User-agent': ua}))

response = urlopen(req, timeout=20)

wordbook = {
    1: '今 开',
    2: '昨 收',
    3: '当 前',
    4: '最 高',
    5: '最 低',
    6: '买 一',
    7: '卖 一',
    8: '成交量',
    9: '成交额',
    10: '买一成交量',
    11: '买 一',
    12: '买 二',
    13: '买二成交量',
    14: '买 三',
    15: '买三成交量',
    16: '买 四',
    17: '买四成交量',
    18: '买 五',
    19: '买五成交量',
    20: '卖一成交量',
    21: '卖 一',
    22: '卖二成交量',
    23: '卖 二',
    24: '卖三成交量',
    25: '卖 三',
    26: '卖四成交量',
    27: '卖 五',
    28: '卖五成交量',
    29: '日期'
}

idx = ['sh000001', 'sz399001', 'sz399006', 'sz399300', 'sh000300', 'sz399005']

with response as res:
    result = res.read().decode('utf-8', 'ignore')
    s = [i for i in result.split(',')]
    print(s)
    for i in idx:
        if i == sk_symbol:
            s = '{}：{}\n{}：{}\n{}：{}\n{}：{}\n{}：{}\n{}：{}\n{}：{}'.format(
                wordbook[1], round(float(s[1]), 2),
                wordbook[2], round(float(s[2]), 2),
                wordbook[3], round(float(s[3]), 2),
                wordbook[4], round(float(s[4]), 2),
                wordbook[5], round(float(s[5]), 2),
                wordbook[8] + '（亿）手', round(int(s[8])/10000000000, 2),
                wordbook[9] + '（亿）元', round(int(float(s[9]))/100000000, 2)
           )

print(s)