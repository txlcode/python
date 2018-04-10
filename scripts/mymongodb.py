#!/usr/bin/python
#coding:utf8
# 导入相应包
from pymongo import MongoClient
def mongodb():
	# 建立数据库连接
	client = MongoClient('localhost',27017)
	# 连接目标数据库
	db = client.test
	# 连接集合
	db.authenticate("db-test", "secret")
	return db.col
