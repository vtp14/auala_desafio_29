import os

codigo = int(input("Digite o código do produto: "))

nome = input("Nome do produto: ")

quantidade = int(input("Digite a quantidade: "))

preço = int(input("Digite o preço do produto: "))

resp = preço*quantidade


print("------------------------------")
print("           CADASTRO           ")
print("CÓDIGO DO PRODUTO: ",codigo)
print("NOME DO PRODUTO: ",nome)
print("QUANTIDADE: ",quantidade)
print("PREÇO: R$",preço)
print("PREÇO TOTAL: R$",resp)
print("------------------------------")

os.system("pause")

import os