# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class AccountWrap(Wrapper):
    uid = None #账号UID
    name = None #账户名
    status = None #账户状态
    platform = None #帐号平台
    pid = None #平台ID
    ret1 = None #保留字段1
    ret2 = None #保留字段2
    ret3 = None #保留字段3
    ret4 = None #保留字段4
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.name)
        pack.addInt(self.status)
        pack.addString(self.platform)
        pack.addString(self.pid)
        pack.addString(self.ret1)
        pack.addString(self.ret2)
        pack.addString(self.ret3)
        pack.addString(self.ret4)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.name = pack.popString()
        self.status = pack.popInt()
        self.platform = pack.popString()
        self.pid = pack.popString()
        self.ret1 = pack.popString()
        self.ret2 = pack.popString()
        self.ret3 = pack.popString()
        self.ret4 = pack.popString()
        pass