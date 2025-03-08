#testes basicas tkinter gui
import tkinter as tk
from tkinter import messagebox

#BOTAO BAS_ICO
def exibir_nome():
    nome = entry_nome.get()
    print(f"Nome: {nome}")
    return nome
#checkbox basico
def checkbox():
    idade = check.get()
    if idade == 1:
        idade ="SIM, É MAIOR DE IDADE"
    else:
        idade="NÃO, É MENOR DE IDADE"    
    print(f"É maior de idade ? {idade}")
    return idade
#radio
def exibir_radio():
    opcao = radio.get()
    print(f"Mora No Estado: {opcao}")
    return opcao
#listbox
def exibir_lista():
    item_selecionado = listbox.curselection()#obtem iten selecionado
    if item_selecionado:
        item = listbox.get(item_selecionado)
        print(f"Tipo Sanguino:{item}")
    return item 


def exibir_mensagem():
    nome = exibir_nome()
    maior = checkbox()
    estado = exibir_radio()
    sangue = exibir_lista()

    mensagem_user =(f"Aqui Estão Todas As Informaçoes: Nome: {nome} \n Maior De Idade: {maior} \n Estado: {estado}  \n Tipo De Sangue: {sangue}")
    
    messagebox.showinfo("Todas Informações Do User", mensagem_user)

# criar janela principal
root = tk.Tk()
root.title("TESTES TKINTER") # titulo do programa
root.geometry('320x480') # tamanho da janela


#widgets basicos
#labels
label_nome = tk.Label(root, text="Nome: ")
label_nome.pack() #pack add widgets na janela

#entrandas para nome
entry_nome = tk.Entry(root)
entry_nome.pack()

#criando botao ira pegar funçao exibir nome ao clicar nele NO TERMINAL
botao = tk.Button(root,text="Exibir nome", command=exibir_nome)
botao.pack()

#criando uma checkbox
check = tk.IntVar()
check_botao = tk.Checkbutton(root,text="Maior De Idade", variable=check)
check_botao.pack()

botao_check = tk.Button(root,text="Verificar +18",command=checkbox)
botao_check.pack()

#CRIANDO RADIOBUTTON ESCOLHER ESTADO
radio = tk.StringVar(value='PR') # valor incial
radio1 = tk.Radiobutton(root,text='PR', variable=radio, value='PR')
radio1.pack()
radio2 = tk.Radiobutton(root,text='SP', variable=radio, value='SP')
radio2.pack()
radio3 = tk.Radiobutton(root,text='RJ', variable=radio, value='RJ')
radio3.pack()

botao_radio = tk.Button(root, text='Exibir Estado: ',command=exibir_radio)
botao_radio.pack()

#criando listbox
listbox = tk.Listbox(root, height=3)
listbox.pack()
listbox.insert(tk.END,'Tipo A')
listbox.insert(tk.END,'Tipo B')
listbox.insert(tk.END,'Tipo C')

listabox_botao = tk.Button(root, text='exibir tipo sangue: ', command=exibir_lista)
listabox_botao.pack()
#criar botao  q exiba todos dados em uma tela de mensagem para user
#botao que exiba todas  informçao na tela atraves de uma janela de mensagem para user.
botao_mensagem = tk.Button(root,text='EXIBIR TUDO',command=exibir_mensagem)
botao_mensagem.pack()


root.mainloop()
