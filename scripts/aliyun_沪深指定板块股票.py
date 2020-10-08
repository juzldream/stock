from urllib.request import urlopen, Request
import sys
import ssl
import simplejson


# 获取指定板块股票列表
page = str(1)
host = 'https://ali-stock.showapi.com'
path = '/stock-in-block'
method = 'GET'
appcode = '191fe144054e4c4f85c79fc45977ba39'
querys = 'page=' + page + '&typeId=cyb'
bodys = {}
url = host + path + '?' + querys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}

request = Request(url, headers=headers)
print(1, request)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print(222, urlopen(request, context=ctx, timeout=15))
with urlopen(request, context=ctx, timeout=15) as res:
    result = simplejson.loads(res.read())
    print('总共：{} 页'.format(result['showapi_res_body']['pagebean']['allPages']))
    print('所属板块：{}'.format(result['showapi_res_body']['pagebean']['name']))
    print('总共股票个数：{}'.format(result['showapi_res_body']['pagebean']['allNum']))
    print('每一展示：{}个股票'.format(
        result['showapi_res_body']['pagebean']['maxResult']))
    s = result['showapi_res_body']['pagebean']
    with open(page + '.txt', 'w') as f:
        f.write(simplejson.dumps(s))
