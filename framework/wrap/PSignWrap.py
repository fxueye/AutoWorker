# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PSignWrap(Wrapper):
    uid = None #唯一标识
    signDayTimes = None #当天签到次数
    signMonthTimes = None #当月签到次数
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.signDayTimes)
        pack.addInt(self.signMonthTimes)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.signDayTimes = pack.popInt()
        self.signMonthTimes = pack.popInt()
        pass