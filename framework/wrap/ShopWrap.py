# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Commoditywrap import Commoditywrap# @UnresolvedImport
class ShopWrap(Wrapper):
    shopId = None #商店ID
    commodityWraps = []
    refreshDaily = None #当天刷新次数
    status = None #商店的状态0正常1永久召唤
    endTime = None #商店结束时间(s)
    def encode(self, pack):
        pack.addInt(self.shopId)
        pack.addShort(len(self.commodityWraps))
        for v in self.commodityWraps:
            pack.addCommoditywrap(v)
        pack.addInt(self.refreshDaily)
        pack.addInt(self.status)
        pack.addInt(self.endTime)
        pass

    def decode(self, pack):
        self.shopId = pack.popInt()
        for i in range(pack.popShort()):
            CommodityWrap = Commoditywrap()
            CommodityWrap.decode(pack)
            self.commodityWraps.append(CommodityWrap)
        self.refreshDaily = pack.popInt()
        self.status = pack.popInt()
        self.endTime = pack.popInt()
        pass