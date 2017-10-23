# coding : UTF-8

import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup


def get_content(url, data=None):
    global rep
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'vjuids=-3082f3824.15f3c91f50a.0.b12ad19c31598; userNewsPort0=1; f_city=%E6%B4%9B%E9%98%B3%7C101180901%7C; __auc=3306761a15f3c920d5eca36be31; vjlast=1508549719.1508655332.13; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1508549742,1508576834,1508655332,1508655341; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1508658890',
        'Pragma':'no-cache',
        'Host':'www.weather.com.cn',
        'Referer': 'http://www.weather.com.cn/weather1d/101180901.shtml',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'UTF-8'
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
    return rep.text


def get_date(html_text):
    final = []
    soup = BeautifulSoup(html_text, "html.parser")
    body = soup.body
    date = body.find('div', {'id': '7d'})
    ul = date.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        temp.append(inf[0].string, )
        if inf[1].find('span') is None:
            temperature_max = None
        else:
            temperature_max = inf[1].find('span').string.replace('℃', '')
        temperature_min = inf[1].find('i').string.replace('℃', '')
        temp.append(temperature_max)
        temp.append(temperature_min)
        final.append(temp)
    return final


def writre_date(date, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(date)


if __name__ == '__main__':
    url = "http://www.weather.com.cn/weather/101180901.shtml"
    html = get_content(url)
    result = get_date(html)
    writre_date(result, "weather.csv")
