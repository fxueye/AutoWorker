# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class BTHeroWrap(Wrapper):
    uid = None #UID
    heroId = None #英雄ID
    heroLv = None #等级
    figureId = None #形象ID
    gunId = None #装备的枪ID
    propIds = []
    propValues = []
    gunPropIds = []
    gunPropValues = []
    skillIds = []
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.heroId)
        pack.addInt(self.heroLv)
        pack.addInt(self.figureId)
        pack.addInt(self.gunId)
        pack.addShort(len(self.propIds))
        for v in self.propIds:
            v.encode(pack)
        pack.addShort(len(self.propValues))
        for v in self.propValues:
            v.encode(pack)
        pack.addShort(len(self.gunPropIds))
        for v in self.gunPropIds:
            v.encode(pack)
        pack.addShort(len(self.gunPropValues))
        for v in self.gunPropValues:
            v.encode(pack)
        pack.addShort(len(self.skillIds))
        for v in self.skillIds:
            v.encode(pack)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.heroId = pack.popInt()
        self.heroLv = pack.popInt()
        self.figureId = pack.popInt()
        self.gunId = pack.popInt()
        for i in range(pack.popShort()):
            self.propIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.propValues.append(pack.popDouble())
        for i in range(pack.popShort()):
            self.gunPropIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.gunPropValues.append(pack.popDouble())
        for i in range(pack.popShort()):
            self.skillIds.append(pack.popInt())
        pass