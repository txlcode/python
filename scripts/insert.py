#!/usr/bin/python
#coding:utf8
# 导入相应包
import mymongodb
import random
import datetime
import myredis
import datetime
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
r=myredis.r
collection=mymongodb.mongodb()
def tongji():
	time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	first_name = ["陈","张","李","王","赵"]
	second_name = ["冰","鑫","程","爱","暖"]
	third_name = ["强","国","明","风","芬"]
	data = [
	    {"name":random.choice(first_name)+
	            random.choice(second_name)+
	            random.choice(third_name),
	     "age":random.randint(16,60),
	     "high":random.randint(170,190),
	     "list":list(random.randint(1,200) for i in range(10)),
	     "create_time":datetime.datetime.utcnow()
	    } for i in range(100)
	]
	try:
	    for record in data:
	        collection.insert(record)
	#except pymongo.errors.DuplicateKeyError:
	#    print('record exists')
	except Exception as e:
	    print(e)
	r.incr("oper_num")
	r.set('time',str(time))
	ages=collection.aggregate([{"$group":{ "_id":"$age","count":{"$sum":1}}},{'$sort':{'_id':1}}])
	for age in ages:
		nianling=age['_id']
		num=age['count']
		r.set(('age_'+str(nianling)),int(num))
		r.expire(('age_'+str(nianling)), 86400)
if __name__ == '__main__':
	tongji()
