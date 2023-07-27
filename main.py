# importação das bibliotecas 
from tkinter import * 
from tkinter import ttk

# cores
cor_cinza = "#545659" 
cor_branca = "#ffffff" 
cor_verde = "#298730"
cor_verde_claro = "#5cff68"
cor_verde_escuro = "#152616"
cor_verde_cinza_claro = "#b0d4b2"

# criação da janela e faz configurações 
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x314")
janela.config(bg= cor_cinza)


# criação de frames
frame_tela = Frame(janela, width= 300, height= 56, bg = cor_cinza)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 300, height= 340)
frame_corpo.grid(row=1 , column =0)


todos_valores = ''

# criando função para passar valor pra tela
def entrar_valores(e):
    
    global todos_valores 
    
    todos_valores = todos_valores + str(e)
    
    
    # passa valor para a tela 
    valor_texto.set(todos_valores)
    

# função calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    
# funcao para limpar tela 
def limpa_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')
    
    
# criando label 
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable= valor_texto, width = 16, height = 2, padx= 7, relief = FLAT, anchor= "e", justify = RIGHT, font= ('Ivy 18'), bg = cor_verde_escuro, fg = cor_branca)
app_label.place(x= 0, y= 0)


# criando botões
# clean
b_1 = Button(frame_corpo, text= "C", command= limpa_tela, width = 11, height = 2, bg= cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_1.place(x = 0, y = 0)

b_2 = Button(frame_corpo, text="%", command = lambda:entrar_valores('%') ,width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_2.place(x = 119, y = 0)

b_3 = Button(frame_corpo, text="/",command = lambda:entrar_valores('/') , width = 5, height = 2, bg = cor_verde_claro, font= ('Ivy 13 bold'))
b_3.place(x = 177, y = 0)


b_4 = Button(frame_corpo, text="7",command = lambda:entrar_valores('7') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_4.place(x = 0, y = 52)

b_5 = Button(frame_corpo, text="8",command = lambda:entrar_valores('8') , width = 5, height = 2, bg = cor_verde_cinza_claro, font= ('Ivy 13 bold'))
b_5.place(x = 59, y = 52)

b_6 = Button(frame_corpo, text="9",command = lambda:entrar_valores('9') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_6.place(x = 118, y = 52)

b_7 = Button(frame_corpo, text="*",command = lambda:entrar_valores('*') , width = 5, height = 2, bg = cor_verde_claro, font= ('Ivy 13 bold'))
b_7.place(x = 177, y = 52)


b_8 = Button(frame_corpo, text="4",command = lambda:entrar_valores('4') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_8.place(x = 0, y = 104)

b_9 = Button(frame_corpo, text="5",command = lambda:entrar_valores('5') , width = 5, height = 2, bg = cor_verde_cinza_claro, font= ('Ivy 13 bold'))
b_9.place(x = 59, y = 104)

b_10 = Button(frame_corpo, text="6",command = lambda:entrar_valores('6') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_10.place(x = 118, y = 104)

b_11 = Button(frame_corpo, text="-",command = lambda:entrar_valores('-') , width = 5, height = 2, bg = cor_verde_claro, font= ('Ivy 13 bold'))
b_11.place(x = 177, y = 104)


b_12 = Button(frame_corpo, text="1",command = lambda:entrar_valores('1') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_12.place(x = 0, y = 156)

b_13 = Button(frame_corpo, text="2",command = lambda:entrar_valores('2') , width = 5, height = 2, bg = cor_verde_cinza_claro, font= ('Ivy 13 bold'))
b_13.place(x = 59, y = 156)

b_14 = Button(frame_corpo, text="3",command = lambda:entrar_valores('3') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_14.place(x = 118, y = 156)

b_15 = Button(frame_corpo, text="+",command = lambda:entrar_valores('+') , width = 5, height = 2, bg = cor_verde_claro, font= ('Ivy 13 bold'))
b_15.place(x = 177, y = 156)


b_16 = Button(frame_corpo, text= "0",command = lambda:entrar_valores('0') , width = 11, height = 2, bg= cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_16.place(x = 0, y = 208)

b_17 = Button(frame_corpo, text=".",command = lambda:entrar_valores('.') , width = 5, height = 2, bg = cor_verde_cinza_claro, font = ('Ivy 13 bold'))
b_17.place(x = 119, y = 208)

b_18 = Button(frame_corpo, text="=",command = calcular , width = 5, height = 2, bg = cor_verde_claro, font= ('Ivy 13 bold'))
b_18.place(x = 180, y = 208)



    
janela.mainloop()