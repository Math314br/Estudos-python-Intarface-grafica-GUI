#aqui sera parte que usara banco de dados na app

from mysql.connector  import Error
from criar_tabela import conexao,mycursor

class APPBD:
    def __init__(self,conexao,mycursor):
     self.conn = conexao
     self.cur = mycursor
     print('CONEXÃO COM BANCO DE DADOS FEITA COM SUCESSO!')
     self.BANCO_con()
   
    def BANCO_con(self):
       self.conn = conexao
       self.cur = mycursor
       print('CONEXAO COM BANCO DE DADOS FEITO COM SUCESSO')

    def selecionar_dados(self):
       try:
        # Imprimir para verificar se a conexão e o cursor estão configurados corretamente
        print("Tentando executar a consulta SQL...")

        # Tente executar a consulta SQL
        self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO")
        
        # Imprimir para verificar se a consulta foi executada com sucesso
        print("Consulta executada com sucesso!")

        # Recuperando os registros da tabela
        registros = self.cur.fetchall()

        # Verifique os registros recuperados
        print(f"Registros recuperados: {registros}")
        
        return registros
       except (Exception, Error) as error:
        # Exibir a mensagem de erro detalhada
        print("ERRO AO SELECIONAR DADOS: ", error)
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
        self.cur.execute(''' UPDATE PRODUTO SET NOME = %s, PRECO = %s  WHERE CODIGO = %s''',(nome,preco,codigo)
                         )
        self.conn.commit()
        print("Atualizado COM sucesso!!")
       except (Exception, Error) as error:
          print("erro ao atualizar dados", error)
    
    def excluir_dados(self,codigo):
       try:
          self.cur.execute(''' DELETE FROM PRODUTO WHERE  CODIGO = %s''',(codigo,))
          self.conn.commit()
          print("Exclusão realizada COM sucesso")
       except (Exception, Error) as error:
          print("Erro Ao Excluir Dados", error)
      
    
if __name__ == '__main__':
   app_db = APPBD(conexao,mycursor)
       

