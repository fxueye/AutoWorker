# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Btherowrap import Btherowrap# @UnresolvedImport
class PvpRankWrap(Wrapper):
    name = None #角色名
    playerUid = None #角色UID
    rank = None #排名
    fightValue = None #战斗力
    point = None #积分
    grade = None #段位
    heroWraps = []
    def encode(self, pack):
        pack.addString(self.name)
        pack.addString(self.playerUid)
        pack.addInt(self.rank)
        pack.addInt(self.fightValue)
        pack.addInt(self.point)
        pack.addInt(self.grade)
        pack.addShort(len(self.heroWraps))
        for v in self.heroWraps:
            pack.addBtherowrap(v)
        pass

    def decode(self, pack):
        self.name = pack.popString()
        self.playerUid = pack.popString()
        self.rank = pack.popInt()
        self.fightValue = pack.popInt()
        self.point = pack.popInt()
        self.grade = pack.popInt()
        for i in range(pack.popShort()):
            BTHeroWrap = Btherowrap()
            BTHeroWrap.decode(pack)
            self.heroWraps.append(BTHeroWrap)
        pass