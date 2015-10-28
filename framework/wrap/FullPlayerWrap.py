# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Accountwrap import Accountwrap# @UnresolvedImport
from framework.wrap.Playerwrap import Playerwrap# @UnresolvedImport
from framework.wrap.Herowrap import Herowrap# @UnresolvedImport
from framework.wrap.Itemwrap import Itemwrap# @UnresolvedImport
from framework.wrap.Taskwrap import Taskwrap# @UnresolvedImport
from framework.wrap.Mailwrap import Mailwrap# @UnresolvedImport
from framework.wrap.Gachawrap import Gachawrap# @UnresolvedImport
from framework.wrap.Noticewrap import Noticewrap# @UnresolvedImport
from framework.wrap.Pvegroupwrap import Pvegroupwrap# @UnresolvedImport
from framework.wrap.Shopwrap import Shopwrap# @UnresolvedImport
from framework.wrap.Teamwrap import Teamwrap# @UnresolvedImport
class FullPlayerWrap(Wrapper):
    sysTime = None #系统时间（UTC时间ms)
    accountWrap = None #账户信息
    playerWrap = None #玩家基本信息
    heroWraps = []
    itemWraps = []
    taskWraps = []
    mailWraps = []
    gachaWraps = []
    noticeWraps = []
    otherPlayerNames = []
    pveGroupWraps = []
    shopWraps = []
    teamWraps = []
    def encode(self, pack):
        pack.addLong(self.sysTime)
        self.accountWrap.encode(pack)
        self.playerWrap.encode(pack)
        pack.addShort(len(self.heroWraps))
        for v in self.heroWraps:
            pack.addHerowrap(v)
        pack.addShort(len(self.itemWraps))
        for v in self.itemWraps:
            pack.addItemwrap(v)
        pack.addShort(len(self.taskWraps))
        for v in self.taskWraps:
            pack.addTaskwrap(v)
        pack.addShort(len(self.mailWraps))
        for v in self.mailWraps:
            pack.addMailwrap(v)
        pack.addShort(len(self.gachaWraps))
        for v in self.gachaWraps:
            pack.addGachawrap(v)
        pack.addShort(len(self.noticeWraps))
        for v in self.noticeWraps:
            pack.addNoticewrap(v)
        pack.addShort(len(self.otherPlayerNames))
        for v in self.otherPlayerNames:
            v.encode(pack)
        pack.addShort(len(self.pveGroupWraps))
        for v in self.pveGroupWraps:
            pack.addPvegroupwrap(v)
        pack.addShort(len(self.shopWraps))
        for v in self.shopWraps:
            pack.addShopwrap(v)
        pack.addShort(len(self.teamWraps))
        for v in self.teamWraps:
            pack.addTeamwrap(v)
        pass

    def decode(self, pack):
        self.sysTime = pack.popLong()
        AccountWrap = Accountwrap()
        AccountWrap.decode(pack)
        self.accountWrap =  AccountWrap
        PlayerWrap = Playerwrap()
        PlayerWrap.decode(pack)
        self.playerWrap =  PlayerWrap
        for i in range(pack.popShort()):
            HeroWrap = Herowrap()
            HeroWrap.decode(pack)
            self.heroWraps.append(HeroWrap)
        for i in range(pack.popShort()):
            ItemWrap = Itemwrap()
            ItemWrap.decode(pack)
            self.itemWraps.append(ItemWrap)
        for i in range(pack.popShort()):
            TaskWrap = Taskwrap()
            TaskWrap.decode(pack)
            self.taskWraps.append(TaskWrap)
        for i in range(pack.popShort()):
            MailWrap = Mailwrap()
            MailWrap.decode(pack)
            self.mailWraps.append(MailWrap)
        for i in range(pack.popShort()):
            GachaWrap = Gachawrap()
            GachaWrap.decode(pack)
            self.gachaWraps.append(GachaWrap)
        for i in range(pack.popShort()):
            NoticeWrap = Noticewrap()
            NoticeWrap.decode(pack)
            self.noticeWraps.append(NoticeWrap)
        for i in range(pack.popShort()):
            self.otherPlayerNames.append(pack.popString())
        for i in range(pack.popShort()):
            PveGroupWrap = Pvegroupwrap()
            PveGroupWrap.decode(pack)
            self.pveGroupWraps.append(PveGroupWrap)
        for i in range(pack.popShort()):
            ShopWrap = Shopwrap()
            ShopWrap.decode(pack)
            self.shopWraps.append(ShopWrap)
        for i in range(pack.popShort()):
            TeamWrap = Teamwrap()
            TeamWrap.decode(pack)
            self.teamWraps.append(TeamWrap)
        pass