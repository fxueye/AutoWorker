# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class TeamWrap(Wrapper):
    teamID = None #teamID
    heros = []
    def encode(self, pack):
        pack.addInt(self.teamID)
        pack.addShort(len(self.heros))
        for v in self.heros:
            v.encode(pack)
        pass

    def decode(self, pack):
        self.teamID = pack.popInt()
        for i in range(pack.popShort()):
            self.heros.append(pack.popString())
        pass