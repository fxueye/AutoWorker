#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import json


class SysConfig(object):
    config = ""
    def __init__(self):
        pass
    @staticmethod
    def load(configPacth):
        f = open(configPacth, "a+")
        line = f.readline()
        while line:
            SysConfig.config =SysConfig.config + line.strip('\n').replace(" ","")
            line = f.readline()
        f.close() 
        SysConfig.config = json.loads(SysConfig.config)
        pass
def main():
    SysConfig.load("../../config/config.json")
    print SysConfig.config["db"]["passwd"]
if __name__ == '__main__':
    main()