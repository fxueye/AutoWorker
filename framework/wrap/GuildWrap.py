# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Guildmemberwrap import Guildmemberwrap# @UnresolvedImport
from framework.wrap.Guildlogwrap import Guildlogwrap# @UnresolvedImport
class GuildWrap(Wrapper):
    uid = None #UID
    id = None #公会ID
    name = None #公会名称
    icon = None #公会图标
    declaration = None #公会说明
    active = None #活跃度
    historyActive = None #活跃度
    inCondition = None #加入条件
    inLevel = None #加入等级
    maxMember = None #最大加入会员数
    dump = None #掉落插队
    pveTeam = []
    createTime = None #公会创建时间
    members = []
    logs = []
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.id)
        pack.addString(self.name)
        pack.addString(self.icon)
        pack.addString(self.declaration)
        pack.addInt(self.active)
        pack.addInt(self.historyActive)
        pack.addInt(self.inCondition)
        pack.addInt(self.inLevel)
        pack.addInt(self.maxMember)
        pack.addBoolean(self.dump)
        pack.addShort(len(self.pveTeam))
        for v in self.pveTeam:
            v.encode(pack)
        pack.addLong(self.createTime)
        pack.addShort(len(self.members))
        for v in self.members:
            pack.addGuildmemberwrap(v)
        pack.addShort(len(self.logs))
        for v in self.logs:
            pack.addGuildlogwrap(v)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.id = pack.popInt()
        self.name = pack.popString()
        self.icon = pack.popString()
        self.declaration = pack.popString()
        self.active = pack.popInt()
        self.historyActive = pack.popInt()
        self.inCondition = pack.popInt()
        self.inLevel = pack.popInt()
        self.maxMember = pack.popInt()
        self.dump = pack.popBoolean()
        for i in range(pack.popShort()):
            self.pveTeam.append(pack.popString())
        self.createTime = pack.popLong()
        for i in range(pack.popShort()):
            GuildMemberWrap = Guildmemberwrap()
            GuildMemberWrap.decode(pack)
            self.members.append(GuildMemberWrap)
        for i in range(pack.popShort()):
            GuildLogWrap = Guildlogwrap()
            GuildLogWrap.decode(pack)
            self.logs.append(GuildLogWrap)
        pass