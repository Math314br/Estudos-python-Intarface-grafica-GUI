#script DE CONECTAR AO BANCO DE DADOS
import mysql.connector

conexao = mysql.connector.connect(
   host="localhost",
    user="root",
    password="0314",
    database="mydatabase"
)


mycursor = conexao.cursor()
print('conexao com banco de dados com sucesso !!')
