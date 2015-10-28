# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Pvpactorstatuswrap import Pvpactorstatuswrap# @UnresolvedImport
class PvpRoundWrap(Wrapper):
    order = None #顺序（1、2、3对应于左、中、右路，同时开始计时，4最后计时 ）
    actorStatusWrapList = []
    def encode(self, pack):
        pack.addInt(self.order)
        pack.addShort(len(self.actorStatusWrapList))
        for v in self.actorStatusWrapList:
            pack.addPvpactorstatuswrap(v)
        pass

    def decode(self, pack):
        self.order = pack.popInt()
        for i in range(pack.popShort()):
            PvpActorStatusWrap = Pvpactorstatuswrap()
            PvpActorStatusWrap.decode(pack)
            self.actorStatusWrapList.append(PvpActorStatusWrap)
        pass