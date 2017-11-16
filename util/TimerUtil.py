# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import time
class TimerUtil(object):
    SECOND_MILLS = 1000L;
    MINUTE_MILLS = SECOND_MILLS * 60;
    HOUR_MILLS = MINUTE_MILLS * 60;
    HALF_DAY_MILLS = HOUR_MILLS * 12;
    DAY_MILLS = HOUR_MILLS * 24;
    def __init__(self):
        pass
    @staticmethod
    def minuteToMills(minute):
        return TimerUtil.MINUTE_MILLS * minute 
        pass
    @staticmethod
    def secondToMills(second):
        return TimerUtil.SECOND_MILLS * second
        pass
    @staticmethod
    def setTimeZone(self, zoneID):
        pass
    @staticmethod
    def millsToSecond(mills):
        return (mills / TimerUtil.SECOND_MILLS)
        pass
    @staticmethod
    def timeToStr(mills):
        tup_birth = time.localtime(TimerUtil.millsToSecond(mills))
        format_birth = time.strftime("%Y-%m-%d %H:%M:%S", tup_birth)
        return format_birth
    @staticmethod
    def strToTime(format_birth):
        tup_birth = time.strptime(format_birth, "%Y-%m-%d %H:%M:%S");
        birth_secds = time.mktime(tup_birth)
        return birth_secds
        pass
def main():
    print TimerUtil.minuteToMills(5)
if __name__ == '__main__':
    main()
