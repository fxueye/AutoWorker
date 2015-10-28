# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class ActiveWrap(Wrapper):
    uid = None #UID
    time = None #时间
    value = None #活跃度值
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addLong(self.time)
        pack.addLong(self.value)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.time = pack.popLong()
        self.value = pack.popLong()
        pass