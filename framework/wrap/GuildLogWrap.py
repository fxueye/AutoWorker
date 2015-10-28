# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class GuildLogWrap(Wrapper):
    uid = None #UID
    type = None #日志类型
    time = None #创建时间
    logInfo = None #log信息
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.type)
        pack.addLong(self.time)
        pack.addString(self.logInfo)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.type = pack.popInt()
        self.time = pack.popLong()
        self.logInfo = pack.popString()
        pass