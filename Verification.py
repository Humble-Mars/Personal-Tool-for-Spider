# -*- coding:utf8 -*-

import urllib.request
import requests
import socket
socket.setdefaulttimeout(3)

headers = {'User-Agent': 'Mozilla/5.0'}
inf = open("ip.txt")    # 这里打开刚才存ip的文件
lines = inf.readlines()
proxys = []
for i in range(0, len(lines)):
    proxy_host = "http://" + lines[i].rstrip()
    proxy_temp = {proxy_host}
    proxys.append(proxy_temp)


# 将可用ip写入valid_ip.txt
ouf = open("valid_ip.txt", "a+")

for proxy in proxys:
    try:
        res = requests.get('http://1212.ip138.com/ic.asp', proxies={"https": str(proxy)}, timeout=5.0)
        print(res.status_code)
        print(res.text)
        valid_ip = str(proxy)
        print(('valid_ip: ' + valid_ip))
        ouf.write(valid_ip)
    except Exception as e:
        print("Fail:" + str(proxy))
        print(e)
        print("\n")
        continue



