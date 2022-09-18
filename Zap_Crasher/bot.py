from time import sleep
import pyautogui as auto
from pyperclip import copy


class Automação:
                def __init__(self, alvo, mensagem, intervalo, repetições, barraProgresso):    
                    self.alvo = alvo
                    self.mensagem = mensagem
                    self.intervalo = intervalo
                    self.repetições = repetições
                    self.barraProgresso = barraProgresso
                    copy(self.alvo)
                

                def atacar(self, espera):
                    auto.doubleClick(x=121, y=767)
                    sleep(7)
                    self.barraProgresso.Update(20)
                    auto.click(x=190, y=49)
                    auto.write('web.whatsapp.com')
                    auto.press('enter')
                    sleep(espera)
                    self.barraProgresso.Update(40)
                    auto.click(x=98, y=173)
                    auto.hotkey('ctrl', 'v')
                    auto.press('enter')
                    sleep(5)
                    copy(self.mensagem)
                    self.barraProgresso.Update(70)

                    for c in range(0, self.repetições):
                        auto.click(x=630, y=727)
                        auto.hotkey('ctrl', 'v')
                        auto.press('enter')
                        sleep(0.2)
                        c += 1
                    self.barraProgresso.Update(100)