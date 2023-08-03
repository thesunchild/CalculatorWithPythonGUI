import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['KM to Mile', 'KG to Pound', 'Sec to Min', 'Inch to Cm'], key ='-UNITS-'),
        sg.Button('Convert', key= '-CONVERT-'),
        sg.Button('Exit', key='-EXIT-')
    ],
    [sg.Text('Output', key= '-OUTPUT-')]

]
window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break

    if event == '-CONVERT-':
            input_value = values['-INPUT-']
            if input_value.isnumeric():
                selected_unit = values['-UNITS-']
            if selected_unit == 'KM to Mile':
                output = float(input_value) * 0.6214
            elif selected_unit == 'KG to Pound':
                output = float(input_value) * 2.20462
            elif selected_unit == 'Inch to Cm':
                output = float(input_value) * 2.5
            elif selected_unit == 'Sec to Min':
                output = float(input_value) / 60
            else:
                output = 'Invalid unit selection'
            window['-OUTPUT-'].update(f'Output: {output:.2f}')


    window.close()

