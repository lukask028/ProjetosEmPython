# Simulador de dados

# Simular o uso de um dado, gerando um valor de 1 até 6
# cria o _init_ com as configurações iniciais do projeto

import random
import PySimpleGUI as sg

class simuladorDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Quer jogar o dado ?'
        
        
        #Layout
        self.layout = [
            [sg.Text('jogar o dado?')],
            [sg.Button('sim'), sg.Button('Não')]
            ]
         
    def Iniciar(self):
        
        # Criar uma janela
        self.janela = sg.Window('simulador de dado', layout = self.layout)
        
        # Ler os valores 
        self.eventos, self.valores = self.janela.Read()
        # Fazer algo com os valores
        try:
                    
            if self.eventos == 'sim' or self.eventos == 's':
                self.ValordoDado()
                
            elif self.eventos == 'Não' or self.eventos == 'n':
                print("Obrigado pela participação")
                
            else:
                print("Digitar sim ou nao")
        except:
                print("ocorreu um erro ao receber a resposta") 
            
            
        
                      
    def ValordoDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))
        
simulador = simuladorDado()
simulador.Iniciar()