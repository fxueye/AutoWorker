# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.timer.Action import Action
from framework.timer.PeriodicTimer import PeriodicTimer
from util.SysConfig import SysConfig
from util.TimerUtil import TimerUtil
from public.AppQueue import AppQueue

class MonitorAction(Action):
    _logger = None
    _process = None
    _timer = None
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        monitorSecond = SysConfig.config["servers"]["monitorSecond"]
        if not monitorSecond:
            monitorSecond = 5
        self._timer = PeriodicTimer(TimerUtil.secondToMills(monitorSecond))
        self._process = proc
        pass
    def update(self, diff, now):
        return self._timer.update(diff)
        pass        
    def call(self): 
        self._logger.debug("numiid count:%d"%(AppQueue.numiidQueue.qsize()) )
        pass
    def isOver(self):
        return False
        pass
