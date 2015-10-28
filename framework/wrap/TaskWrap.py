# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
from framework.wrap.Boolean import Boolean# @UnresolvedImport
class TaskWrap(Wrapper):
    uid = None #uid
    taskId = None #任务ID
    progress = None #任务完成度
    finished = None #是否已领取
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addInt(self.taskId)
        pack.addInt(self.progress)
        self.finished.encode(pack)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.taskId = pack.popInt()
        self.progress = pack.popInt()
        Boolean = Boolean()
        Boolean.decode(pack)
        self.finished =  Boolean
        pass