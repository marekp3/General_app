import imp
from multiprocessing import Process, Queue
import time
from src.SM.SM import sm_class
from src.ACQ.ACQ import acq_class
from src.GUI.GUI import gui_class
from src.Shared.type_defs import Communication, My_Queues
com = Communication()


queue_sm = Queue()
queue_acq = Queue()
queue_gui = Queue()
queues = {'sm_class': queue_sm,'acq_class': queue_acq, 'gui_class': queue_gui}

sm = sm_class(queues, False, 0.1 , 0, 0, 'IDLE')
acq = acq_class(queues, False, 0.1, 0, 0, 'IDLE')
gui = gui_class(queues, 0.1)

if __name__ == '__main__':
    sm_pr = Process(target=sm.main, args =())
    acq_pr = Process(target=acq.main, args = ())
    gui_pr = Process(target=gui.main, args = ())
    gui_pr.start()
    sm_pr.start()
    acq_pr.start()


