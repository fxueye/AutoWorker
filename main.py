#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
from main.MainDev import MainDev

def main():
    mainDev = MainDev.GetInstance()
    mainDev.start()
if __name__ == '__main__':
    main()