#utilizando faker para gerar dados ele gera dados falsos para complemantar tabela
from faker import  Faker
from conectar import conexao,mycursor

#idioma do faker
Fake = Faker('pt_BR')

# AQUI ira gerar 20 dados falsos com faker, e preco sera formatado para ter 5 digitos e 3 casas antes do ponto.

for _ in range(20):
    nome = Fake.name()
    preco = round(Fake.random_number(digits=5) / 100, 2)
    print("DADOS GERADOS", nome, preco)
    mycursor.execute(''' INSERT INTO PRODUTO (NOME, PRECO) VALUES(%s,%s)''',(nome,preco))
conexao.commit()
print('dados inseridos com sucesso!!')
mycursor.close()
conexao.close()    