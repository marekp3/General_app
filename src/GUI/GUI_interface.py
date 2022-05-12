import PySimpleGUI as sg
tab1_layout = [[sg.T('This is test station tab', size=(100,40))]]   #test_station_view
tab2_layout = [[sg.T('This is DUTs tab')]]                          #DUTs view 
tab3_layout = [[sg.T('This is test boards tab')]]                   #test_board view
tab4_layout = [[sg.T('This is power supply tab')]]                  #power_supply view
tab5_layout = [[sg.T('This is ACQ tab')]]
tab6_layout = [[sg.T('This is test config tab')]]                   #test_config view
tab7_layout = [[sg.T('This is test view')], [sg.In(key='Queue_elements_SM')]]                         #test_view


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

