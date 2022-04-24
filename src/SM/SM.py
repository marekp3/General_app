from asyncio import queues
import sys
import os
path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))

from Thread.Thread import Thread
class sm_class(Thread):
    def __init__(self, queues, status, timeout, loop_start_time, loop_stop_time, state):
        super().__init__(queues, status, timeout, loop_start_time, loop_stop_time, state)
    
    def read_decide(self, command, data):
        if command == 'EXIT':
            self.status = True
        elif command == 'EMPTY':
            pass
        elif command == 'START_ACQ':
            self.queues['acq_class'].put(['START_ACQ',[]])
        elif command == 'STOP_ACQ':
            self.queues['acq_class'].put(['STOP_ACQ',[]])
        else:
            print(self.__class__.__name__ + "nie rozumie kokendy: ", command)

