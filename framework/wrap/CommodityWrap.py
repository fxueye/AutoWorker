# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class CommodityWrap(Wrapper):
    position = None #position
    itemId = None #商品ID
    itemCount = None #数量
    priceId = None #价格ID(货币对应的ItemID)
    price = None #价格
    isDiscounts = None #是否打折
    isSell = None #是否售完
    isLock = None #是否解锁
    def encode(self, pack):
        pack.addInt(self.position)
        pack.addInt(self.itemId)
        pack.addInt(self.itemCount)
        pack.addInt(self.priceId)
        pack.addInt(self.price)
        pack.addBoolean(self.isDiscounts)
        pack.addBoolean(self.isSell)
        pack.addBoolean(self.isLock)
        pass

    def decode(self, pack):
        self.position = pack.popInt()
        self.itemId = pack.popInt()
        self.itemCount = pack.popInt()
        self.priceId = pack.popInt()
        self.price = pack.popInt()
        self.isDiscounts = pack.popBoolean()
        self.isSell = pack.popBoolean()
        self.isLock = pack.popBoolean()
        pass