# -*- coding: UTF-8 -*-

import re
# 正则表达式练习
pattern = re.compile(r"\d+")
m = pattern.match("sfflsjflk8979sdfsf",9,12)
print(m.group())

m=pattern.search("sfflsjflk8979sdfsf")
print(m.group())
pattern.findall()
