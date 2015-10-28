# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class BonusWrap(Wrapper):
    pveId = None #
    itemIds = []
    itemCounts = []
    MonsterBonusIds = []
    MonsterBonusCounts = []
    BossBonusIds = []
    BossBounsCounts = []
    def encode(self, pack):
        pack.addInt(self.pveId)
        pack.addShort(len(self.itemIds))
        for v in self.itemIds:
            v.encode(pack)
        pack.addShort(len(self.itemCounts))
        for v in self.itemCounts:
            v.encode(pack)
        pack.addShort(len(self.MonsterBonusIds))
        for v in self.MonsterBonusIds:
            v.encode(pack)
        pack.addShort(len(self.MonsterBonusCounts))
        for v in self.MonsterBonusCounts:
            v.encode(pack)
        pack.addShort(len(self.BossBonusIds))
        for v in self.BossBonusIds:
            v.encode(pack)
        pack.addShort(len(self.BossBounsCounts))
        for v in self.BossBounsCounts:
            v.encode(pack)
        pass

    def decode(self, pack):
        self.pveId = pack.popInt()
        for i in range(pack.popShort()):
            self.itemIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.itemCounts.append(pack.popInt())
        for i in range(pack.popShort()):
            self.MonsterBonusIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.MonsterBonusCounts.append(pack.popInt())
        for i in range(pack.popShort()):
            self.BossBonusIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.BossBounsCounts.append(pack.popInt())
        pass