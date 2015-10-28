# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Activitywrap import Activitywrap# @UnresolvedImport
class GActivityWrap(Wrapper):
    uid = None #uid
    title = None #活动标题
    content = None #活动内容
    icon = None #活动图标
    hot = None #热度
    type = None #显示活动类型
    startTime = None #开始时间
    endTime = None #结束时间
    enabled = None #活动的状态
    gmName = None #gm
    activity = []
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.title)
        pack.addString(self.content)
        pack.addString(self.icon)
        pack.addInt(self.hot)
        pack.addInt(self.type)
        pack.addLong(self.startTime)
        pack.addLong(self.endTime)
        pack.addBoolean(self.enabled)
        pack.addString(self.gmName)
        pack.addShort(len(self.activity))
        for v in self.activity:
            pack.addActivitywrap(v)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.title = pack.popString()
        self.content = pack.popString()
        self.icon = pack.popString()
        self.hot = pack.popInt()
        self.type = pack.popInt()
        self.startTime = pack.popLong()
        self.endTime = pack.popLong()
        self.enabled = pack.popBoolean()
        self.gmName = pack.popString()
        for i in range(pack.popShort()):
            ActivityWrap = Activitywrap()
            ActivityWrap.decode(pack)
            self.activity.append(ActivityWrap)
        pass