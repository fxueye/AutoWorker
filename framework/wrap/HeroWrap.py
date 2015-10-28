# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Runewrap import Runewrap# @UnresolvedImport
class HeroWrap(Wrapper):
    uid = None #UID
    heroId = None #英雄ID
    heroExp = None #经验
    createTime = None #创建时间
    star = None #星级
    grade = None #品阶
    equipIDs = []
    equipExps = []
    skillIds = []
    skillLvs = []
    runeWraps = []
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.heroId)
        pack.addInt(self.heroExp)
        pack.addLong(self.createTime)
        pack.addInt(self.star)
        pack.addInt(self.grade)
        pack.addShort(len(self.equipIDs))
        for v in self.equipIDs:
            v.encode(pack)
        pack.addShort(len(self.equipExps))
        for v in self.equipExps:
            v.encode(pack)
        pack.addShort(len(self.skillIds))
        for v in self.skillIds:
            v.encode(pack)
        pack.addShort(len(self.skillLvs))
        for v in self.skillLvs:
            v.encode(pack)
        pack.addShort(len(self.runeWraps))
        for v in self.runeWraps:
            pack.addRunewrap(v)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.heroId = pack.popInt()
        self.heroExp = pack.popInt()
        self.createTime = pack.popLong()
        self.star = pack.popInt()
        self.grade = pack.popInt()
        for i in range(pack.popShort()):
            self.equipIDs.append(pack.popInt())
        for i in range(pack.popShort()):
            self.equipExps.append(pack.popInt())
        for i in range(pack.popShort()):
            self.skillIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.skillLvs.append(pack.popInt())
        for i in range(pack.popShort()):
            RuneWrap = Runewrap()
            RuneWrap.decode(pack)
            self.runeWraps.append(RuneWrap)
        pass