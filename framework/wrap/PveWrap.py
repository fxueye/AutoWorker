# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PveWrap(Wrapper):
    pveId = None #pveId
    dailyCount = None #当天挑战次数
    lastTime = None #最后一次挑战时间
    appraisal = None #关卡过关得分,为0表示未通过此关卡
    resetCount = None #重置次数
    lastResetTime = None #最后一次重置时间
    def encode(self, pack):
        pack.addInt(self.pveId)
        pack.addInt(self.dailyCount)
        pack.addLong(self.lastTime)
        pack.addInt(self.appraisal)
        pack.addInt(self.resetCount)
        pack.addLong(self.lastResetTime)
        pass

    def decode(self, pack):
        self.pveId = pack.popInt()
        self.dailyCount = pack.popInt()
        self.lastTime = pack.popLong()
        self.appraisal = pack.popInt()
        self.resetCount = pack.popInt()
        self.lastResetTime = pack.popLong()
        pass