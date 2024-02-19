import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_teste = '1234'
        usuario_teste = 'leonardo' and 'Leonardo'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_teste and usuario == usuario_teste:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Senha ou usuário incorreto')
