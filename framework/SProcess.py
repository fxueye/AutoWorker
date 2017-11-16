# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging
import threading
import time

from framework.WorkLoading import WorkLoading


class SProcess(threading.Thread):
    _logger = None
    _interval = None
    _running = None
    _workLoading = None
    _services = None
    def __init__(self):
        super(SProcess, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        self._services = []
        self._running = False
        self._interval = 0
        pass
    def registerService(self, service):
        self._services.append(service)
    def start(self):
        super(SProcess, self).start()
        pass
    def setInterval(self, interval):
        if interval > 0:
            self._interval = interval
    def run(self):
        self._workLoading = WorkLoading((time.time() * 1000))
        self._running = True
        for service in self._services:
            service.start()
        runing = True
        while runing:
            workTime = self._workLoading.getWorkTime()
            for s in self._services:
                s.update(self._interval, workTime)
            block = self._workLoading.updateWorkTime(self._interval, (time.time() * 1000)) / 1000
            if block > 0:
                time.sleep(block)
            self.onDelay(self._workLoading.getDelayTimeValue())
        for s in self._services:
            s.close()
        pass
    def onDelay(self, delayTime):
        if delayTime > 0:
            self._logger.warning("server is overload, delay:" + delayTime + "ms")
    def close(self):
        super(SProcess, self).close()
    
