# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.SProcess import SProcess
from main.services.CheckService import CheckService
from lib.Browser import Browser
import re
import threading




class WorkProc(SProcess):
    _logger = None
    _check_service = None
    _browser = None
    _main_dev = None
    _mutex = threading.Lock()
    def __init__(self, mainDev):
        super(WorkProc, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        self._check_service = CheckService(self)
        self.registerService(self._check_service)
        self._main_dev = mainDev
        self._browser = Browser()
        pass
    def getMainDev(self):
        return self._main_dev
        pass
    def checkData(self,numiid):
        infoUrl = "http://hws.m.taobao.com/cache/mtop.wdetail.getItemFullDesc/4.1/?data=%7B%22item_num_id%22%3A%22"+numiid+"%22%7D"
        data = self._browser.openurl(infoUrl)
        m = re.search(r'SYSTEM_ERROR',data.read())
        if m:
            self._mutex.acquire()
            self._main_dev.getDb().query("delete from ftxia_items where num_iid=%s" % (numiid))
            self._main_dev.getDb().commit()
            self._mutex.release()
            self._logger.debug("SYSTEM_ERROR:%s"%(numiid))
