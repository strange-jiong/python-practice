import re
# 尽量使用原生字符串
with open("english.txt") as f:
    print len(re.findall(r"\w+", f.read()))
