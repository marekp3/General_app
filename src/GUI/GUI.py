from turtle import back
import PySimpleGUI as sg
import os
import sys
import time
from GUI.GUI_functions import switch_tab
from Shared.type_defs import My_Queues
path = os.path.dirname(os.path.dirname( __file__ ))
sys.path.insert(0,str(path))
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

_VARS = {'window': False,
	 'fig_agg': False,
	 'pltFig' : False,
	 'dataSize': 60}

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

AppFont = 'Any 16'
SliderFont = 'Any 14'
sg.theme('black')

class gui_class:
    def __init__(self, com, timeout):
        self.timeout = timeout
        self.com = com
 
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
                messege = self.com.dequeue(My_Queues.GUI)
                command = messege[0]
                data = messege[1]
            except:
                command = 'EMPTY'
                data = []
            if command == 'NEW_DATA':
                print(data)



            event, values = window.read(timeout = self.timeout)
            if event == sg.WIN_CLOSED or event == 'Exit':
                self.com.enqueue(My_Queues.SM,'EXIT',[])
                self.com.enqueue(My_Queues.ACQ,'EXIT',[])
                self.com.close(My_Queues.GUI)
                break
            switch_tab(event, window) #Switch TAB with use of Buttons
            if event == 'Start_ACQ':
                print('START_ACQ')
                self.com.enqueue(My_Queues.SM,'START_ACQ',[])
            elif event == 'Stop':
                self.com.enqueue(My_Queues.SM,'STOP_ACQ',[])
            time.sleep(self.timeout)
        window.close()
