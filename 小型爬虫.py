import re
import requests
# coding=gbk

f = open(r"c:\1.csv", "w")

r = requests.get('http://www.bjrbj.gov.cn/LDJAPP/search/ddyy/ddyy_01_outline_new.jsp?sno=0&spage=0&epage=10&leibie=00&suoshu=00&sword')
while 1:
    data = r.text
    # 利用正则查找所有连接
    link_list =re.findall(r"(?<=href=\").+?(?=\">下一页)" ,data)
    print(r'http://www.bjrbj.gov.cn/LDJAPP/search/ddyy/' + link_list[0])
    r = requests.get(r'http://www.bjrbj.gov.cn/LDJAPP/search/ddyy/' + link_list[0])
    link_list = re.findall(r"(?:<td bgcolor.+>[^<]).+?(?=<)", data)
    iCount = 0
    for url in link_list:
        iPos = url.rfind('>') + 1
        content = url[iPos:len(url)]
        print(content)
        f.write(content)
        f.write(",")
        iCount = iCount + 1
        if(iCount >= 5):
            iCount = 0
            f.write("\r\n")
    break;
f.close()
print(r"over")
