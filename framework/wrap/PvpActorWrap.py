# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PvpActorWrap(Wrapper):
    heroUid = None #英雄UID
    heroId = None #英雄ID(暂用DemoHeroConfig中的id)
    isAttacker = None #是否攻方（攻方初始在上面）
    def encode(self, pack):
        pack.addString(self.heroUid)
        pack.addInt(self.heroId)
        pack.addBoolean(self.isAttacker)
        pass

    def decode(self, pack):
        self.heroUid = pack.popString()
        self.heroId = pack.popInt()
        self.isAttacker = pack.popBoolean()
        pass