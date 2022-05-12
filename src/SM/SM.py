import sys
import os
path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))

from Thread.Thread import Thread
from Shared.type_defs import My_Queues
class sm_class(Thread):
    def __init__(self, com, status, timeout, loop_start_time, loop_stop_time, state):
        super().__init__(com, status, timeout, loop_start_time, loop_stop_time, state)
    
    def read_decide(self, command, data):
        if command == 'EXIT':
            self.status = True
        elif command == 'EMPTY':
            pass
        elif command == 'START_ACQ':
            self.com.enqueue(My_Queues.ACQ,'START_ACQ',[])
        elif command == 'STOP_ACQ':
            self.com.enqueue(My_Queues.ACQ,'STOP_ACQ',[])
        elif command == 'NEW_DATA':
            self.com.enqueue(My_Queues.GUI,'NEW_DATA',data)
        else:
            print(self.__class__.__name__ + "nie rozumie kokendy: ", command)

