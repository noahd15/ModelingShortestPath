def UI():
    import PySimpleGUI as sg
    import os
    sg.theme('Reddit')
    while True:
        layout = [  [sg.Image('~/Desktop/summer/project/map.png')],
                [sg.Text('Enter starting location:', size=(20,1), font=('Times 15')), sg.InputText(font=('Times 15'))],
                [sg.Text('Enter destination:', size=(20,1), font=('Times 15')), sg.InputText(font=('Times 15'))],
                [sg.Text('Day:', size=(20,1), font=('Times 15')), sg.InputText(font=('Times 15'))],
                [sg.Text('Time in military:', size=(20,1), font=('Times 15')), sg.InputText(font=('Times 15'))],
                [sg.Button('Enter', size=(30,1), font=('Times 15'),bind_return_key=True), sg.Button('Cancel', size=(30,1), font=('Times 15'))]]
        window = sg.Window('Shortest Path', layout,element_justification='c')



        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            return

        values[1] = values[1].upper()
        values[2] = values[2].upper()
        # casting Day to uppercase so Day can be entered as lower, upper, or a mixture and it will not change how the program runs. 
        values[3] = values[3].upper()

        # Grabbing only the first three letters of the day. 
        values[3] = values[3][:3]

        values[3] = values[3] + values[4] + '.txt'
        p = os.popen('echo {0} {1} | ~/Desktop/summer/project/bin/project ~/Desktop/summer/project/trafficfiles/{2}'.format(values[1], values[2], values[3]))
        window.close()
        sg.popup(p.read(), title='Result', font=('Times 20'), image='~/Desktop/summer/project/map.png', no_titlebar=True, grab_anywhere=True)
        p.close()
UI()
