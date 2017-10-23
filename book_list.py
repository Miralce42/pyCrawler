# coding : UTF-8

import requests
import csv
import random
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
    # return html_text


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text)  # 创建Beautifu
    data = bs.find('div', {'class': 'clear borrowTop'})  # 找到id为7d的div
    tr = data.find_all('tr')  # 获取ul部分

    for book in tr[1:]:
        temp = []
        td = book.find_all('td')
        temp.append(td[0].string)
        book_name = td[1].a.get_text()
        temp.append(book_name)
        temp.append(td[4].string)
        final.append(temp)

    return final


def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == '__main__':
    url = 'http://lib.haust.edu.cn/haust/topreading/do.jsp'
    html = get_content(url)
    result = get_data(html)
    write_data(result, 'book_list.csv')
