import PySimpleGUI as sg


sg.theme("GrayGrayGray")
font = ('Source Code Pro',18)

layout = [
         [sg.Text('INPUT YOUR TEXT HERE ')],
          [sg.Input(key= '-INPUT-')],
          [ sg.Text('VOLUME'),sg.Slider(range=(0, 100), 
                orientation='h', size=(50, 10), enable_events=True, key = '-VOL-', default_value= 100) ],
          [ sg.Text('Adjust Speed'),sg.Slider(range=(150, 400), 
                orientation='h', size=(50, 10), enable_events=True, key = '-SPEED-', default_value= 150) ],
          [sg.Button('Speak', bind_return_key=True), sg.Button('EXIT')],
          [sg.Text('Select Voice Type'),sg.Radio('MALE VOICE', "RADIO1", default=False, key="-RADIO1-"),sg.Radio('FEMALE VOICE', "RADIO1", default=True, key="-RADIO2-")],
           
          ]
 
window = sg.Window(" TEXT TO SPEECH APP", layout,font=font)

while True:
    event, values =window.read()

    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Speak'and values["-RADIO1-"] == True :
        import pyttsx3
        TTS=pyttsx3.init()
        input_value = values['-INPUT-']
        rate= values['-SPEED-']
        TTS.setProperty('rate',rate)
        volume = values['-VOL-'] /100
        TTS.setProperty('volume',volume)
        voices = TTS.getProperty('voices')
        TTS.setProperty('voice', voices[0].id)
        TTS.say(input_value)
        TTS.runAndWait()
    elif event == 'Speak'and values["-RADIO2-"] == True:
        import pyttsx3
        TTS=pyttsx3.init()
        input_value = values['-INPUT-']
        rate= values['-SPEED-']
        TTS.setProperty('rate',rate)
        volume = values['-VOL-'] /100
        TTS.setProperty('volume',volume)
        voices = TTS.getProperty('voices')
        TTS.setProperty('voice', voices[1].id)
        TTS.say(input_value)
        TTS.runAndWait()
    

window.close()
       




