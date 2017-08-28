# -*- coding: UTF-8 -*-
import urllib2
import urllib


# 贴吧爬取
def loadUlr(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"}
    urllib2.Request(url, headers=head)
    return urllib2.urlopen(url).read()


def writeUrl(data, filename):
    filename = filename.decode('utf-8').encode('gb2312')
    with open(filename, "w") as f:
        f.write(data)


def tiebaSpider(url, startPage, endPage):
    # 组装url
    for i in range(startPage, endPage + 1):
        fullUlr = url + "&pn=" + str((i - 1) * 50)
        data = loadUlr(fullUlr)
        fileName = "第" + str(i) + ".html"
        print "正在下载" + str(i) + "页"
        writeUrl(data, fileName)
        print "正在保存" + str(i) + "页"


if __name__ == '__main__':
    tbname = raw_input('请输入你要爬取的贴吧:')
    startPage = int(raw_input('请输入起始页:'))
    endPage = int(raw_input('请输入结束页:'))
    url = "https://tieba.baidu.com"
    kw = urllib.urlencode({"kw": tbname})
    fullUrl = url + "?" + kw
    tiebaSpider(fullUrl, startPage, endPage)
