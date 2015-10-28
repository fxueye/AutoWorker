# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class BuildRankWrap(Wrapper):
    playerName = None #玩家名字
    itemId = []
    itemCount = []
    awardItemId = None #建造获取物品的id
    awardHeroId = None #建造获取的英雄id
    time = None #获取奖励时间
    def encode(self, pack):
        pack.addString(self.playerName)
        pack.addShort(len(self.itemId))
        for v in self.itemId:
            v.encode(pack)
        pack.addShort(len(self.itemCount))
        for v in self.itemCount:
            v.encode(pack)
        pack.addInt(self.awardItemId)
        pack.addInt(self.awardHeroId)
        pack.addLong(self.time)
        pass

    def decode(self, pack):
        self.playerName = pack.popString()
        for i in range(pack.popShort()):
            self.itemId.append(pack.popInt())
        for i in range(pack.popShort()):
            self.itemCount.append(pack.popInt())
        self.awardItemId = pack.popInt()
        self.awardHeroId = pack.popInt()
        self.time = pack.popLong()
        pass