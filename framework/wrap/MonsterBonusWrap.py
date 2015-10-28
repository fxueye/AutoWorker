# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class MonsterBonusWrap(Wrapper):
    waveIdx = None #第几波的怪(1,2,3)
    monsterIdx = None #第几个怪(从0开始）
    itemIDs = []
    itemCounts = []
    def encode(self, pack):
        pack.addInt(self.waveIdx)
        pack.addInt(self.monsterIdx)
        pack.addShort(len(self.itemIDs))
        for v in self.itemIDs:
            v.encode(pack)
        pack.addShort(len(self.itemCounts))
        for v in self.itemCounts:
            v.encode(pack)
        pass

    def decode(self, pack):
        self.waveIdx = pack.popInt()
        self.monsterIdx = pack.popInt()
        for i in range(pack.popShort()):
            self.itemIDs.append(pack.popInt())
        for i in range(pack.popShort()):
            self.itemCounts.append(pack.popInt())
        pass