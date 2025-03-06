#exemplos de 3 intarfaces graficas basico.
#cria uma janela basica tkinter 
print("TESTANDO TKINTER JANELA")
import tkinter
tkinter._test()

#flexx criando uma janela basica com dois botao.
print("TESTANDO FLEXX JANELA")
from flexx import flx
#cria janela
class janela_flexx(flx.Widget):
    def init(self):
        #cria botao

        flx.Button(text='BOTAO 1')
        flx.Button(text="BOTAO 2")

if __name__ == '__main__':
    #muda titulo do programa
    inicio  = flx.App(janela_flexx, title='Flexx janela')
    executar = inicio.launch()
    flx.run()
print("TESTANDO KIVY JANELA")
## usando Kivy para criar janela que é um botao
from kivy.app import App
from kivy.uix.button import Button
class BOTAO(App):
    def build(self):
        return Button(text='Novo Mundo')
if __name__ == '__main__':
   BOTAO().run()




