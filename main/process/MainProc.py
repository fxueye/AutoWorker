# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.SProcess import SProcess
from main.services.MainService import MainService
from main.services.TimerService import TimerService


class MainProc(SProcess):
    _logger = None
    _main_service = None
    _timer_service = None
    _main_dev = None
    def __init__(self, mainDev):
        super(MainProc, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        self._main_service = MainService(self)
        self.registerService(self._main_service)
        self._timer_service = TimerService(self)
        self.registerService(self._timer_service)
        self._main_dev = mainDev
        pass
    def getMainDev(self):
        return self._main_dev
        pass
