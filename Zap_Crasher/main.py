from PySimpleGUI import PySimpleGUI as sg
from interface import Interface
from bot import Automação

# Instânciando e configurando interface gráfica
interface = Interface()
interface.config('#00ff0d', '#13282b', '#00ff0d', '#081112')

# Criando layout da janela
layout = [
    [sg.Text('Alvo:                    '), sg.Input(key='alvo', border_width=0)],
    [sg.Text('Mensagem:          '), sg.Multiline(key='mensagem', border_width=0)],
    [sg.Text('Intervalo: (Em segundos)'), sg.Input(key='intervalo', border_width=0)],
    [sg.Text('Repetições:                   '), sg.Input(key='repetições', border_width=0), sg.Button(' Atacar ', mouseover_colors="red", border_width=0, button_color='#000000')]
    ]


# Criando a janela
janela = interface.criarJanela(titulo='Zap Cracher', layout=layout, local=(400, 300), color="#081112", icon="whatsappico_4Ui_icon.ico")


# Ler os eventos e validar entradas
while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    elif eventos == ' Atacar ':
        invalido = valores['alvo'] == "" or valores['mensagem'] == "" or valores['intervalo'] == "" or valores['repetições'] == "" or valores['intervalo'].isnumeric() == False or valores['repetições'].isnumeric() == False
        
        if invalido == True:
            layout = layout.append([sg.Text('*Insira as Informações Corretamente*', text_color='red')])
            janela = interface.novaJanela(janela, layout=layout)
            print('Preencha as informações corretamente.')
        else:
            alvo = valores['alvo']
            msg = valores['mensagem']
            intervalo = float(valores['intervalo'])
            repetições = int(valores['repetições'])
            layout = [
                [sg.Text('Alvo:                    '), sg.Input(key='alvo', border_width=0)],
                [sg.Text('Mensagem:          '), sg.Multiline(key='mensagem', border_width=0)],
                [sg.Text('Intervalo: (Em segundos)'), sg.Input(key='intervalo', border_width=0)],
                [sg.Text('Repetições:                   '), sg.Input(key='repetições', border_width=0), sg.Button(' Atacar ', mouseover_colors="red", border_width=0, button_color='#000000')],
                [sg.Text('\n\nAtaque em progresso... Pressione CTRL para interromper')],
                [sg.ProgressBar(max_value=100, orientation='h', size=(20, 10), key='progress')],
                ]
            janela = interface.novaJanela(janela, layout=layout)
            progresso = janela['progress']

        try:
            zap = Automação(alvo=alvo, mensagem=msg, intervalo=intervalo, repetições=repetições, barraProgresso=progresso)
            zap.atacar(30)
        except:
            break