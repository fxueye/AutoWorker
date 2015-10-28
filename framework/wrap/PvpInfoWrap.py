# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Pvprankwrap import Pvprankwrap# @UnresolvedImport
from framework.wrap.Pvprankwrap import Pvprankwrap# @UnresolvedImport
class PvpInfoWrap(Wrapper):
    rank = None #排名
    point = None #积分
    grade = None #段位
    topRankWraps = []
    rankWraps = []
    def encode(self, pack):
        pack.addInt(self.rank)
        pack.addInt(self.point)
        pack.addInt(self.grade)
        pack.addShort(len(self.topRankWraps))
        for v in self.topRankWraps:
            pack.addPvprankwrap(v)
        pack.addShort(len(self.rankWraps))
        for v in self.rankWraps:
            pack.addPvprankwrap(v)
        pass

    def decode(self, pack):
        self.rank = pack.popInt()
        self.point = pack.popInt()
        self.grade = pack.popInt()
        for i in range(pack.popShort()):
            PvpRankWrap = Pvprankwrap()
            PvpRankWrap.decode(pack)
            self.topRankWraps.append(PvpRankWrap)
        for i in range(pack.popShort()):
            PvpRankWrap = Pvprankwrap()
            PvpRankWrap.decode(pack)
            self.rankWraps.append(PvpRankWrap)
        pass