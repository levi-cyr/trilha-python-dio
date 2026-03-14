pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

#teste dos formatos de dicionario
linguagem = {"lingua": ["Python", "C#", "Java"]}
print(linguagem)

linguagem = dict(lingua={"Python", "C#", "Java"})
print(linguagem)

linguagem["lingua"] = "Python", "C#", "Java"
print(linguagem)
