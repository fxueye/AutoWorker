# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Boolean import Boolean# @UnresolvedImport
class GachaResultWrap(Wrapper):
    order = None #顺序
    itemId = None #道具ID,非道具为0
    itemCount = None #道具数量,非道具为0
    heroId = None #抽到的英雄ID
    awardHeroExist = None #抽到的英雄是否存在（true为存在，需要分解）
    def encode(self, pack):
        pack.addInt(self.order)
        pack.addInt(self.itemId)
        pack.addInt(self.itemCount)
        pack.addInt(self.heroId)
        self.awardHeroExist.encode(pack)
        pass

    def decode(self, pack):
        self.order = pack.popInt()
        self.itemId = pack.popInt()
        self.itemCount = pack.popInt()
        self.heroId = pack.popInt()
        Boolean = Boolean()
        Boolean.decode(pack)
        self.awardHeroExist =  Boolean
        pass