#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年7月27日
@author: QQ:281431280
'''
import logging

from framework.Service import Service
from main.timer.MonitorAction import MonitorAction


class TimerService(Service):
    _logger = None
    _process = None
    _actions = []
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        pass
    def setProcess(self, proc):
        self._process = proc
        pass
    def addAction(self, action):
        self._actions.append(action)
        pass
    def removeAction(self, action):
        self._actions.remove(action)
        pass
    def close(self):
        self._actions = []
        pass
    def start(self):
        monitorAction = MonitorAction(self._process)
        self._actions.append(monitorAction)
        pass
    def update(self, diff, now):
        self._actions = filter(lambda x:not x.isOver(), self._actions)
        for a in self._actions:
            if a.update(diff, now):
                a.call()
        pass
