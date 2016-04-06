# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import uuid

uuids = []
for i in range(200):
    # uuid.uuid1()基于时间戳生成,uuid.uuid3() 基于名字
    uuids.append(uuid.uuid3(uuid.uuid1(), 'jiong'))
print uuids
