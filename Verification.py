# -*- coding:utf8 -*-

import Module
import urllib.request
import requests
import re
import time
import random
import socket
import threading
import os.path


url = "https://www.douban.com/note/660331076/"  # 打算爬取的网址


# 读取IP代理文件
inf = open("Unverified_IP.txt", 'r', encoding="utf-8")
lines = inf.readlines()

Unver_Proxys = []
for i in range(0, len(lines)):
    proxy_host = lines[i].rstrip()
    proxy_temp = {"http": proxy_host}
    Unver_Proxys.append(proxy_temp)



# 将可用ip写入Valid_IP.txt
a1 = re.compile("(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*?")
filename = a1.search(url).group()
ouf = open(str(filename) + "_Valid_IP.txt", "a+")

# 建立一个锁
lock = threading.Lock()


# 验证代理IP有效性的方法
def test(i):
    socket.setdefaulttimeout(5)  # 设置全局超时时间
    try:
        # proxy_support = urllib.request.ProxyHandler(Unver_Proxys[i])
        # opener = urllib.request.build_opener(proxy_support)
        # opener.addheaders = Module.randHeader()
        # urllib.request.install_opener(opener)
        # res = urllib.request.urlopen(url).read()
        res = requests.get('http://1212.ip138.com/ic.asp', headers=Module.randHeader(), proxies={"https": str(Unver_Proxys[i])}, timeout=5.0)
        lock.acquire()  # 获得锁
        print(Unver_Proxys[i], 'is OK')
        ouf.write('%s\n' % str(Unver_Proxys[i]))  # 写入该代理IP
        lock.release()  # 释放锁
    except Exception as e:
        lock.acquire()
        print(Unver_Proxys[i], e)
        lock.release()

# 多线程验证
threads = []
for i in range(len(Unver_Proxys)):
    thread = threading.Thread(target=test, args=[i])
    threads.append(thread)
    thread.start()
# 阻塞主进程，等待所有子线程结束
for thread in threads:
    thread.join()

inf.close()  # 关闭文件

