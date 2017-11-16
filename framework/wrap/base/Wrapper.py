#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年7月17日
@author: QQ:281431280
'''
from abc import abstractmethod
class Wrapper(object):
    def __init__(self):
        pass
    @abstractmethod
    def encode(self,pack):
        pass
    @abstractmethod
    def decode(self,pack):
        pass
    def getValue(self):
        return self
        pass