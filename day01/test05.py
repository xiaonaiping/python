# -*- coding: UTF-8 -*-

import urllib
import urllib2
import re
import sys

#爬取吧主昵称
def loadUrl(url,startPage,endPage):
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"}
    pattern=re.compile(r'class="u-user-name" target="_blank">(.*?)</a>')
    fulldata=[]
    encoding=sys.getfilesystemencoding()
    for i in range(startPage,endPage+1):
        url=url+str(i)
        request=urllib2.Request(url,headers=header)
        data=urllib2.urlopen(request).read()
        m=re.findall(pattern,data)
        print(" ".join(m))


if __name__ == '__main__':
    startPage=int(raw_input("请输入你要爬取的开始页"))
    endPage=int(raw_input("请输入你要爬取的结束页"))
    url = 'http://www.budejie.com/'
    data=loadUrl(url,startPage,endPage)
    print(data)

