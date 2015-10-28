# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class GachaWrap(Wrapper):
    gachaId = None #gachaId
    freeTimesToday = None #当天免费抽取次数
    lastRollTime = None #最后一次免费抽取的时间
    isPaid = None #是否已付费首抽
    def encode(self, pack):
        pack.addInt(self.gachaId)
        pack.addInt(self.freeTimesToday)
        pack.addLong(self.lastRollTime)
        pack.addBoolean(self.isPaid)
        pass

    def decode(self, pack):
        self.gachaId = pack.popInt()
        self.freeTimesToday = pack.popInt()
        self.lastRollTime = pack.popLong()
        self.isPaid = pack.popBoolean()
        pass