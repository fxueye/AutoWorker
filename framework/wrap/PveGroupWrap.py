# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Pvewrap import Pvewrap# @UnresolvedImport
class PveGroupWrap(Wrapper):
    groupId = None #PveGroupId
    dailyCount = None #当天挑战次数
    lastTime = None #最后一次挑战时间
    pveWraps = []
    def encode(self, pack):
        pack.addInt(self.groupId)
        pack.addInt(self.dailyCount)
        pack.addLong(self.lastTime)
        pack.addShort(len(self.pveWraps))
        for v in self.pveWraps:
            pack.addPvewrap(v)
        pass

    def decode(self, pack):
        self.groupId = pack.popInt()
        self.dailyCount = pack.popInt()
        self.lastTime = pack.popLong()
        for i in range(pack.popShort()):
            PveWrap = Pvewrap()
            PveWrap.decode(pack)
            self.pveWraps.append(PveWrap)
        pass