
#-*- coding:utf-8 -*-
"""

第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？
请使用 Python 对密码加密。

"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import uuid
import hashlib


def encrypt_password(password):
    # 基于随机数
    salt = uuid.uuid4().hex
    # print salt
    result = password
    for i in range(10):
        result = hashlib.sha256(salt+ result).hexdigest()
    return salt + ':' + result

if __name__ == '__main__':
    # pw = input('Please input your password:')
    print "The password stored in the database is:" + encrypt_password('jiong')
