from turtle import back
import PySimpleGUI as sg
import os
import sys
import time
from src.GUI.GUI_functions import switch_tab
path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))


class gui_class:
    def __init__(self, queues, timeout):
        self.timeout = timeout
        self.queues = queues
 
    def main(self):


        tab1_layout = [[sg.T('This is test station tab', size=(100,40))]]   #test_station_view
        tab2_layout = [[sg.T('This is DUTs tab')]]                          #DUTs view 
        tab3_layout = [[sg.T('This is test boards tab')]]                   #test_board view
        tab4_layout = [[sg.T('This is power supply tab')]]                  #power_supply view
        tab5_layout = [[sg.T('This is ACQ tab')],
        [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(200,200), background_color='red', key='graph')]]                           #ACQ view
        tab6_layout = [[sg.T('This is test config tab')]]                   #test_config view
        tab7_layout = [[sg.T('This is test view')]]                         #test_view


        col1 = [[sg.Button('Test_Station', size=20)],
        [sg.Button('DUTs', size=20)],
        [sg.Button('Test_Boards', size=20)],
        [sg.Button('Power_Supply', size=20)],
        [sg.Button('ACQ', size=20)],
        [sg.Button('Test_Config', size=20)],
        [sg.Button('Start_ACQ', size=20)],
        [sg.Button('Stop', size=20)],
        [sg.Exit('Exit', size=20)]]

        col2 = [[sg.TabGroup([[sg.Tab('Test_Station', tab1_layout), sg.Tab('DUTs', tab2_layout), sg.Tab('Test_Boards', tab3_layout), sg.Tab('Power_Supply', tab4_layout), sg.Tab('ACQ', tab5_layout), sg.Tab('Test_Config', tab6_layout), sg.Tab('Test', tab7_layout)]],key='tabgroup', enable_events=True)]]

        layout = [[sg.Column(col1, element_justification='c' ), sg.Column(col2, element_justification='c')]]


        window = sg.Window('Window that stays open', layout, finalize=True)
        grapg = window['graph']

        while True:
            print("Jestem w GUI")
            try:
                messege = self.queues['gui_class'].get_nowait()
                command = messege[0]
                data = messege[1]
            except:
                command = 'EMPTY'
                data = []
            if command == 'NEW_DATA':
                print(data)



            event, values = window.read(timeout = self.timeout)
            if event == sg.WIN_CLOSED or event == 'Exit':
                self.queues["sm_class"].put(['EXIT',[]])
                self.queues["acq_class"].put(['EXIT',[]])
                self.queues['gui_class'].close()
                break
            switch_tab(event, window) #Switch TAB with use of Buttons
            if event == 'Start_ACQ':
                print('START_ACQ')
                self.queues["sm_class"].put(['START_ACQ',[]])
            elif event == 'Stop':
                self.queues['sm_class'].put(['STOP_ACQ',[]])
            time.sleep(self.timeout)
        window.close()
