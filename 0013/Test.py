__author__ = 'jiong'
from urllib import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=v2ex').read()
print f
s = BeautifulSoup(f)

images = s.find_all('img')#, pic_type='0')
print images
count = 1


def download(src):
    global count
    file_name = str(count) + '.jpg'
    content = urlopen(src).read()
    with open(file_name, 'wb') as f:
        f.write(content)
    count += 1

for image in images:
    # print image
    download(image['src'])
    print count
