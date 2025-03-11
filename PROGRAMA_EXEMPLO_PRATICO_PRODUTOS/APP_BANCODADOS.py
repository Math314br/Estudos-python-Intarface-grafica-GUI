#aqui sera parte que usara banco de dados na app

from mysql.connector  import Error
from criar_tabela import conexao,mycursor

class APPBD:
    def __init__(self):
     self.conn = None
     self.cur = None
     self.BANCO_con()
   
    def BANCO_con(self):
       self.conn = conexao
       self.cur = mycursor
       print('CONEXAO COM BANCO DE DADOS FEITO COM SUCESSO')

    def selecionar_dados(self):
       try:
          self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO")
          registros =  self.cur.fetchall()
          return registros
       except (Exception, Error) as error:
         print ("ERRO AO SELECIONAR DADOS: ", error)
         return []
    def inserir_dados(self,nome,preco):
       try:
          self.cur.execute(''' INSERT INTO PRODUTO (NOME,PRECO) VALUES(%s,%s)''',(nome,preco))
          self.conn.commit()
          print('inserção realizada com sucesso !')
       except (Exception,Error) as error:
          print('Erro ao inserir dados', error)
    def atualizar_dados(self,codigo,nome,preco):
       try:
        self.cur.execute(''' UPDATE PRODUTO SET NOME = %s, PRECO = %s,  WHERE CODIGO = %s''',(nome,preco,codigo)
                         )
        self.conn.commit()
        print("Atualizado COM sucesso!!")
       except (Exception, Error) as error:
          print("erro ao atualizar dados", error)
    
    def excluir_dados(self,codigo):
       try:
          self.cur.execute(''' DELETE FROM PRODUTO WHERE  CODIGO = %s''',(codigo))
          self.conn.commit()
          print("Exclusão realizada COM sucesso")
       except (Exception, Error) as error:
          print("Erro Ao Excluir Dados", error)
    
if __name__ == '__main__':
   app_db = APPBD()
       

