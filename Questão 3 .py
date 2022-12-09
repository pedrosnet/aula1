# Questão 3: 

# No inicio será determinado a primeira tentativa, onde, caso errado, na sua tela ira surgir uma mensagem de erro
senha = int(input("Digite sua senha: "))

# A função while será a chave para o programa, visto que, enquanto você não digita a senha correta, você não conseguirá o acesso!
while senha != 2002: 
    print("SENHA INCORRETA! tente novamente: ") 
    senha = input("digite sua senha: ")
   
print ("ACESSO PERMITIDO! Seja bem-vindo a sua conta!")