def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

def somar():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número:" ))
    soma = num1 + num2
    print(f"A soma entre {num1} e {num2} é igual a {soma}")

#exibir_mensagem()
#exibir_mensagem_2(nome="Guilherme")
#exibir_mensagem_3()
#exibir_mensagem_3(nome="Chappie")
somar()
