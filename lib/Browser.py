# -*- coding: utf-8 -*-
'''
Created on 2015年6月14日

@author: Administrator
'''
import random
import socket
import urllib2
import cookielib
class Browser(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        socket.setdefaulttimeout(20)
        cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        self._opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(self._opener)
        user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",

                    ] 
        agent = random.choice(user_agents)
        self._opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
    def openurl(self,url):
        try:
            res = self._opener.open(url)
        except Exception,e:
            print str(e)
            raise Exception
        else:
            return res    
if __name__=='__main__':
    b = Browser()
    for i in range(100):
        data = b.openurl("http://www.dianping.com/search/keyword/1/0_%E7%BA%A2%E8%B1%86%E8%96%8F%E7%B1%B3")
        print data.read()