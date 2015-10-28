# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging.config
import os

from util.SysConfig import SysConfig
class SDevice(object):
    _processList = [];
    def __init__(self):
        runPath = os.getcwd()
        SysConfig.load("%s/config/config.json" % (runPath))
        logging.config.fileConfig("%s/config/logging.conf" % (runPath))
        pass
    def start(self):
        for p in self._processList:
            p.start();
        pass
    def close(self):
        for p in self._processList:
            p.close()
        pass
    def addProcess(self, process, interval):
        process.setInterval(interval)
        self._processList.append(process)
    def allClosed(self):
        for p in self._processList:
            if p.is_active():
                return False;
        return True
    def getProcessCount(self):
        return len(self._processList)
        
