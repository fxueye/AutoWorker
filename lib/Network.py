# -*- coding: utf-8 -*-
'''
Created on 2015年6月14日

@author: Administrator
'''
import copy
import httplib
import urllib
import urllib2


class Network(object):
    '''
    classdocs
    '''
    _url =""

    def __init__(self, url):
        '''
        Constructor
        '''
        self._url = url
    def _http_send(self, method, url_path, ec_params):

        uri = 'http://%s%s' % (self._url, url_path)
        
        if method.lower() == 'post':
            data = urllib2.urlopen(uri,ec_params).read()
        elif method.lower() == 'get':
            if ec_params:
                dest_url = '%s?%s' % (uri, ec_params)
            else:
                dest_url = uri
            data = urllib2.urlopen(dest_url).read()
        else:
            raise TypeError, 'method invalid:%s' % method

        return data   
    def _https_send(self, method, url_path, ec_params):
        conn = httplib.HTTPSConnection(self._url)

        method = method.upper()

        if method == 'GET':
            url = '%s?%s' % (url_path, ec_params)
            conn.request(method, url)
        else:
            conn.request(method, url_path, ec_params)

        rsp = conn.getresponse()

        if rsp.status != 200:
            raise ValueError, 'status:%d' % rsp.status
        data = rsp.read()

        return data    
    def _mk_send_data(self, params):

        ec_params = urllib.urlencode(params)

        return ec_params
    def open(self, method, url_path, params, protocol='http'):
        ec_params = self._mk_send_data(copy.deepcopy(params))

        if protocol == 'http':
            data = self._http_send(method, url_path, ec_params)
        elif protocol == 'https':
            data = self._https_send(method, url_path, ec_params)
        else:
            raise TypeError,'protocol invalid:%s' % protocol

        return data
    