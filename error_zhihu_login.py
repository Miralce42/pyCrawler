# coding : UTF-8

import requests
from bs4 import BeautifulSoup


def login():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
    }
    session = requests.session()
    res = session.get('http://www.zhihu.com', headers=header).content
    _xsrf = BeautifulSoup(res, "html.parser").find('input', attrs={'name': '_xsrf'})['value']
    login_date = {
        '_xsrf': _xsrf,
        'password': 'hz19970816',
        'remember_me': 'true',
        'email': '1014653167@qq.com'
    }
    session.post('https://www.zhihu.com/#signin', data=login_date, headers=header)
    res = session.get('http://www.zhihu.com')
    print(res.text)


if __name__ == '__main__':
    login()
