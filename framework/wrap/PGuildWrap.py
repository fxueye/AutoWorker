# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PGuildWrap(Wrapper):
    uid = None #唯一标识
    guildUid = None #公会UID
    guildStatus = None #公会状态
    guildMoney = None #公会货币
    outGuildTimes = None #退出公会
    joinGuildTimes = None #加入公会
    lastOutGuildTime = None #最后一次退出公会时间
    lastJoinGuildTime = None #最后一次加入公会时间
    restOutGuildTime = None #最后一次重置退出公会时间
    restJoinGuildTime = None #最后一次重置加入公会时间
    applyForGuilds = []
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.guildUid)
        pack.addBoolean(self.guildStatus)
        pack.addLong(self.guildMoney)
        pack.addInt(self.outGuildTimes)
        pack.addInt(self.joinGuildTimes)
        pack.addLong(self.lastOutGuildTime)
        pack.addLong(self.lastJoinGuildTime)
        pack.addLong(self.restOutGuildTime)
        pack.addLong(self.restJoinGuildTime)
        pack.addShort(len(self.applyForGuilds))
        for v in self.applyForGuilds:
            v.encode(pack)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.guildUid = pack.popString()
        self.guildStatus = pack.popBoolean()
        self.guildMoney = pack.popLong()
        self.outGuildTimes = pack.popInt()
        self.joinGuildTimes = pack.popInt()
        self.lastOutGuildTime = pack.popLong()
        self.lastJoinGuildTime = pack.popLong()
        self.restOutGuildTime = pack.popLong()
        self.restJoinGuildTime = pack.popLong()
        for i in range(pack.popShort()):
            self.applyForGuilds.append(pack.popString())
        pass