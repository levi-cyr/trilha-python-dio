dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

#posso armazenar mais de um dado na chave, como exemplo 2 nomes com 2 idades, 2 telefones, etc
dados2 = {"nome": ["Levi", "Guilherme"], "idade": [26, 28]}

print(dados2["nome"][0]) #acesso como uma array, especificando se quero a de ambos ou só de um em especifico
print(dados2["nome"][1])

print(dados2)
