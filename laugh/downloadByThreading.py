#!/usr/bin/python
#coding:utf-8
import threading
import time,sys,os,re,json
from time import time
reload(sys)
sys.setdefaultencoding('utf-8')
count = 0

def getThing(store_path, config, count):
    rename = re.sub(r'[\\/:*?"<> ]', '#', config['name'])
    true_path = store_path + rename + config['path'][config['path'].rfind('.'):]
    command = "wget " + config['path'] + " -q -O " + true_path
    if not os.path.exists(true_path):
        #command = "touch " + true_path
        os.system(command)
    else:
        print true_path + " exists!"
    #print command
    #os.system(command)

def createThread(f, store_path):
    item = f.readline()
    if not item:
        return None;
    config = json.loads(item)
    t = threading.Thread(target = getThing, args=(store_path, config, count))
    global count
    count = count + 1
    if count % 10 == 0:
        print count
    return t

if __name__ == '__main__':
    paramsNum = len(sys.argv)
    if paramsNum != 4:
        print 'usage:'
        print sys.argv[0] + ' json_file thread_number store_path'
        sys.exit(0)

    json_file = sys.argv[1]
    thread_number = int(sys.argv[2])
    store_path = sys.argv[3]
    count = 0
    print "json_file : %s thread_number : %d store_path: %s" %(json_file, thread_number, store_path)
    startTime = time()
    dirname = os.path.dirname(store_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    f = open(json_file, "r")
    threads = []

    for i in range(thread_number):
        t = createThread(f, store_path)
        if t:
            threads.append(t)
            t.setDaemon(True)
            t.start()
    while threads != []:
        for t in threads:
            t.join(1)
            if not t.is_alive():
                threads.remove(t)
                newt = createThread(f, store_path)
                if newt:
                    threads.append(newt)
                    newt.setDaemon(True)
                    newt.start()
    f.close()
    print ('Item- %d Use time- %f s)' %(count, (time() - startTime)))
