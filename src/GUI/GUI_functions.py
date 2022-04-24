import PySimpleGUI

def test():
    print("test")

def switch_tab(event, window):    
    if event == 'Test_Station':
        window['tabgroup'].Widget.select(0)
    elif event =='DUTs':
        window['tabgroup'].Widget.select(1)
    elif event == 'Test_Boards':
        window['tabgroup'].Widget.select(2)
    elif event == 'Power_Supply':
        window['tabgroup'].Widget.select(3)
    elif event == 'ACQ':
        window['tabgroup'].Widget.select(4)
    elif event == 'Test_Config':
        window['tabgroup'].Widget.select(5)
    elif event == 'Start_ACQ':
        window['tabgroup'].Widget.select(6)
