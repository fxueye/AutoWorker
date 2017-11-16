# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''



from framework.Service import Service
from public.AppQueue import AppQueue
import logging
import threading
class MailService(Service):
    _logger = None
    _process = None
    mutex = threading.Lock()
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        pass
    def start(self):
        pass
    def update(self, diff, now):
        if not AppQueue.mailQueue.empty():
            maild = AppQueue.mailQueue.get()
            if maild:
                self._process.getMail().setReceiver(maild.getReceiver())
                self._process.getMail().setSubject(maild.getSubject())
                try:
                    self._process.getMail().sendTextMail(maild.getContent())
                except Exception, e:
                    print Exception, str(e)
                    AppQueue.mailQueue.put(maild)
#         self._logger.debug(self._process.getIndex())
        
#         self._logger.debug("index is %d %s"%(self._process.getIndex(), TimerUtil.timeToStr(now)))
#         self._logger.debug("index is %d %d"%(self._process.getIndex(), now))
        pass
    def close(self):
        pass
    
    
        
        
