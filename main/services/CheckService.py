# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''



from framework.Service import Service
from public.AppQueue import AppQueue
import logging
class CheckService(Service):
    _logger = None
    _process = None
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        pass
    def start(self):
        pass
    def update(self, diff, now):
        if not AppQueue.numiidQueue.empty():
            numiid = AppQueue.numiidQueue.get()
            if numiid:
                try:
                    self._process.checkData(numiid)
                except Exception, e:
                    print Exception, str(e)
                    AppQueue.numiidQueue.put(numiid)
        pass
    def close(self):
        pass
    
    
        
        