#!/usr/bin/python
#coding:utf8
import redis
host = 'r-wz920e8cee5b8bf4.redis.rds.aliyuncs.com'
port = 6379
user = 'r-wz920e8cee5b8bf4'
pwd = 'Cdsbyxkj9527'
                #连接时通过password参数指定AUTH信息，由user,pwd通过":"拼接而成
r = redis.Redis(host=host, port=port, password=user+':'+pwd,db=1)
