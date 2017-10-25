# coding : UTF-8

import requests
import random
import os
import time
import socket
import http.client
from bs4 import BeautifulSoup


def get_content(url, data=None):
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
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text


def store_pic(html_text):
    soup = BeautifulSoup(html_text)  # 构造美汤
    girls = soup.find_all('div', {'class': 'List-item'})

    path = os.path.abspath('.')  # 构造路径
    path = os.path.join(path, 'pretty_short_hair_girls')
    os.mkdir(path)  # 创建根文件夹

    for girl in girls:
        girl_a = girl.find_all('a', {'class': 'UserLink-link'})[1]
        girl_name = girl_a.get_text()  # 获取用户名
        girl_url = 'www.zhihu.com/people/' + girl_a['href']  # 获取用户链接
        girl_path = path + '\\' + girl_name  # 构造用户链接
        os.mkdir(girl_path)  # 创建用户文件夹
        with open(girl_path + '\\inf.txt', 'w') as f:
            f.write(girl_name + '\n' + girl_url)
        pics = girl.find_all('img')
        cnt = 0
        for pic in pics:
            pic_url = pic['src']
            with open(girl_path + r'\%s.jpg' % cnt, 'wb') as fp:
                req = requests.get(url, stream=True)
                fp.write(req.content)
            cnt += 1


if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/40273344'
    html_text = get_content(url)
    store_pic(html_text)
