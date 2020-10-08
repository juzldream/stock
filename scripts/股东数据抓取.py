import requests
from lxml import etree
import random
import simplejson


# 贵州茅台 600519 爱尔眼科 300015
sk_symbol = '300300'
url = 'https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/' + sk_symbol +'/displaytype/10.phtml'

ua_list = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
]
ua = random.choice(ua_list)
session = requests.Session()
with session:
    response = session.get(url, headers={
        'User-agent': ua
    })
    content = response.text
    html = etree.HTML(content)
    #//table[@id='CirculateShareholderTable']//div[@align='center']
    #//table[@id='CirculateShareholderTable']//div[@align='center']/a/@name
    titles = html.xpath("//table[@id='CirculateShareholderTable']//div[@align='center']")
    result = []
    for title in titles:
        txt = title.xpath('.//text()')
        time = title.xpath('.//a/@name')
        result += time + txt

with open("..\\data\\" + sk_symbol + '.txt', 'w') as f:
    f.write(simplejson.dumps(result))
