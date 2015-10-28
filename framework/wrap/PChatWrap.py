# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PChatWrap(Wrapper):
    uid = None #唯一标识
    chatTimes = None #当天聊天次数
    lastChatTime = None #最后一次聊天时间
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.chatTimes)
        pack.addLong(self.lastChatTime)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.chatTimes = pack.popInt()
        self.lastChatTime = pack.popLong()
        pass