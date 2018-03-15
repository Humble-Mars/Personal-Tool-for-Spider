import urllib.request
import urllib
import re
import time
import random
import socket
import threading
import os.path

baseurl = 'http://www.xicidaili.com/nn/'  # 西刺代理

# 建立随机header
def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return header

# 抓取代理IP
ip_detail = []
for page in range(1, 2):
    # url = 'http://ip84.com/dlgn/' + str(page)
    url = baseurl + str(page)
    headers = randHeader()
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
# time.ctime(os.stat("Unverified_Proxy_IP.txt"))
proxy_ip = open('Unverified_Proxy_IP.txt', 'w')  # 新建一个储存有效IP的文档
proxys = []
for i in range(0, len(ip_detail), 4):
    proxy_host = ip_detail[i] + ':' + ip_detail[i + 1]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)
    proxy_ip.write('%s\n' % str(proxy_temp))


proxy_ip.close()  # 关闭文件
print('爬取完成')
