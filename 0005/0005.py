# -*- coding: utf-8 -*-
import os
from PIL import Image


def get_filepaths(directory):
    # 路径这个还可以用glob的包进行查找
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

r_w, r_h = (1136, 640)

for infile in get_filepaths('image'):
    try:
        im = Image.open(infile)
        w, h = im.size
        if w > r_w or h > r_h:
            # 后一个参数为滤镜
            im.thumbnail((r_w, r_h), Image.ANTIALIAS)
            im.save(infile)
    except IOError:
        print "cannot create thumbnail for '%s'" % infile
