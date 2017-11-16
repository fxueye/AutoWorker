# -*- coding: utf-8 -*-
'''
Created on 2014年10月16日
@author: skw QQ:281431280
'''
import time
def timeToStr(birth_secds):
    tup_birth = time.localtime(birth_secds)
    format_birth = time.strftime("%Y-%m-%d %H:%M:%S",tup_birth)
    return format_birth
def strToTime(format_birth):
    tup_birth = time.strptime(format_birth, "%Y-%m-%d %H:%M:%S");
    birth_secds = time.mktime(tup_birth)
    return birth_secds
