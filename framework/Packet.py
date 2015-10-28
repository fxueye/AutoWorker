# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年7月15日
@author: QQ:281431280
'''
import struct


class Packet(object):
    BYTE = [0, 1, 'b']
    BOOL = [1, 1, '?']
    SHORT = [2, 2, 'h']
    INT = [3, 4, 'i']
    LONG = [4, 4, 'l']
    LLONG = [5, 8, 'q']
    FLOAT = [6, 4, 'f']
    DOUBLE = [7, 8, 'd']
    STRING = [8, 0, 's']
    _buffer = None
    _types = None
    _position = None
    _mode = None
    def __init__(self):
        self._buffer = b""
        self._types = []
        self._position = 0
        self._mode = 0
        pass
    def addBytes(self, b):
        self._beforeAdd()
        self._types.append(self.BYTE)
        self._buffer = self._buffer + struct.pack('b', b)
        pass
    def popBytes(self):
        buff = self._buffer[0:1]
        self._buffer = self._buffer[1:len(self._buffer)]
        return struct.unpack('b', buff)[0]
        pass
    def addBool(self, b):
        self._beforeAdd()
        self._types.append(self.BOOL)
        self._buffer = self._buffer + struct.pack('?', b)
        pass
    def popBool(self):
        return self.unpack(Packet.BOOL)
        pass
    def addShort(self, h):
        self._beforeAdd()
        self._types.append(self.SHORT)
        self._buffer = self._buffer + struct.pack('h', h)
        pass
    def popShort(self):
        return self.unpack(Packet.SHORT)
        pass
    def addInt(self, i):
        self._beforeAdd()
        self._types.append(self.INT)
        self._buffer = self._buffer + struct.pack('i', i)
        pass    
    def popInt(self):
        return self.unpack(Packet.INT)
    def addLong(self, l):
        self._beforeAdd()
        self._types.append(self.LONG)
        self._buffer = self._buffer + struct.pack('l', l)
        pass
    def popLong(self):
        return self.unpack(Packet.LONG)
    def addlLong(self, ll):
        self._beforeAdd()
        self._types.append(self.LLONG)
        self._buffer = self._buffer + struct.pack('q', ll)
        pass
    def poplLong(self):
        return self.unpack(Packet.LLONG)
    def addFloat(self, f):
        self._beforeAdd()
        self._types.append(self.FLOAT)
        self._buffer = self._buffer + struct.pack('f', f)
        pass
    def popFloat(self):
        return self.unpack(Packet.FLOAT)
    def addDouble(self, d):
        self._beforeAdd()
        self._types.append(self.DOUBLE)
        self._buffer = self._buffer + struct.pack('d', d)
        pass
    def popDouble(self):
        return self.unpack(Packet.DOUBLE)
    def addString(self, s):
        self._beforeAdd()
        self._types.append(self.STRING)
        formats = "%ss"%(len(s))
        l = struct.calcsize(formats)
        self.addShort(l)
        self._buffer = self._buffer + struct.pack(formats, s)
        pass
    def popString(self):
        length = self.popShort()
        buff = self._buffer[0:length]
        formats = "%ss"%(length)
        return struct.unpack(formats, buff)[0]
        pass
    def setBuffer(self, buffers):
        self._buffer = buffers
        pass
    def getBuffer(self):
        return self._buffer
        pass
    def unpack(self, t):
        buff = self._buffer[0:t[1]]
        self._buffer = self._buffer[t[1]:len(self._buffer)]
        return struct.unpack(t[2], buff)[0]
        pass
    def flip(self):
        self._mode = 1
        self._types.reverse()
        self._position = 0
        pass
    def _beforeAdd(self):
        if self._mode == 1:
            self._mode = 0
            self._types.reverse()
