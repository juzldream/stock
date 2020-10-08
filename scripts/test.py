import requests


page = str(1)
host = 'https://ali-stock.showapi.com'
path = '/stock-in-block'
method = 'GET'
appcode = '191fe144054e4c4f85c79fc45977ba39'
querys = 'page=' + page + '&typeId=cyb'
bodys = {}
url = host + path + '?' + querys


ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
session = requests.Session()
with session:
    response = session.get(url, headers={
        'User-agent': ua
    })
    print(response)
    content = response.text
    print(content)