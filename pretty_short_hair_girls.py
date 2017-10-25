# coding : UTF-8

import requests
import random
from selenium import webdriver
import os
import re
import time
import socket
import http.client
from bs4 import BeautifulSoup


def get_content(url, data=None):
    browser = webdriver.Firefox()
    while True:
        try:
            browser.get(url)
            btn = browser.find_elements_by_class_name('QuestionMainAction')
            cnt = 10
            print('读取中...')
            while cnt != 0 and len(btn) != 0:
                cnt -= 1
                print('.')
                btn[0].click()
                time.sleep(3)
                btn = browser.find_elements_by_class_name('QuestionMainAction')
            time.sleep(10)
            pageSource = browser.page_source
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

    return pageSource


def store_pic(html_text):
    soup = BeautifulSoup(html_text, "html.parser")  # 构造美汤\
    girls = soup.find_all('div', {'class': 'List-item'})

    path = os.path.abspath('.')  # 构造路径
    path = os.path.join(path, 'pretty_short_hair_girls')
    #os.mkdir(path)  # 创建根文件夹
    num = 0
    for girl in girls:
        user = girl.find_all('a', {'class': 'UserLink-link'})
        if len(user) == 0:
            continue
        girl_a = user[1]
        girl_name = girl_a.get_text()  # 获取用户名
        girl_url = 'www.zhihu.com' + girl_a['href']  # 获取用户链接
        girl_path = path + '\\%s_' % num + girl_name  # 构造用户链接
        print('爬取小姐姐 %s 的照片中...\n' % girl_name)
        os.mkdir(girl_path)  # 创建用户文件夹
        with open(girl_path + '\\inf.txt', 'w') as f:
            f.write(girl_name + '\n' + girl_url)
        pics = girl.find_all('img')
        cnt = 0
        for pic in pics:
            pic_url = pic['src']
            if pic_url is None or re.match('[a-zA-z]+://[^\s]*', pic_url) is None:
                continue
            req = requests.get(pic_url)
            with open(girl_path + r'\%s.jpg' % cnt, 'wb') as fp:
                fp.write(req.content)
            cnt += 1
        num += 1

if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/40273344'
    html_text = get_content(url)
    store_pic(html_text)
