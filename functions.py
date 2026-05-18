def create(lista):
    produto = input("\nDigite o nome do produto: ").lower().strip().replace(" ","_")
    teste = True
    for i in range(0, len(lista)):
        if lista[i][0]==produto:
            teste = False        
    if teste: 
        while True:
            try:
                valor = float(input("\nDigite o valor: \n"))
                break          
            except ValueError:
                print("Digite um número!")
        lista.append([produto, valor])
    else:
        print("\nEsse produto já existe!")

def read(lista):
    if lista:
        for i in range(0, len(lista)):
            print(f"\nProduto: {lista[i][0]}\nValor: R${lista[i][1]}")

def update(lista):
    teste = False
    produto = input("\nQual produto voce quer atualizar?\n").lower().strip()
    
    for i in range(0, len(lista)):
        if lista[i][0]==produto:
            teste = True
        if teste:
            antigo = lista[i][1]
            lista[i][1] = float(input(f"\nDigite o novo valor para {lista[i][0]}: "))
            print(f"Valor atualizado de R${antigo} para R${lista[i][1]} ")
        else:    
            opcao = input("\nEsse produto não está cadastrado, deseja cadastrar? (S/N):").lower()
            if opcao=="s":
                create(lista)

def delete(lista):
    produto = input("\nQual produto voce quer remover?")
    for i in range(0, len(lista)):
        if lista[i][0]==produto:
            print(f"\nProduto {lista[i][0]} removido!")
            lista.pop(i)