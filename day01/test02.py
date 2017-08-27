#-*- coding: UTF-8 -*-
import urllib2
# 使用代理
proxyHandler=urllib2.ProxyHandler({"http":"163.125.210.7:9797"})
proxyOpener=urllib2.build_opener(proxyHandler)
urllib2.install_opener(proxyOpener)
request=urllib2.Request("http://www.baidu.com")
data=urllib2.urlopen(request).read()
print(data)