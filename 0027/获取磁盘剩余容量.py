#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-25 09:26:36
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
path = None
if path is None:
    if os.name == 'nt':
        path = "C:\\"
    else:
        path = '/'
if os.name == 'nt':
    import win32file
    res_list = win32file.GetDiskFreeSpace(path)
    # numFreeClusters * sectorsPerCluster * bytesPerSector
    disk_free_space = res_list[0] * res_list[1] * res_list[2] / (1024 * 1024.0)
    print str(disk_free_space)+'MB'
    print '000%s'.format('a')
else:
    import statvfs
    vfs = os.statvfs(path)
    disk_free_space = vfs[statvfs.F_BAVAIL] * \
        vfs[statvfs.F_BSIZE] / (1024 * 1024.0)
