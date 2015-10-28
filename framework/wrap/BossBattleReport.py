# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Bossdamwrap import Bossdamwrap# @UnresolvedImport
class BossBattleReport(Wrapper):
    playerInfo = None #玩家伤害信息
    bossUID = None #bossUID
    bossHP = None #boss战斗前的血量
    isWin = None #是否击杀
    def encode(self, pack):
        self.playerInfo.encode(pack)
        pack.addLong(self.bossUID)
        pack.addDouble(self.bossHP)
        pack.addBoolean(self.isWin)
        pass

    def decode(self, pack):
        BossDamWrap = Bossdamwrap()
        BossDamWrap.decode(pack)
        self.playerInfo =  BossDamWrap
        self.bossUID = pack.popLong()
        self.bossHP = pack.popDouble()
        self.isWin = pack.popBoolean()
        pass