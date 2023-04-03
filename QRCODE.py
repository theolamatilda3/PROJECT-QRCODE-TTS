import PySimpleGUI as sg
import qrcode

sg.theme("GrayGrayGray")
font = ('Source Code Pro',18)

qr_image= [sg.Image('',key ='-QRCODE-')]

layout = [
     [sg.Text('INPUT TEXT OR LINK')],
     [sg.Input('',key='-INPUT-')],
     [sg.Button('CREATE QRCODE', key='-CREATE-'), sg.Button('EXIT')],
     [sg.Column([qr_image], justification='center')]
             
]
 
window = sg.Window("QR CODE GENERATOR", layout,font=font)

while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event =='-CREATE-':
        text = values['-INPUT-']
        if text:
            image = qrcode.make(text)
            image.save('qr.png')
            window['-QRCODE-'].update('qr.png')

window.close()