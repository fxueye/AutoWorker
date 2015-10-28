#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
class WorkLoading(object):
    _workTime = 0
    _delayTime = 0
    _totalTimes = 0
    _delayTimes = 0
    _maxDelayTime = 0
    def __init__(self, startTime):
        self._workTime = startTime
    def getWorkTime(self):
        return self._workTime
    def getDelayTimeValue(self):
        return self._delayTime;
    def setWorkTime(self, workTime):
        self._workTime = workTime
    def updateWorkTime(self, deltaMS, now):
        self._workTime = self._workTime + deltaMS
        if (now - self._workTime) <= 0:
            self._delayTime = 0
        else:
            self.delayTime = now - self._workTime
        self._totalTimes = self._totalTimes + 1
        if self._delayTime > 0:
            if self._maxDelayTime > self._delayTime:
                self._maxDelayTime = self._maxDelayTime
            else:
                self._maxDelayTime = self._delayTime
        ret = 0
        if self._workTime - now > 0:
            ret = self._workTime - now
        return ret
        
        

        
