import sys
import os
from tkinter import W
path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))

from Shared.type_defs import*
from Thread.Thread import Thread
class acq_class(Thread):
    def __init__(self, queues, status, timeout, loop_start_time, loop_stop_time, state):
        super().__init__(queues, status, timeout, loop_start_time, loop_stop_time, state)
    def write(self):
        pass
    def read_decide(self, command, data):
        if command == 'EXIT':
            self.status = True
        elif command == 'EMPTY':
            pass
        elif command == 'START_ACQ':
            self.state = 'ACQ'
        elif command == 'STOP_ACQ':
            self.state = 'IDLE'
        else:
            print(self.__class__.__name__ + "nie rozumie kokendy: ", command)


    def process(self):
        if self.state =='ACQ':
            self.queues['gui_class'].put(['NEW_DATA', [1,2,3,4,5,6,7,8,9,10]])
            print("data feed")
        elif self.state =='IDLE':
            pass
