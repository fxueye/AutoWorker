# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Bossdamwrap import Bossdamwrap# @UnresolvedImport
from framework.wrap.Bossdamwrap import Bossdamwrap# @UnresolvedImport
class BossWrap(Wrapper):
    bossLv = None #boss等级
    bossHP = None #boss血量
    bossStarted = None #boss是否开启
    killer = None #击杀者信息
    topTen = []
    boostLv = None #鼓舞等级
    lastBoostTime = None #上一次金币鼓舞的时间(ms)
    lastBattleTime = None #上一次战斗的时间(ms)
    goldBoostCount = None #钻石鼓舞次数
    damage = None #造成的伤害
    rank = None #当前排名
    attackCount = None #攻击次数
    def encode(self, pack):
        pack.addInt(self.bossLv)
        pack.addDouble(self.bossHP)
        pack.addBoolean(self.bossStarted)
        self.killer.encode(pack)
        pack.addShort(len(self.topTen))
        for v in self.topTen:
            pack.addBossdamwrap(v)
        pack.addInt(self.boostLv)
        pack.addLong(self.lastBoostTime)
        pack.addLong(self.lastBattleTime)
        pack.addInt(self.goldBoostCount)
        pack.addDouble(self.damage)
        pack.addInt(self.rank)
        pack.addInt(self.attackCount)
        pass

    def decode(self, pack):
        self.bossLv = pack.popInt()
        self.bossHP = pack.popDouble()
        self.bossStarted = pack.popBoolean()
        BossDamWrap = Bossdamwrap()
        BossDamWrap.decode(pack)
        self.killer =  BossDamWrap
        for i in range(pack.popShort()):
            BossDamWrap = Bossdamwrap()
            BossDamWrap.decode(pack)
            self.topTen.append(BossDamWrap)
        self.boostLv = pack.popInt()
        self.lastBoostTime = pack.popLong()
        self.lastBattleTime = pack.popLong()
        self.goldBoostCount = pack.popInt()
        self.damage = pack.popDouble()
        self.rank = pack.popInt()
        self.attackCount = pack.popInt()
        pass