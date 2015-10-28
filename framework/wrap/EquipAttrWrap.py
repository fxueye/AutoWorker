# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class EquipAttrWrap(Wrapper):
    index = None #索引
    attrId = None #属性Id
    value = None #属性值
    quality = None #品质(0白1绿2蓝3紫)
    equipRndId = None #HeroEquipRandConfig中的ID
    isOld = None #是否是旧属性
    def encode(self, pack):
        pack.addInt(self.index)
        pack.addInt(self.attrId)
        pack.addDouble(self.value)
        pack.addInt(self.quality)
        pack.addInt(self.equipRndId)
        pack.addBoolean(self.isOld)
        pass

    def decode(self, pack):
        self.index = pack.popInt()
        self.attrId = pack.popInt()
        self.value = pack.popDouble()
        self.quality = pack.popInt()
        self.equipRndId = pack.popInt()
        self.isOld = pack.popBoolean()
        pass