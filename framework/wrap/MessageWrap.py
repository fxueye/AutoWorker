# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class MessageWrap(Wrapper):
    channelId = None #频道Id
    name = None #玩家名字
    lv = None #玩家等级
    icon = None #头像
    content = None #内容
    time = None #时间
    guildUID = None #工会UID
    def encode(self, pack):
        pack.addInt(self.channelId)
        pack.addString(self.name)
        pack.addInt(self.lv)
        pack.addString(self.icon)
        pack.addString(self.content)
        pack.addLong(self.time)
        pack.addString(self.guildUID)
        pass

    def decode(self, pack):
        self.channelId = pack.popInt()
        self.name = pack.popString()
        self.lv = pack.popInt()
        self.icon = pack.popString()
        self.content = pack.popString()
        self.time = pack.popLong()
        self.guildUID = pack.popString()
        pass