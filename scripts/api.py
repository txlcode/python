#!/usr/bin/python
#coding:utf8
# 导入相应包
import random
import datetime
import myredis
import datetime
from flask import jsonify
from flask import Flask
app = Flask(__name__)
r=myredis.r
@app.route("/user/<age>")
def user(age):		
	return r.get('age_'+str(age))
@app.route("/time")
def time1():
	return r.get('time')
@app.route("/hello", methods=['GET', ])
def hello():
	return jsonify(msg="hello world!")
if __name__ == '__main__':
    app.run(debug=True)
    # startapp()

