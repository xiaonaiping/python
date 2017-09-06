# -*- coding: UTF-8 -*-

# 利用bs4爬取知乎

from bs4 import BeautifulSoup
import requests
import time


def dealCaptcha(captchaData):
    with open("captchaPic.jpg", "wb") as f:
        f.write(captchaData)
        # text= raw_input("请输入验证码：")
        # return text


def zhihulogin():
    # 创建session对象，可以存储cookie
    sess = requests.Session()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"}
    html = sess.get("https://www.zhihu.com/#signin", headers=header).text
    bs = BeautifulSoup(html, "lxml")
    _xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")
    captchaUrl = "https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn" % (time.time() * 1000)
    captchaData = sess.get(captchaUrl, headers=header).content
    dealCaptcha(captchaData)
    # print(captchaText)
    captchaAll = (
        [24.2969, 29], [39.2969, 24], [88.2969, 28], [84.52, 19.17], [108.72, 28.64], [132.95, 24.44], [158.297, 34])
    outCaptcha = []
    str = raw_input("请输入你要选中的验证码的坐标，用逗号间隔：")
    captchaIndexList = str.split(",")
    for i in captchaIndexList:
        outCaptcha.append(captchaAll[int(i)])
    captcha = {
        "img_size": [200, 44],
        "input_points": outCaptcha
    }
    data = {
        "_xsrf": _xsrf,
        "email": "17085345763",
        "password": "wxc5418693",
        # "captcha": captcha
        "captcha_type": "cn"
    }
    print data
    url = "https://www.zhihu.com/login/email"
    res = sess.post(url, data=data, headers=header).text
    print(res)


if __name__ == '__main__':
    zhihulogin()
    # print(u"\u8bf7\u70b9\u51fb\u56fe\u4e2d\u5012\u7acb\u7684\u6587\u5b57")
