#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年7月27日
@author: QQ:281431280
'''
class Command(object):
    _opcode = None
    _pack = None
    _sid = None
    def __init__(self,opcode):
        self._opcode = opcode
        pass
    def setPack(self,pack):
        self._pack = pack
        pass
    def getpack(self):
        return self._pack
        pass
    def setSid(self,sid):
        self._sid = sid
        pass
    def getSid(self):
        return self._sid
        pass