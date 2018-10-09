# CREATED FOR TEST 1
# 获取大学排名

import requests
from bs4 import BeautifulSoup
import bs4


def gethtmltext(url):
    ht = requests.get(url)
    ht.encoding = ht.apparent_encoding
    return ht.text


def mklist(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def oputlist(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    # 对于中文输出格式不对齐的改进
    print(tplt.format('排名', '学校', '总分', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = gethtmltext(url)
    mklist(uinfo, html)
    oputlist(uinfo, 20)


main()
