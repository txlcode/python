#!/usr/bin/env python
# encoding:utf-8
  
import os
import datetime
import logging
from pyinotify import WatchManager, Notifier, \
ProcessEvent,IN_DELETE, IN_CREATE,IN_MODIFY
  
class EventHandler(ProcessEvent):
 logging.basicConfig(level=logging.INFO,filename='/var/log/monitor.log')
    #自定义写入那个文件，可以自己修改
 logging.info("Starting monitor...")
 
 """事件处理"""
 def process_IN_CREATE(self, event):
	print "CREATE event:", event.pathname
	logging.info("CREATE event : %s  %s" % (os.path.join(event.path,event.name),datetime.datetime.now()))
	newdir=event.path.replace('test','test1')
	if not os.path.isdir(newdir):
        	os.makedirs(newdir)
	newfile= newdir + "/" + "bjh_" + event.name
	copyCommand='\cp' + " " +'-f' + " " +event.pathname + " " + newfile
	replaceCommand = 'sed' + " " + '-i' + " " + "'s#<section id=\"async-iframe\"></section>#<br>#g'" + " " + newfile
	if os.system(copyCommand)==0:
		os.system(replaceCommand)
 def process_IN_DELETE(self, event):
	print "DELETE event:", event.pathname
   	logging.info("DELETE event : %s  %s" % (os.path.join(event.path,event.name),datetime.datetime.now()))
	newdir=event.path.replace('test','test1')
	newfile= newdir + "/" + "bjh_" + event.name
	os.system('rm' + " " + "-rf " + newfile)
 def process_IN_MODIFY(self, event):
   	print "MODIFY event:", event.pathname
   	logging.info("MODIFY event : %s  %s" % (os.path.join(event.path,event.name),datetime.datetime.now()))
	newdir=event.path.replace('test','test1')
        if not os.path.isdir(newdir):
                os.makedirs(newdir)
        newfile= newdir + "/" + "bjh_" + event.name
        copyCommand='\cp' + " " +  "-f" + " " + event.pathname + " " + newfile
        replaceCommand = 'sed' + " " + '-i' + " " + "'s#<section id=\"async-iframe\"></section>#<br>#g'" + " " + newfile
        if os.system(copyCommand)==0:
                os.system(replaceCommand) 
def FSMonitor(path='.'):
	wm = WatchManager() 
  	mask = IN_DELETE | IN_CREATE |IN_MODIFY
  	notifier = Notifier(wm, EventHandler())
  	wm.add_watch(path, mask,auto_add=True,rec=True)
  	print 'now starting monitor %s'%(path)
  	while True:
   		try:
     			notifier.process_events()
     			if notifier.check_events():
       				notifier.read_events()
   		except KeyboardInterrupt:
     			notifier.stop()
     			break
  
if __name__ == "__main__":
	FSMonitor('/tmp/test')
 
