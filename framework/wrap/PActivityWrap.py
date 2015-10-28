# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class PActivityWrap(Wrapper):
    uid = None #任务UID
    activity_uid = None #任务UID
    progress = None #进度
    last_time = None #最后一次更新时间
    finished = None #是否完成
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.activity_uid)
        pack.addLong(self.progress)
        pack.addLong(self.last_time)
        pack.addBoolean(self.finished)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.activity_uid = pack.popString()
        self.progress = pack.popLong()
        self.last_time = pack.popLong()
        self.finished = pack.popBoolean()
        pass