# -*- coding: UTF-8 -*-

import urllib2
import cookielib
import urllib
#使用cookielib进行cookie的保存，进而通过cookie访问本站点其他页面
cookie = cookielib.CookieJar()
cookieProcessor = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookieProcessor)
opener.addheaders = [("User-Agent",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36)")]
urllib2.install_opener(opener)
url = "http://www.renren.com/PLogin.do"
data = {"email": "17621025691", "password": "wxc123"}
data = urllib.urlencode(data)
request = urllib2.Request(url, data=data)
response = urllib2.urlopen(request)
print(response.read())
