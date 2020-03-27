import threading
import time
from threading import current_thread

def mythread(arg1,arg2):
    print(current_thread().getName(),'start')
    print('%s %s'%(arg1,arg2))
    print(current_thread().getName(),'stop')

for i in range(1,5,1):
    t1=threading.Thread(target=mythread,args=(i,i+1))
    t1.start()
    # mythread(i,i+1)
print(current_thread().getName(),'end')