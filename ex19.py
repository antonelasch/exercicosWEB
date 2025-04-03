def jogar_jokenpo():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    print("Seja bem-vindo ao jogo de Jokenpô!")
    print("Informe uma opção:")
    print("1 - Pedra")
    print("2 - Tesoura")
    print("3 - Papel")
    
    opcao_usuario = int(input("Digite o número correspondente à sua escolha: "))
    
    if opcao_usuario != [0, 1, 2]: print("Opção inválida! Tente novamente")

    else: print("Opção válida")
            
    opcao_comp = (ord(input("Selecione/pressiona uma tecla aleatória para que a escolha do computador seja feita! ")) % 3)
    
    print("Você escolheu:", opcao_usuario)

    print("O computador escolheu:", opcao_comp)
    
    if opcao_usuario == opcao_comp: print("EMPATE entre o usuário e o computador!")

    elif (opcao_usuario == 0 and opcao_comp == 2) or (opcao_usuario == 1 and opcao_comp == 0) or (opcao_usuario == 2 and opcao_comp == 1): print("Você VENCEU!")

    else: print("O computador VENCEU!")

    if __name__ == "__main__": jogar_jokenpo()
