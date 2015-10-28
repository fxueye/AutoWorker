# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月17日
@author: QQ:281431280
'''
from framework.SDevice import SDevice
from main.process.MainProc import MainProc
from util.SysConfig import SysConfig
import logging
import threading
from main.process.MailProc import MailProc
from main.process.WorkProc import WorkProc
from lib.Mysql import Mysql
from public.AppQueue import AppQueue
class MainDev(SDevice):
    _logger = None
    _main_proc = None
    _mail_procs = None
    _work_procs = None
    _db = None
    instance = None
    mutex = threading.Lock()
    def __init__(self):
        super(MainDev, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        interval = SysConfig.config["servers"]["interval"]
        if not  interval:
            interval = 200
        self._main_proc = MainProc(self)
        self.addProcess(self._main_proc, interval)
        mailProcCount = SysConfig.config["mail"]["mailProcCount"]
        self._mail_procs = []
        for i in range(mailProcCount):  
            mailProc = MailProc(self)
            mailProc.setIndex(i)
            self._mail_procs.append(mailProc)
            self.addProcess(mailProc, interval)
        self._work_procs = []
        workProcCount = SysConfig.config['servers']['workProcCount']
        for i in range(workProcCount):
            workProc = WorkProc(self)
            self._work_procs.append(workProc)
            self.addProcess(workProc, interval)
        host = SysConfig.config['db']['host']
        port = SysConfig.config['db']['port']
        user = SysConfig.config['db']['user']
        passwd = SysConfig.config['db']['passwd']
        dbName = SysConfig.config['db']['db']
        charset = SysConfig.config['db']['charset']
        self._db = Mysql(host, port, user, passwd, dbName, charset)
        pass
        
    @staticmethod
    def GetInstance():
        if(MainDev.instance == None):
            MainDev.mutex.acquire()
            if(MainDev.instance == None):
                MainDev.instance = MainDev()
            MainDev.mutex.release()
        return MainDev.instance
        pass
    def getMainProc(self):
        return self._main_proc
        pass
    def getRedis(self):
        return self._redis
        pass
    def start(self):
        super(MainDev, self).start()
        row = self._db.query("select num_iid from ftxia_items order by id desc")
        for r in row:
            AppQueue.numiidQueue.put(r[0])
        self._logger.debug("numiid count %d"%(AppQueue.numiidQueue.qsize()))
        self._logger.debug("server start ........")
    def close(self):
        self._logger.debug("server close ........")
        super(MainDev,self).close()
        self._db.close()
    def getDb(self):
        return self._db
    def getFactory(self):
        return self._factory
        pass
