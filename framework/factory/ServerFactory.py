# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年7月7日
@author: QQ:281431280
'''
from twisted.internet.protocol import Factory

from framework.handler.IoHander import IoHander
import logging


class ServerFactory(Factory):
    _clients = None
    _main_dev = None
    _logger = None
    
    def __init__(self,mainDev):
        self._clients = dict()
        self._main_dev = mainDev
        self._logger = logging.getLogger(str(__name__))
        pass
    def buildProtocol(self, addr):
        return IoHander(self)
        pass
    def getClients(self):
        return self._clients
        pass
    def addNewSession(self,sid,IoHander):
        if not self._clients.has_key(sid):
            self._clients[sid] = IoHander
        else:
            self._logger.error("sid eorror "+sid)
        pass
    def removeSession(self,sid):
        if self._clients.has_key(sid):
            del self._clients[sid]
        else:
            self._logger.error("not find sid :"+sid)
        pass
    def getSession(self,sid):
        if self._clients.has_key(sid):
            return self._clients.get(sid)
        else:
            self._logger.error("not find sid "+sid)
        pass
    def getMainDev(self):
        return self._main_dev
        pass
