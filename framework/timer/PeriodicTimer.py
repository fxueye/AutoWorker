# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
class PeriodicTimer(object):
    _period = 0
    _expire_time = 0
    def __init__(self, period):
        self._period = period
        self._expire_time = self._period
        pass
    def update(self, millis):
        self._expire_time = self._expire_time - millis
        if self._expire_time > 0:
            return False
        addMillis = 0
        if self._period > millis:
            addMillis = self._period
        else:
            addMillis = millis
        self._expire_time = self._expire_time + addMillis
        return True
        pass
    def getPeriod(self):
        return self._period