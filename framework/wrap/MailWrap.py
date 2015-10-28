# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月18日
@author: QQ:281431280
'''
from framework.wrap.base.Wrapper import Wrapper
class MailWrap(Wrapper):
    uid = None #uid
    senderName = None #发送者名称
    title = None #标题
    content = None #内容
    time = None #发送时间
    itemIds = []
    itemCounts = []
    status = None #邮件状态
    def encode(self, pack):
        pack.addString(self.uid)
        pack.addString(self.senderName)
        pack.addString(self.title)
        pack.addString(self.content)
        pack.addLong(self.time)
        pack.addShort(len(self.itemIds))
        for v in self.itemIds:
            v.encode(pack)
        pack.addShort(len(self.itemCounts))
        for v in self.itemCounts:
            v.encode(pack)
        pack.addInt(self.status)
        pass

    def decode(self, pack):
        self.uid = pack.popString()
        self.senderName = pack.popString()
        self.title = pack.popString()
        self.content = pack.popString()
        self.time = pack.popLong()
        for i in range(pack.popShort()):
            self.itemIds.append(pack.popInt())
        for i in range(pack.popShort()):
            self.itemCounts.append(pack.popInt())
        self.status = pack.popInt()
        pass