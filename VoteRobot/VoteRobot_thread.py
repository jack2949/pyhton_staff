#encoding=utf-8

import sys
import time
import random
import string

import httplib
import urllib
import requests
import threading

Agents = [
		"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools",
		"Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
		"Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)",
		"Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN",
		"Mozilla/5.0 (Linux; Android 8.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044353 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools",
		"Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/NON_NETWORK Language/zh_CN Process/tools",
		"Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN",
		"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN",
		"Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI MT1-U06 Build/HuaweiMT1-U06) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_2.7.3_diordna_8021_027/IEWAUH_61_2.1.4_60U-1TM+IEWAUH/7300001a/91E050E40679F078E51FD06CD5BF0A43%7C544176010472968/1",
		"Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/4G Language/zh_CN Process/tools",
		"Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN",
		"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN",
		"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools",
		"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
	]

# 生成指定位数的随机字符串，字符为字母或数字
def getRandomString(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = ''
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString

# 对指定的作品（zpid）投一张票
def voteOnce(zpid):
    #conn = httplib.HTTPConnection("test.vattiwg.com")
    SessionId = getRandomString(24)
    UniqueID = getRandomString(8) + '-' + getRandomString(4) + '-' + getRandomString(4) +'-' + getRandomString(4) + '-' + getRandomString(12)
    #print SessionId
    #print UniqueID
    cookies_new = {
	'StrImage': 'http://cqengine.net:51202/UpLoadFile/Vote/Image/12Original.jpg',
	'strActivityCode': '003',
    'strWXShareDesc': '', 
	'strWXShareImge': 'http://cqengine.net:51202/UpLoadFile/Vote/Image/12300.jpg',
	'strWXShareTitle': '',
    'ASP.NET_SessionId': SessionId,
	'UniqueID':UniqueID
	}
#    cookies_new = "StrImage=http://cqengine.net:51202/UpLoadFile/Vote/Image/12Original.jpg; strActivityCode=003; strWXShareDesc=; strWXShareImge=http://cqengine.net:51202/UpLoadFile/Vote/Image/12300.jpg;strWXShareTitle=; ASP.NET_SessionId=%s; UniqueID=%s" % ("wmhnpnaxpnsnoh45gtiai4yc", "520bd39e-39e5-4963-81e4-b6913d5488bb")
    headers = {
			'Host':'test.vattiwg.com',
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With': 'XMLHttpRequest',
			'Accept-Language': 'zh-cn',
			'Accept-Encoding':'gzip, deflate',
			'Origin': 'http://test.vattiwg.com',
			'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
			'Connection':'keep-alive',
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'Referer':'http://test.vattiwg.com/?strActivityCode=003&from=groupmessage&isappinstalled=0',
			'User-Agent':'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN'
			}
    postParams = urllib.urlencode({'VoteID': zpid})
    #r = conn.request("POST", "/Vote/SaveUserVote", postParams, headers)
    payload = {"VoteID" : zpid}
    try:
        r = requests.post("http://test.vattiwg.com/Vote/SaveUserVote", data = payload, headers=headers,cookies=cookies_new)
        print r.content
    except:
	   print "some error."
    #conn.close()

	
# 投票控制器：指定作品（zpid）和投票张数（voteNum），并随机出投票间隔时间
def voteController(zpid, thread_number, voteNum):
	
    i = 0
    threads = []
    print '======== Start to vote zpid({0}), Total votes: {1}'.format(zpid, voteNum)
    for i in range(thread_number):
        t = threading.Thread(target = voteOnce, args=(zpid,))
        if t:
            threads.append(t)
            t.setDaemon(True)
            t.start()
    while threads != []:
        #print "111"
        for t in threads:
            t.join(5)
            #print t.is_alive()
            if not t.is_alive():
                threads.remove(t)
                newt = threading.Thread(target = voteOnce, args=(zpid,))
                i = i + 1
                print i
                if i >= voteNum:
                    #print 'bbb'
                    break;
                if newt:
                    #print 'aaa'
                    threads.append(newt)
                    newt.setDaemon(True)
                    newt.start()
    
        #randomSleepTime = random.randint(20, 50)
        #print '{0} tickets has been voted, the next ticket will be voted after {1} seconds.'.format(i+1, randomSleepTime)
        #time.sleep(randomSleepTime)
    print '======== Voting Ended!'


if __name__ == '__main__':
    paramsNum = len(sys.argv)
    if paramsNum != 4:
        print 'usage:'
        print sys.argv[0] + ' zpid thread_number count'
        sys.exit(0)

    zpid = sys.argv[1]
    thread_number = int(sys.argv[2])
    count = int(sys.argv[3])
    voteController(zpid, thread_number, count)
