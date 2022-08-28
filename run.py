def UI():
    import PySimpleGUI as sg
    import os
    sg.theme('Reddit')
    
    locations = dict([

    ('MELROSE MELROSE', '1'), ('MELROSE VOLUNTEER', '2'), ('LAKE MELROSE', '3'),
    ('CUMBERLAND VOLUNTEER', '4'), ('16 CUMBERLAND', '4'), ('PEYTON VOLUNTEER', '5'),
    ('17 CUMBERLAND', '6'), ('17 WHITE', '7'), ('17 CLINCH', '8'), ('16 CLINCH', '9'),
    ('CLINCH JAMES', '10'),
    ('16 WHITE', '11'), ('JAMES WHITE', '12'), ('CUMBERLAND JAMES', '13'),
    ('CUMBERLAND PHILLIP', '13'), ('JAMES PEYTON', '14'), ('NEYLAND', '15'),
    ('HODGES', '1'), ('FIREHOUSE', '6'), ('CANES', '6'), ('PANDA', '6'), ('STRONG', '4'),
    ('HOSKINS', '13'), ('CHAIYO', '10'), ('CLEMENT', '7'), ('STANDARD', '7'),
    ('CHIPOTLE', '6'), ('BAKER', '6'), ('ROAST', '3'), ("GUS'S", '3'), ('HOOKAH', '3'),
    ('TYSON', '3'), ('TORCHBEARER', '5'), ('CIRCLE', '5'), ('NURSING', '5'),
    ('HEARING', '14'), ('UNION', '4'), ('RONALD', '8'), ('VOLUNTEER', '12'), ('KNOX', '10'),
    ('LAW', '6'),
                     ])
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

        values[1] = locations.get(values[1])
        values[2] = locations.get(values[2])
        # casting Day to uppercase so Day can be entered as lower, upper, or a mixture and it will not change how the program runs. 
        values[3] = values[3].upper()

        # Grabbing only the first three letters of the day. 
        values[3] = values[3][:3]

        values[3] = values[3] + values[4] + '.txt'
        p = os.popen('echo {0} {1} | ./project ./trafficFiles/{2}'.format(values[1], values[2], values[3]))
        window.close()
        sg.popup(p.read(), title='Result', font=('Times 20'), image='~/Desktop/summer/project/map.png', no_titlebar=True, grab_anywhere=True)
        p.close()
UI()
