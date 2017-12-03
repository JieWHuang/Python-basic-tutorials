import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容(输入“q！”退出程序)：")
    if content == 'q!':
        break
    
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11682.400'

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1502593792633'
    data['sign'] = 'c97d4f8b1eb5f3fdae76c9cf2db2a5f6'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_ENTER'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
     
    target = json.loads(html)
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
    time.sleep(1)
