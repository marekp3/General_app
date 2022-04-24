from multiprocessing import Queue
import enum 
import os
import sys

queue_sm = Queue()
queue_acq = Queue()
queue_gui = Queue()

queues = {'sm_class': queue_sm,'acq_class': queue_acq, 'gui_class': queue_gui}

class My_Queues(enum.Enum):
	SM = queues['sm_class']
	AC = queues['acq_class']
	GUI = queues['gui_class']



path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))

class Communication:
	def __init__(self):
		pass
	def enqueue(self, queue_name, command, data):
		queue_name.put([command, data])
	def dequeue(self, queue_name):
		try:
			messege = queue_name.get_nowait()		
			command = messege[0]
			data = messege[1]
		except:
			messege = ['EMPTY', []]
		return messege
		

