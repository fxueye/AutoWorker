# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class BossDamWrap(Wrapper):
    rank = None #排名
    playerUID = None #玩家UID
    playerLv = None #玩家等级
    playerName = None #玩家名字
    playerIcon = None #玩家头像
    figureID = None #形象ID
    damage = None #伤害
    def encode(self, pack):
        pack.addInt(self.rank)
        pack.addLong(self.playerUID)
        pack.addInt(self.playerLv)
        pack.addString(self.playerName)
        pack.addString(self.playerIcon)
        pack.addInt(self.figureID)
        pack.addDouble(self.damage)
        pass

    def decode(self, pack):
        self.rank = pack.popInt()
        self.playerUID = pack.popLong()
        self.playerLv = pack.popInt()
        self.playerName = pack.popString()
        self.playerIcon = pack.popString()
        self.figureID = pack.popInt()
        self.damage = pack.popDouble()
        pass