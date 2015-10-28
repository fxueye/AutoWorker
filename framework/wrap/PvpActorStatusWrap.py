# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PvpActorStatusWrap(Wrapper):
    heroUid = None #英雄UID
    armorPercent = None #剩余护甲百分比(保留)
    shieldPercent = None #剩余护盾百分比(保留)
    hpPercent = None #剩余血量百分比(保留)
    roundTime = None #该回合行动时间（s），为0表示存活下来，耗血时间等于对方回合时间的和
    def encode(self, pack):
        pack.addString(self.heroUid)
        pack.addDouble(self.armorPercent)
        pack.addDouble(self.shieldPercent)
        pack.addDouble(self.hpPercent)
        pack.addDouble(self.roundTime)
        pass

    def decode(self, pack):
        self.heroUid = pack.popString()
        self.armorPercent = pack.popDouble()
        self.shieldPercent = pack.popDouble()
        self.hpPercent = pack.popDouble()
        self.roundTime = pack.popDouble()
        pass