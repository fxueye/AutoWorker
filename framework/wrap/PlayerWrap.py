# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Pactivitywrap import Pactivitywrap# @UnresolvedImport
from framework.wrap.Pchatwrap import Pchatwrap# @UnresolvedImport
from framework.wrap.Pguildwrap import Pguildwrap# @UnresolvedImport
from framework.wrap.Psignwrap import Psignwrap# @UnresolvedImport
class PlayerWrap(Wrapper):
    uid = None #uid
    name = None #名字
    icon = None #头像
    activity = []
    chat = None #聊天信息
    guild = None #工会信息
    sign = None #签到信息
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.name)
        pack.addString(self.icon)
        pack.addShort(len(self.activity))
        for v in self.activity:
            pack.addPactivitywrap(v)
        self.chat.encode(pack)
        self.guild.encode(pack)
        self.sign.encode(pack)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.name = pack.popString()
        self.icon = pack.popString()
        for i in range(pack.popShort()):
            PActivityWrap = Pactivitywrap()
            PActivityWrap.decode(pack)
            self.activity.append(PActivityWrap)
        PChatWrap = Pchatwrap()
        PChatWrap.decode(pack)
        self.chat =  PChatWrap
        PGuildWrap = Pguildwrap()
        PGuildWrap.decode(pack)
        self.guild =  PGuildWrap
        PSignWrap = Psignwrap()
        PSignWrap.decode(pack)
        self.sign =  PSignWrap
        pass