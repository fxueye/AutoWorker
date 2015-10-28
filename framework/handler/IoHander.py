# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年7月7日
@author: QQ:281431280
'''



import logging
from uuid import uuid1

from twisted.internet.protocol import Protocol
from framework.Packet import Packet
from framework.Command import Command
from public.AppQueue import AppQueue


class IoHander(Protocol):
    _sid = None
    _logger = None
    _factory = None
    
    def __init__(self, factory):
        self._logger = logging.getLogger(str(__name__))
        self._factory = factory
        self._sid = uuid1()
        pass
    # 接收到数据
    def dataReceived(self, data):
        pack = Packet()
        pack.setBuffer(data)
        opcode = pack.popShort()
        cmd = Command(opcode)
        cmd.setPack(pack)
        cmd.setSid(self._sid)
        AppQueue.cmdQueue.put(cmd)
        pass
    # 断开连接
    def connectionLost(self, reason):
        self._factory.removeSession(self._sid)
        self._logger.debug("close client ip:%s:%d"%(str(self.transport.getPeer().host),self.transport.getPeer().port))
        pass
    # 新建立的连接
    def connectionMade(self):
#         self.setSid(uuid1())
        self._factory.addNewSession(self._sid,self)
        self._logger.debug(self.getSid())
        self._logger.debug("new client ip:%s:%d"%(str(self.transport.getPeer().host),self.transport.getPeer().port))
        pass
    def getSid(self):
        return self._sid
        pass
    def setSid(self,sid):
        self._sid = sid;
        pass
