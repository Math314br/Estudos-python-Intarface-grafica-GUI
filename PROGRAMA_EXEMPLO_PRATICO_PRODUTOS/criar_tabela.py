#importando script de conexao 
from  conectar import conexao, mycursor

# criando tabelas
# NUMERIC (10,2) É USADO PARA ARMAZENAR NUMEROS DECIMAIS 2 DIGITOS DPS DA VIRGULA TIPO 1.30 OU 20.30
mycursor.execute(''' CREATE TABLE IF NOT EXISTS PRODUTO (CODIGO INT AUTO_INCREMENT PRIMARY KEY,
                 NOME VARCHAR(150) NOT NULL, PRECO NUMERIC (10, 2) NOT NULL
                 );''')

conexao.commit()
print("tabela criada com sucesso!")
conexao.close()
