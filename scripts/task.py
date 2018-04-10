#coding:utf-8
from apscheduler.schedulers.background import BackgroundScheduler
import insert
def my_job():
	scheduler=BackgroundScheduler()
	scheduler.add_job(insert.tongji, 'interval', seconds=5)
	scheduler.start()


