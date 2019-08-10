# #-*- coding:utf-8 -*-
#
# import urllib2
import urllib
from urllib import request

import chardet
# import urlparse
import urllib.parse

def download(url, user_agent='wswp', proxy=None, num_retries=2):
    print('Downloading: ', url)
    headers = {'User-agent' : user_agent}
    request = urllib.request.Request(url, headers=headers)


    # opener = urllib.build_opener()

    opener = urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
        # opener.add_handler(urllib.ProxyHandler(proxy_params))
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
        charset = chardet.detect(html)['encoding']
        if charset == 'GB2312' or charset == 'gb2312':
            html = html.decode('GBK').encode('GB18030')
        else:
            html = html.decode(charset).encode('GB18030')
    except urllib.request.URLError as e:
        print('Download error', e.reason)
        html = None
        if num_retries > 0:
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # recursively retry 5xx HTTP errors
                    return download(url, user_agent, proxy, num_retries-1)
    return html



print(download('https://www.google.co.jp/', proxy='42.200.227.97:24733'))

#
# import urllib.request as request
# import requests
#
# proxies = {
#     'https': 'https://42.200.227.97:24733',
#     'http': 'http://42.200.227.97:24733'
# }
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }
#
# print('--------------使用urllib--------------')
# google_url = 'https://www.google.com'
# opener = request.build_opener(request.ProxyHandler(proxies))
# request.install_opener(opener)
#
# req = request.Request(google_url, headers=headers)
# response = request.urlopen(req)
#
# print(response.read().decode())
#
# print('--------------使用requests--------------')
# response = requests.get(google_url, proxies=proxies)
# print(response.text)