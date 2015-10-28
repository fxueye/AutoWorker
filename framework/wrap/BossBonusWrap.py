# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Bonuswrap import Bonuswrap# @UnresolvedImport
class BossBonusWrap(Wrapper):
    bossLv = None #boss等级
    killerName = None #击杀boss的文件名称
    aPlayerToBossHurt = None #单个玩家对boss的累计伤害
    aPlayerRank = None #单个玩家排名
    bonusWrap = None #单个玩家获得的奖励
    def encode(self, pack):
        pack.addInt(self.bossLv)
        pack.addString(self.killerName)
        pack.addDouble(self.aPlayerToBossHurt)
        pack.addInt(self.aPlayerRank)
        self.bonusWrap.encode(pack)
        pass

    def decode(self, pack):
        self.bossLv = pack.popInt()
        self.killerName = pack.popString()
        self.aPlayerToBossHurt = pack.popDouble()
        self.aPlayerRank = pack.popInt()
        BonusWrap = Bonuswrap()
        BonusWrap.decode(pack)
        self.bonusWrap =  BonusWrap
        pass