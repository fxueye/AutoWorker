# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class RuneWrap(Wrapper):
    runeId = None #符文id
    exp = None #符文经验
    idx = None #索引
    def encode(self, pack):
        pack.addInt(self.runeId)
        pack.addInt(self.exp)
        pack.addInt(self.idx)
        pass

    def decode(self, pack):
        self.runeId = pack.popInt()
        self.exp = pack.popInt()
        self.idx = pack.popInt()
        pass