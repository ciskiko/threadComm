from threadComm import Thread,Queue
import time
 
 #set queue
class th(Thread):
    def __init__(self,**queues):
        Thread.__init__(self,queues)
 
    def run(self):
        for i in range(15):
            self._com.set_data(i+1)
            time.sleep(1)
#get Queue
class th2(Thread):
    def __init__(self,**queues):
        Thread.__init__(self,queues)
 
    def run(self):
        n = 0
        while n != 15:
            print "N value: "+str(n)
            data = self._q.wait_data(3,1)
            if data[0] == True:
                n = data[2]
 
#simple example
q = Queue()
 
t = th(com=q)
t2 = th2(q=q)
 
t.start()
t2.start()
 
for i in range(17):
    print "thread main: "+str(i)
    time.sleep(1)
'''
output:
thread main: 0
N value: 0
N value: [1]
thread main: 1
N value: [2]
thread main: 2
N value: [3]
thread main: 3
N value: [4]
thread main: 4
N value: [5]
thread main: 5
N value: [6]
thread main: 6
N value: [7]
thread main: 7
N value: [8]
thread main: 8
N value: [9]
thread main: 9
N value: [10]
thread main: 10
N value: [11]
thread main: 11
N value: [12]
thread main: 12
N value: [13]
thread main: 13
N value: [14]
thread main: 14
N value: [15]
thread main: 15
thread main: 16
