# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class SignWrap(Wrapper):
    itemIDs = []
    itemCounts = []
    vipLvDouble = None #vip领双份等级
    validTime = None #生效时间
    days = None #签到的天数
    def encode(self, pack):
        pack.addShort(len(self.itemIDs))
        for v in self.itemIDs:
            v.encode(pack)
        pack.addShort(len(self.itemCounts))
        for v in self.itemCounts:
            v.encode(pack)
        pack.addInt(self.vipLvDouble)
        pack.addLong(self.validTime)
        pack.addInt(self.days)
        pass

    def decode(self, pack):
        for i in range(pack.popShort()):
            self.itemIDs.append(pack.popInt())
        for i in range(pack.popShort()):
            self.itemCounts.append(pack.popInt())
        self.vipLvDouble = pack.popInt()
        self.validTime = pack.popLong()
        self.days = pack.popInt()
        pass