# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class ItemWrap(Wrapper):
    uid = None #道具UID
    itemId = None #道具ID
    itemCount = None #道具数量
    lastRefreshTime = None #上一次更新时间
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.itemId)
        pack.addLong(self.itemCount)
        pack.addLong(self.lastRefreshTime)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.itemId = pack.popInt()
        self.itemCount = pack.popLong()
        self.lastRefreshTime = pack.popLong()
        pass