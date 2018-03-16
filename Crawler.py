# -*- coding:utf8 -*-

import random
import re
import time
import urllib.request
import Module

# baseurl = 'http://www.xicidaili.com/nn/'  # 西刺代理
baseurl = 'http://m.66ip.cn/'


# 抓取代理IP
ip_detail = []
for page in range(1, 2):
    # url = 'http://ip84.com/dlgn/' + str(page)
    url = baseurl + str(page) + '.html'
    headers = Module.randHeader()
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print('爬取第' + str(page) + "页IP代理")
    pattern = re.compile('<td>(\d.*?)</td>')  # 截取<td>与</td>之间第一个数为数字的内容
    ip_page = re.findall(pattern, str(content))
    ip_detail.extend(ip_page)
    time.sleep(random.choice(range(1, 3)))

# 处理抓取内容
xiciproxy = open('xiciproxy.txt', 'w', encoding="utf-8")  # 创建一个西刺代理的详细文档参考
xiciproxy.write('代理IP地址' + '\t' + '端口' + '\t' + '速度' + '\t' + '验证时间' + '\n')
for i in range(0, len(ip_detail), 4):
    xiciproxy.write(ip_detail[i] + '\t' + ip_detail[i + 1] + '\t' + ip_detail[i + 2] + '\t' + ip_detail[i + 3] + '\n')



# 整理代理IP格式
# time.ctime(os.stat("Unverified_IP.txt"))
proxy_ip = open('Unverified_IP.txt', 'w')  # 新建一个储存有效IP的文档
proxys = []
for i in range(0, len(ip_detail), 4):
    proxy_host = ip_detail[i] + ':' + ip_detail[i + 1]
    proxy_temp = proxy_host
    proxy_ip.write('%s\n' % str(proxy_temp))


proxy_ip.close()  # 关闭文件
print('爬取完成')
