# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PveFriendInfoWrap(Wrapper):
    uid = None #uid
    levelId = None #关卡id
    friendIcon = []
    friendLevel = []
    friendName = []
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.levelId)
        pack.addShort(len(self.friendIcon))
        for v in self.friendIcon:
            v.encode(pack)
        pack.addShort(len(self.friendLevel))
        for v in self.friendLevel:
            v.encode(pack)
        pack.addShort(len(self.friendName))
        for v in self.friendName:
            v.encode(pack)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.levelId = pack.popInt()
        for i in range(pack.popShort()):
            self.friendIcon.append(pack.popString())
        for i in range(pack.popShort()):
            self.friendLevel.append(pack.popInt())
        for i in range(pack.popShort()):
            self.friendName.append(pack.popString())
        pass