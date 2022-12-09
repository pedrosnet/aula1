# Questão 5:

# Aqui é onde será determinado o valor do seu salario!
salario_bruto = float(input("Qual o seu sálario: "))


# Temos que considerar que o desconto é feito com base no desconto anterior, por isso, é necessário retirar o desconto do "desconto" anterior
# portanto isso é necessário fazer uma subtração do valor bruto com o desconto do inss, para obter o desconto do imposto de renda. 
inss = salario_bruto * 0.11 
imposto_renda = (salario_bruto - inss) * 0.15

# Com os descontos obtidos, resta apenas obter o valor total do desconto e subtrair pelo total 
desconto_total = inss + imposto_renda
salario_liq = salario_bruto - desconto_total

print("Seu salario liquido é de ", salario_liq)
