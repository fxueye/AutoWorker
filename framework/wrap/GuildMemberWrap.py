# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Activewrap import Activewrap# @UnresolvedImport
class GuildMemberWrap(Wrapper):
    uid = None #UID
    guildIUid = None #工会UID
    playerName = None #帐号
    playerUid = None #角色唯一ID
    position = None #权限
    active = []
    awardCoin = None #收获金币数量
    worshipTimes = None #膜拜次数
    createTime = None #创建世时间
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.guildIUid)
        pack.addString(self.playerName)
        pack.addString(self.playerUid)
        pack.addInt(self.position)
        pack.addShort(len(self.active))
        for v in self.active:
            pack.addActivewrap(v)
        pack.addInt(self.awardCoin)
        pack.addInt(self.worshipTimes)
        pack.addLong(self.createTime)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.guildIUid = pack.popString()
        self.playerName = pack.popString()
        self.playerUid = pack.popString()
        self.position = pack.popInt()
        for i in range(pack.popShort()):
            ActiveWrap = Activewrap()
            ActiveWrap.decode(pack)
            self.active.append(ActiveWrap)
        self.awardCoin = pack.popInt()
        self.worshipTimes = pack.popInt()
        self.createTime = pack.popLong()
        pass