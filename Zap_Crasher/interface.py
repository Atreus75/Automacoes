from PySimpleGUI import PySimpleGUI as sg

class Interface():
    def __init__(self):
        pass
    
    def config(self, input_text, input_background, text, text_element_background):
        # Definindo pré-configurações
        sg.theme('Reddit')
        sg.theme_input_text_color(input_text)
        sg.theme_input_background_color(input_background)
        sg.theme_text_color(text)
        sg.theme_text_element_background_color(text_element_background)
    
    
    def criarJanela(self, titulo, layout, local, color, icon):
        janela = sg.Window(title=titulo, layout=layout, location=local, background_color=color, icon=icon)
        return janela
    
    def novaJanela(self, janela, titulo = 'Zap Crasher', layout = [], local = (400, 300), cor = "#081112"):
        janela.Close()
        janela1 = sg.Window(titulo, layout, location=local, background_color=cor, icon="whatsappico_4Ui_icon.ico", finalize=True)
        janela = janela1
        return janela



    