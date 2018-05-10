# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 08:35:00 2018

@author: Administrator
"""

import fe2
import fe3
import schedule
import time


#insertdata.insertData()



 
def job():
    print("I'm working...")
    fe2.insertData()
    print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

def job2():
        fe3.updateuse()
 
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)

def gettast():
    schedule.every().day.at("10:59").do(job)
    schedule.every().day.at("13:30").do(job)
    schedule.every().day.at("16:55").do(job)
    schedule.every().day.at("23:55").do(job2)

 
    while True:
        schedule.run_pending()
        time.sleep(1)