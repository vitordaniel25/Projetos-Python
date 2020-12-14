from PySimpleGUI import PySimpleGUI as sg
import random

sg.theme('DarkBlue12')

layout = [
    [sg.Text('Deseja jogar o dado?', font =200)],
    [sg.Input(default_text='Sim ou Não',key= 'comando',size= (15,1), font=200), sg.Button('OK', key='botao')],
    [sg.Text('...', key='valor',size= (15,1), font = 200)]
]

janela = sg.Window('Simulador de dado', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if ((eventos =='botao')):        
        cmd = valores['comando'].lower()
        if cmd == 'sim':           
           janela['valor'].update('resultado: ' + str(random.randrange(1,7)))
        elif ((cmd == 'não') or (cmd == 'nao')):
            break
        else:
            janela['valor'].update('Valor Inválido!')