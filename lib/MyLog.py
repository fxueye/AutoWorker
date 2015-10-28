# -*- coding: utf-8 -*-
'''
Created on 2014年10月16日
@author: skw QQ:281431280
'''
import logging
import os
import time
LOG_PATH = 'log/'
class MyLog(object):
    def __init__(self,classname,logname="app"):
        self.logger=logging.getLogger(classname)
        self.logger.setLevel(logging.DEBUG)
        logpath=LOG_PATH+'%s/%s.log'%(time.strftime("%Y-%m-%d",time.localtime()),logname)
        path = os.path.dirname(logpath)
        if not os.path.exists(path):
            os.makedirs(path)
        filehandler=logging.FileHandler(logpath)
        streamhandler=logging.StreamHandler()
        streamhandler.setLevel(logging.DEBUG)
        fomatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] : %(message)s')
        filehandler.setFormatter(fomatter)
        streamhandler.setFormatter(fomatter)
        self.logger.addHandler(filehandler)
        self.logger.addHandler(streamhandler)
    def debug(self,message):
        self.logger.debug(message)
    def error(self,message):
        self.logger.error(message)
        
        
            