#!/usr/bin/python
#coding:utf-8

from bs4 import BeautifulSoup
import time,sys,os,re
import urllib2

url = "http://xiaohua.zol.com.cn"

def getUrl(url, encoding):
    response = urllib2.urlopen(url)
    content = response.read()
    response.close()

    return BeautifulSoup(content.decode(encoding))

def _checkPath(path):
    dirname = os.path.dirname(path.strip())
    if not os.path.exists(dirname):
        os.makedirs(dirname)
def saveImg(imgUrl, imgName):
    data=urllib2.urlopen(imgUrl).read()
    _checkPath(imgName)
    with open(imgName,'wb') as f:
        f.write(data)

if __name__ == '__main__':
    paramsNum = len(sys.argv)
    if paramsNum != 4:
        print 'usage:'
        print 'getPicture.py sub_url number store_path'
        sys.exit(0)

    count = 1
    sub_url = sys.argv[1]
    page = int(sys.argv[2])
    store_path = sys.argv[3]
    print sub_url
    print page
    print store_path
    content = getUrl(url +sub_url, 'gbk');

    while content:
        #windows文件/目录名不支持的特殊符号
        title = re.sub(r'[\\/:*?"<>]','#',content.find('h1',class_="article-title").text)
        src = content.find('div',class_="article-text").find('img')['src']

        if count % 10 == 0:
            print count
        #print title + src[src.rfind('.'):]
        #print src
        saveImg(src, store_path + str(count) + title + src[src.rfind('.'):])
        next_sub_url = content.find('a',class_="next")['href']
        #print next_sub_url
        content = getUrl(url +next_sub_url, 'gbk');
        #page = page - 1;
        count = count + 1
