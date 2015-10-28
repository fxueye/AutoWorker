# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.SProcess import SProcess
from lib.Mail import Mail
from util.SysConfig import SysConfig
from main.services.MailService import MailService


class MailProc(SProcess):
    _index = None
    _logger = None
    _mail_service = None
    _time_service = None
    _mail = None
    _main_dev = None
    def __init__(self,mainDev):
        super(MailProc, self).__init__()
        self._index = 0
        self._logger = logging.getLogger(str(__name__))
        self._mail = Mail(SysConfig.config['mail']['userName'], SysConfig.config['mail']['password'])
        self._mail.setSender(SysConfig.config['mail']['sender'])
        self._mail.setSmptServer(SysConfig.config['mail']['smptserver'])
        self._mail_service = MailService(self)
        self.registerService(self._mail_service)
        self._main_dev = mainDev


        pass
    def setIndex(self, index):
        self._index = index
        pass
    def getIndex(self):
        return self._index
        pass
    def getMail(self):
        return self._mail
        pass

