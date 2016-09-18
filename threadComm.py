from PyQt4 import QtCore
import time,sys
 
class Error(Exception):
    def __init__(self,error):
        self.error = error
 
    def __str__(self):
        return self.error
 
class Queue:
    def __init__(self,max_data=1024,max_buffer=1024):
        self.__buffer = []
        self.__writing = False
        self.__getting = False
        self.__max_data = max_data
        self.__max_buffer = max_buffer
 
    def __del_data_buffer(self):
        while self.len_buffer() > self.__max_buffer:
            del self.__buffer[0]
 
    def set_data(self,data):
        if self.__writing == True:
            return (False,'set_data','writing')
        elif sys.getsizeof(data) > self.__max_data:
            return (False,'set_data','size data not supported')
        else:
            if self.len_buffer() > self.__max_buffer:
                self.__del_data_buffer()
            self.__writing = True
            self.__buffer.append(data)
            self.__writing = False
            return (True,'set_data')
 
    def wait_data(self,num_loop=0,time_wait=1):
        if num_loop == 0 and time_wait > 0:
            return self.get_data(True)
        elif num_loop > 0 and time_wait > 0:
            num = 0
            while num < num_loop:
                if self.len_buffer() > 0:
                    return (True,'wait_data',self.get_data(True))
                time.sleep(time_wait)
            return(False,'wait_data',[])
        else:
            if num_loop < 0:
                raise Error('Error num_loop with signed')
            elif time_wait < 0:
                raise Error('Error time_wait with signed')
 
 
    def get_data(self,call=False):
        if self.__getting == True:
            return (False,'get_data','getting')
        self.__getting = True
        temp_buffer = self.__buffer
        self.__buffer = []
        self.__getting = False
        if call == True:
            return temp_buffer
        return (True,'get_data',temp_buffer)
 
    def len_buffer(self):
        if len(self.__buffer) > 0:
            return sys.getsizeof(self.__buffer)
        else:
            return 0
 
class Thread(QtCore.QThread):
    __error_queue = []
    def __init__(self,queues=[]):
        QtCore.QThread.__init__(self)
        for queue in queues:
            if queues[queue].__class__.__name__ == 'Queue':
                setattr(self,'_{0}'.format(queue),queues[queue])
            else:
                self.__error_queue.append("Not supported object because it is not of type Queue, object {0} class {1}".format(queue,\
                queues[queue].__class__.__name__))
        if len(self.__error_queue) > 0:
            raise Error(str(self.__error_queue))
