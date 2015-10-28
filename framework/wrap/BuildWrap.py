# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class BuildWrap(Wrapper):
    position = None #建造位置
    buildEndTime = None #建造倒计时(单位秒，为-1表示为建造，0表示建造完成)
    awardHeroId = None #建造获得的英雄id(没建造完不发送给客户端)
    awardItemId = None #建造获得物品的id(没建造完不发送给客户端)
    unlock = None #是否解锁
    def encode(self, pack):
        pack.addInt(self.position)
        pack.addInt(self.buildEndTime)
        pack.addInt(self.awardHeroId)
        pack.addInt(self.awardItemId)
        pack.addBoolean(self.unlock)
        pass

    def decode(self, pack):
        self.position = pack.popInt()
        self.buildEndTime = pack.popInt()
        self.awardHeroId = pack.popInt()
        self.awardItemId = pack.popInt()
        self.unlock = pack.popBoolean()
        pass