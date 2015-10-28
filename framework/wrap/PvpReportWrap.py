# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Pvproundwrap import Pvproundwrap# @UnresolvedImport
from framework.wrap.Pvpactorwrap import Pvpactorwrap# @UnresolvedImport
class PvpReportWrap(Wrapper):
    reportUid = None #UID
    pvpRoundWrapList = []
    pvpActorWrapList = []
    def encode(self, pack):
        pack.addString(self.reportUid)
        pack.addShort(len(self.pvpRoundWrapList))
        for v in self.pvpRoundWrapList:
            pack.addPvproundwrap(v)
        pack.addShort(len(self.pvpActorWrapList))
        for v in self.pvpActorWrapList:
            pack.addPvpactorwrap(v)
        pass

    def decode(self, pack):
        self.reportUid = pack.popString()
        for i in range(pack.popShort()):
            PvpRoundWrap = Pvproundwrap()
            PvpRoundWrap.decode(pack)
            self.pvpRoundWrapList.append(PvpRoundWrap)
        for i in range(pack.popShort()):
            PvpActorWrap = Pvpactorwrap()
            PvpActorWrap.decode(pack)
            self.pvpActorWrapList.append(PvpActorWrap)
        pass