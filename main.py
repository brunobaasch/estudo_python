from functions import *
lista = []
opcao = 0

while opcao!=5:
    try:
        opcao = int(input("\nCadastro de produtos\nMenu:\n1- Create\n2-Read\n3-Update\n4-Delete\n5-Exit\nDigite um número: "))
    except ValueError:
        print("Erro!\nDigite um número!")
    if opcao==1:
        create(lista)
    elif opcao==2:
        if lista:
            read(lista)
    elif opcao==3:
        if lista:
            update(lista)
    elif opcao==4:
        if lista:
            delete(lista)
    elif opcao==5:
        break
