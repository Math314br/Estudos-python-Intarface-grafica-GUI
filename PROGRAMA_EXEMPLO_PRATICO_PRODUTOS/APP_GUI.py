#parte da intarface do programa.
import tkinter as tk
from tkinter import ttk
from APP_BANCODADOS import APPBD

class Principal:
    def __init__(self,root,db):
        #janela do tk
        self.root = root
        self.db = db
        #titulo do programa
        self.root.title("Gestao De Produtos")
        #label codigo

        self.lblcodigo = tk.Label(root, text="Codigo",font="arial")
        self.lblcodigo.grid(row=0, column=0)
        self.entryCodigo = tk.Entry(root)
        self.entryCodigo.grid(row=0, column=1)
        #label nome
        self.lblnome = tk.Label(root, text="Nome",font="arial")
        self.lblnome.grid(row=1, column=0)
        self.entrynome= tk.Entry(root)
        self.entrynome.grid(row=1, column=1)
        #label preco
        self.lblpreco = tk.Label(root, text="Preço",font="arial")
        self.lblpreco.grid(row=2, column=0)
        self.entrypreco= tk.Entry(root)
        self.entrypreco.grid(row=2, column=1)
        

        # BOTOES
        self.cadastro = tk.Button(root, text='CADASTRAR', command=self.CadastrarProduto)
        self.cadastro.grid(row=3, column=0)
        self.atualizar = tk.Button(root, text='ATUALIZAR', command=self.AtualizarProduto)
        self.atualizar.grid(row=3, column=1)
        self.excluir = tk.Button(root, text='EXCLUIR', command=self.ExcluirProduto)
        self.excluir.grid(row=4, column=0)
        self.limpar = tk.Button(root, text='LIMPAR', command=self.LimparProduto)
        self.limpar.grid(row=4, column=1)
        #exibição tabela gui
        self.tree = ttk.Treeview(root, columns=("CODIGO",'NOME','PRECO'), show='headings')
        self.tree.heading('CODIGO', text='Codigo')
        self.tree.heading('NOME', text='Nome')
        self.tree.heading('PRECO', text='Preço')
        self.tree.grid(row=5, column=0,columnspan=2)
        self.tree.bind('<ButtonRelease-1>',self.aprensentar)

        self.carregarDados()

        #função botao
    def CadastrarProduto(self):
        codigo = self.entryCodigo.get()
        nome = self.entrynome.get()
        preco = self.entrypreco.get()
        self.db.inserir_dados(nome,preco)
        self.tree.insert("","end",values=(codigo,nome,preco))
        self.LimparProduto()
    def AtualizarProduto(self):
        codigo = self.entryCodigo.get()
        nome = self.entrynome.get()
        preco = self.entrypreco.get()
        self.db.inserir_dados(nome,preco)
        self.tree.insert("","end",values=(codigo,nome,preco))
        self.LimparProduto()
        self.carregarDados()
    def ExcluirProduto(self):
        codigo = self.entryCodigo.get()
        self.db.excluir_dados(codigo)
        self.LimparProduto()
    def LimparProduto(self):
        self.entryCodigo.delete(0,tk.END)
        self.entrynome.delete(0,tk.END)
        self.entrypreco.delete(0,tk.END)

        # FUNÇAO NAO FORAM PEGAS AINDAA!!!!!!!!
    
    def aprensentar(self, event):
        item = self.tree.selection()[0]
        valores = self.tree.item(item, 'values')
        self.entryCodigo.delete(0,tk.END)
        self.entryCodigo.insert(tk.END, valores[0])
        self.entrynome.delete(0,tk.END)
        self.entrynome.insert(tk.END, valores[1])
        self.entrypreco.delete(0,tk.END)
        self.entrypreco.insert(tk.END, valores[2])
    def carregarDados(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("","end", values=registro)
root = tk.Tk()
app = APPBD()
app_gui = Principal(root,app)
root.mainloop()    
