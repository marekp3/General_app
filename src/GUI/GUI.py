from turtle import back
import PySimpleGUI as sg
import os
import sys
import time
from GUI.GUI_functions import switch_tab
from GUI.GUI_interface import window
from Shared.type_defs import My_Queues
path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))


class gui_class:
	def __init__(self, com, timeout):
		self.timeout = timeout
		self.com = com

	def main(self):
		while True:
			try:
				messege = self.com.dequeue(My_Queues.GUI)
				command = messege[0]
				data = messege[1]
			except:
				command = 'EMPTY'
				data = []
			if command == 'NEW_DATA':
				print(data)



			event, values = window.read(timeout = self.timeout)
			print(event)
			if event == sg.WIN_CLOSED or event == 'Exit':
				self.com.enqueue(My_Queues.SM,'EXIT',[])
				self.com.enqueue(My_Queues.ACQ,'EXIT',[])
				self.com.close(My_Queues.GUI)
				break
			elif event == '__TIMEOUT__':
				print("Timeot man i have nothing to do")
			switch_tab(event, window) #Switch TAB with use of Buttons
			if event == 'Start_ACQ':
				print('START_ACQ')
				self.com.enqueue(My_Queues.SM,'START_ACQ',[])
			elif event == 'Stop':
				self.com.enqueue(My_Queues.SM,'STOP_ACQ',[])
				time.sleep(self.timeout)
		window.close()
