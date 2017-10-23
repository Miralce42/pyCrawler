# coding : UTF-8

import requests
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup


def get_connect(url, date=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
    }

    timeout = random.choice(range(80, 180))

    while True:
        try:
            req = requests.get(url, headers=header, timeout=timeout)
            req.encoding = 'UTF-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(5, 10)))
        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))
        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))
        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    print(url, '访问成功')
    return req


def get_url(html_text):
    urls = []
    count = int(input('请输出数目:'))
    soup = BeautifulSoup(html_text, "html.parser")
    div = soup.find('div', {'id': 'article_list'})
    span = div.find_all('span', {'class': 'link_title'})
    for sp in span[0:count]:
        a = sp.find('a')
        url = 'http://blog.csdn.net' + a['href']
        if url not in urls:
            print('成功添加博客地址：', url)
            urls.append(url)
    return urls


def visit_blog(urls):
    cnt = 0
    num = len(urls)
    while cnt <= num * 50:
        cnt += 1
        time.sleep(random.choice(range(5, 10)))
        url = urls[random.choice(range(num))]
        req = get_connect(url)
        req.close()


if __name__ == '__main__':
    url = 'http://blog.csdn.net/han_zhuang?viewmode=contents'
    html_text = get_connect(url).text
    urls = get_url(html_text)
    visit_blog(urls)