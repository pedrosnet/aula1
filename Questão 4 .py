#Questão 4 

#Foi determinado uma lista onde todos valores será armazenados 
todas_idades = []
idade = int(input("Digte uma idade: "))

# O while, tem a função de verificar se determinado valor é menor que zero, onde, caso seja, o comando para de funcionar 
while idade >= 0:
    todas_idades.append(idade)
    idade = int(input("Digita sua idade: "))

# Aqui será feita a soma de todos os valores e irá dividir essa soma pela quantidade de elementos presentes dentro da lista, obtendo assim a média!
soma_idades = sum(todas_idades)
media = soma_idades / len(todas_idades)
print("A média é das idades é de: ", media))