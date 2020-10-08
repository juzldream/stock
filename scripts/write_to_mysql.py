#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-08-11 21:12
# @Author  : 小白鞋 (1576768715@qq.com)
# @Link    : https://github.com/juzldream
# @Version : $Id$

"""
* 需要安装 mysql 模块
* pip install mysql-connector

"""

import mysql.connector


cnx = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='stock',
    user='root',
    password='123.com',
    charset='utf8',
    use_unicode=True,
    get_warnings=True)
# names = (('Geert', info, 30), ('Jan', info, 31), ('Michel', info, 32))
# stmt_insert = "INSERT INTO stock_partner VALUES ( '2020-03-31', '300300', '1', 'zhaohui', '1171229185', '45.891', '境内法人股' );"
cur.execute("SHOW TABLES")
cur.execute("select * from stock_partner;")
for x in cur:
  print(x)
# cnx.commit()


# cur.close()
# cnx.close()


