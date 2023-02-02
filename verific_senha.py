while True:
    senha= str(input("Digite sua senha: "))
    if senha.islower():
        print("a senha deve ter pelo menos um caracter Maiusculo: ")
    elif len(senha)<6 :
        print("a senha deve ter pelo menos 8 caracteres: ")
    elif senha.isupper():
        print("a senha deter pelo menos um caracter minusculo")
    elif senha.isalpha():
        print("Necessita de um numero: ")
    elif senha.isalnum():
        print("necessita de um Caractere especial: ")
    else:
        print("senha aceita com sucesso 1!")
        break