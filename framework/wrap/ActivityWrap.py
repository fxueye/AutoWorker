# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class ActivityWrap(Wrapper):
    uid = None #活动ID
    gActivityUid = None #活动组UID
    title = None #活动标题
    itemId = []
    itemCount = []
    condition = None #完成条件
    type = None #活动类型
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.gActivityUid)
        pack.addString(self.title)
        pack.addShort(len(self.itemId))
        for v in self.itemId:
            v.encode(pack)
        pack.addShort(len(self.itemCount))
        for v in self.itemCount:
            v.encode(pack)
        pack.addInt(self.condition)
        pack.addInt(self.type)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.gActivityUid = pack.popString()
        self.title = pack.popString()
        for i in range(pack.popShort()):
            self.itemId.append(pack.popInt())
        for i in range(pack.popShort()):
            self.itemCount.append(pack.popInt())
        self.condition = pack.popInt()
        self.type = pack.popInt()
        pass