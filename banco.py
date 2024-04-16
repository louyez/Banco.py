#O saldo, inicialmente começa com o valor "0":
saldo = 0
#Comando para deixar o programa em Loop:
while True:
    try:
        #O usuário escolhe entre as seguintes opções de como executar o programa:
        escolha = int(input(f"Olá, escolha entre as seguintes opções:\n"
                            "[1] - Depósito\n"
                            "[2] - Saque\n"
                            "[3] - Visualizar saldo\n"
                            "[4] - Fim do programa\n"))
        #A seguir, sua escolha se torna uma operação:
        if escolha == 1:
            deposito = int(input("Digite o valor do depósito:"))
            saldo += deposito
            #Se a escolha for um depósito, ele soma o valor atual com o nóvo número.
            print(f"Depósito de  R${deposito:.2f}realizado com sucesso!")
            print(f"Saldo atual: R${saldo:.2f}")
        
        elif escolha == 2:
            saque = int(input("Digite o valor do seu saque:"))
            if saque > saldo:
                print("Saldo insuficiente para a operação!")
            else:
                saldo -= saque
                #Se a escolha for um saque, ele subtrai o valor atual com o novo número.
                print(f"Saque de R${saque:.2f} realizado com sucesso.")
                print(f"Saldo restante: R${saldo:.2f}")

        elif escolha == 3:
            print(f"Seu saldo é: R${saldo:.2f}")
            #A escolha de exibição, irá exibir o atual valor na conta.

        elif escolha == 4:
            print("Fim das Operações...")
            #Essa escolha, encerra o programa. Em seguida, quebrando o Loop
            break

        else:
            print("Opção inválida. Por favor escolha uma opção válida...")
            #Caso a escolha do usuário não seja entre às [1, 2, 3 e 4], este é o erro exibido no programa.
    except ValueError:
        print("Por favor, digite um número válido!")
        #Caso a escolha do usuário não seja um número inteiro, este é o erro exibido.