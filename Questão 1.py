#Questão 1 

#foi determinado uma váriavel feita somenta para armazenar a quantidade de valores pares 
total = 0

#ao digitar o número, será considerado o resto da divisão, caso igual a 0 temos um valor adicionado no total
num = int(input("digite um número: "))
if (num % 2 == 0):
    total = total + 1

num2 = int(input("digite um número: "))
if (num2 % 2 == 0):
    total = total + 1

num3 = int(input("digite um número: "))
if (num3 % 2 == 0):
    total = total + 1

num4 = int(input("digite um número: "))
if (num4 % 2 == 0):
    total = total + 1

num5 = int(input("digite um número: "))
if (num5 % 2 == 0):
    total = total + 1

print ("o total é: ", total)