# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class NoticeWrap(Wrapper):
    precedence = None #优先级
    content = None #内容
    time = None #发送时间
    continueTime = None #停留时间（秒）
    def encode(self, pack):
        pack.addInt(self.precedence)
        pack.addString(self.content)
        pack.addLong(self.time)
        pack.addInt(self.continueTime)
        pass

    def decode(self, pack):
        self.precedence = pack.popInt()
        self.content = pack.popString()
        self.time = pack.popLong()
        self.continueTime = pack.popInt()
        pass