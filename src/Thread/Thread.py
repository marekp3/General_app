import time
from tkinter import W
import matplotlib.pyplot as plt
from Shared.type_defs import My_Queues

class Thread:
    def __init__(self, com, status, timeout, loop_start_time, loop_stop_time, state):
        self.com = com
        self.status = status
        self.timeout = timeout
        self.loop_start_time = loop_start_time
        self.loop_stop_time = loop_stop_time
        self.state = state

    def init(self):
        pass

    def read_decide(self, command, data):
        pass
    def read(self):
        name = self.__class__.__name__
        if name == 'sm_class':
            messege = self.com.dequeue(My_Queues.SM) 
        elif name == 'acq_class':
            messege = self.com.dequeue(My_Queues.ACQ) 
        command = messege[0]
        data = messege[1]
        self.read_decide(command, data)

    def process(self):
        pass
    def write(self):
        pass

    def close(self):
        pass

    def main(self):
        self.init()
        end_array = []
        while True:
            self.loop_start_time = time.perf_counter()
            self.read()
            self.process()
            self.write()
            if self.status:
                print(self.__class__.__name__ + "zamykam")
                break
            self.loop_stop_time = time.perf_counter()
            loop_time = self.loop_stop_time-self.loop_start_time
            time_to_sleep = self.timeout - loop_time
            if time_to_sleep > 0:
                time.sleep(time_to_sleep)
            else:
                print("houston we have a problem")
            end_time =time.perf_counter() - self.loop_start_time 
            end_array.append(end_time)
        print(self.__class__.__name__)
        plt.plot(end_array)
        plt.show()
        self.close()


        

