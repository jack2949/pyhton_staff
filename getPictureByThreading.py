#!/usr/bin/python
#coding:utf-8
import threading
from bs4 import BeautifulSoup
import time,sys,os,re
import urllib2,threading

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
    response = urllib2.urlopen(imgUrl)
    data = response.read()
    response.close()

    _checkPath(imgName)
    with open(imgName,'wb') as f:
        f.write(data)

def getPicture(url_address, count, store_path):
    content = getUrl(url_address, 'gbk');
    title = re.sub(r'[\\/:*?"<>]','#',content.find('h1',class_="article-title").text)
    src = content.find('div',class_="article-text").find('img')['src']
    #print url_address + "  Done  " + str(count) + " path" + store_path + str(count) + title + src[src.rfind('.'):]
    saveImg(src, store_path + str(count) + title + src[src.rfind('.'):])

if __name__ == '__main__':
    paramsNum = len(sys.argv)
    if paramsNum != 4:
        print 'usage:'
        print sys.argv[0] + ' sub_url number store_path'
        sys.exit(0)

    count = 0
    cur_page = 0
    sub_url = sys.argv[1]
    page = int(sys.argv[2])
    store_path = sys.argv[3]
    print sub_url
    print page
    print store_path
    content = getUrl(url +sub_url, 'gbk');

    while content:
        #windows文件/目录名不支持的特殊符号
        startTime = time.time()
        items = content.find_all('li', class_="article-summary")
        threads = []
        for item in items:
            #print item.find(class_="article-title").a['href']
            t = threading.Thread(target=getPicture,args=(url + item.find(class_="article-title").a['href'],count,store_path))
            threads.append(t)
            count = count + 1
            if count % 10 == 0:
                print count
        for t in threads:
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join(15.0)

        cur_page = cur_page + 1
        if cur_page >= page:
            break

        next_sub_url = content.find('a',class_="page-next")['href']
        #print next_sub_url
        content = getUrl(url + next_sub_url, 'gbk');
        print ('cur_page- %4d ********** Use time- %f s)' %(cur_page, time.time() - startTime))
        #page = page - 1;
        #break
    print "all over %s" % time.ctime()
