import tushare as ts
import pandas as pd


#pip install tushare --upgrade
ts.set_token('cd5d236ef09d0a812056854916c21755d840c6044b75367bd617886e')

pro = ts.pro_api()

#获取沪股通成分
df = pro.hs_const(hs_type='SH')
print(df.values)


#获取深股通成分
# df = pro.hs_const(hs_type='SZ')

