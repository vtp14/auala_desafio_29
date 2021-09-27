import os

nome = input("Digite seu nome: ")
#int() converte o que foi digitado em um valor inteiro
idade = int(input("Digite sua idade: "))

resp = 100 - idade;

print("------------------------------")
print("           Cadastro           ")
print("Nome:",nome)
print("Idade:",idade)
print("Resposta:",resp)
print("------------------------------")

os.system("pause")