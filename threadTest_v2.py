import threading
from threading import current_thread

class mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        print(current_thread().getName(),'stop')

# for i in range(1,5,1):
#     t1=mythread()
#     t1.start()
#     # mythread(i,i+1)
#     t1.join()
t2=mythread()
t2.start()
t2.join()
print(current_thread().getName(),'end')