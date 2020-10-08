#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-09 21:50
# @Author  : 小白鞋 (1576768715@qq.com)
# @Link    : https://github.com/juzldream
# @Version : $Id$

import baostock as bs
import pandas as pd


lg = bs.login()

print('login respond error_code:' + lg.error_code)
print('login respond  error_msg:' + lg.error_msg)

rs = bs.query_history_k_data_plus(
    "sz.300295",
    "date, code, open, high, low, close, preclose,\
    volume, amount, adjustflag, turn, tradestatus,\
    pctChg, peTTM, psTTM, pcfNcfTTM, pbMRQ, isST",
    start_date = '2012-03-15',
    end_date = '2020-07-26',
    frequency = "d",
    adjustflag = "2")

print('query_history_k_data_plus respond error_code:' + rs.error_code)
print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
result.to_csv("history_sz300295rk.csv", index=False)
print(result)
print(rs.get_row_data())
bs.logout()
