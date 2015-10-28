# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月24日
@author: QQ:281431280
'''
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


class Mail(object):
    _sender = None
    _receiver = None
    _subject = None
    _smpt_server = None
    _user_name = None
    _password = None
    _smtp = None
    def __init__(self, username, password):
        self._sender = None
        self._receiver = []
        self._subject = None
        self._smpt_server = None
        self._user_name = username
        self._password = password
        self._smpt = SMTP()
        pass
    def setSubject(self, subject):
        self._subject = subject
        pass
    def setSmptServer(self, smptServer):
        self._smpt_server = smptServer
        pass
    def setReceiver(self, receiver):
        self._receiver = receiver
        pass
    def setSender(self, sender):
        self._sender = sender
        pass
    def connect(self):
        self._smpt.connect(self._smpt_server)
        pass
    def login(self):
        self._smpt.login(self._user_name, self._password)
        pass
    def sendTextMail(self, msgs):
        self.connect()
        self.login()
        msg = MIMEText(msgs, _charset='utf-8')
        msg['Subject'] = Header(self._subject, 'utf-8')
        msg['From'] = self._sender
        msg['to'] = ';'.join(self._receiver) 
        self._smpt.sendmail(self._sender, self._receiver, msg.as_string())
        self.quit()
        pass
    def sendHtmlMail(self, msg):
        self.connect()
        self.login()
        msg = MIMEText(msg, 'html', 'utf-8')
        msg['Subject'] = Header(self._subject, 'utf-8')
        self._smpt.sendmail(self._sender, self._receiver, msg.as_string())
        pass
    def quit(self):
        self._smpt.quit()
        pass
class MailD():
    _uid = None
    _content = None
    _subject = None
    _receiver = None
    def __init__(self, uid, sub, content):
        self._content = content
        self._subject = sub
        self._uid = uid
        self._receiver = []
        pass
    def getContent(self):
        return self._content
        pass
    def getUid(self):
        return self._uid
        pass
    def getReceiver(self):
        return self._receiver
        pass
    def setSubject(self, subject):
        self._subject = subject
        pass
    def getSubject(self):
        return self._subject
        pass
    def setReceiver(self, receiver):
        self._receiver = receiver
        pass
        
    def addReceiver(self, receiver):
        self._receiver.append(receiver)
        pass
def main():
    mail = Mail("568669736@qq.com","skw0103")
    mail.setSender("568669736@qq.com")
    mail.setSmptServer("smtp.qq.com")
    mail.setSubject("title")
    mail.setReceiver(["281431280@qq.com"])
    mail.sendTextMail("你好")
#     mail.sendHtmlMail("<a href='http://baidu.com'>1111111111111111</a>")
    pass
if __name__ == '__main__':
    main()
