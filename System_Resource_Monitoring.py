import psutil
import platform
import json
from threading import Thread, Timer
import sched, time

def getSomeSystemInfo():
    myDic={}
    myDic['time']=time.ctime()
    myDic['CPU']=psutil.cpu_times(percpu=False)
    myDic['Memory']=psutil.virtual_memory()
    myDic['Disk']=psutil.disk_usage('/')
    myDic['Network']= psutil.net_io_counters(pernic=False, nowrap=True)
    print(myDic['CPU'])
    print(myDic['Memory'])
    print(myDic['Disk'])
    print(myDic['Network'])
    with open('output.txt', 'a') as file:
        file.write(str(myDic)+'\n')

def repeatEvery5Sec():
       
    Timer(5.0, repeatEvery5Sec).start()
    getSomeSystemInfo()
    
repeatEvery5Sec()
