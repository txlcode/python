#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from api import app

# 实例化
manager = Manager(app)

# 修饰器
@manager.command
def hello():
    print 'hello world'

@manager.option('-m', '--msg', dest='msg_val', default='world')
def hello_world(msg_val):
    print 'hello ' + msg_val

if __name__ =="__main__":
    manager.run()

