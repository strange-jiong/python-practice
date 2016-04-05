# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PIL import Image, ImageDraw, ImageFont


def add_num(img):
    draw = ImageDraw.Draw(img)
    # myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=50)
    myfont = ImageFont.truetype('msyh.ttf', size=50)
    fillcolor = "#ff0000"
    width, height = img.size
    print width, height
    draw.text((width - 160, 0), u"99", font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)
