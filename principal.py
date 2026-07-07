import operacoes
def main(): 
    saldo = 0.0 
    rodando = True 
    menu = """
    _____CAIXA ELETRÔNICO - MENU_____

    1. DEPOSITAR 
    2. SACAR
    3. VERIFICAR SALDO
    4. SAIR 

    """
    while rodando: 
        print(menu)
        opcao = input("DIGITE ABAIXO O NÚMERO CORRESPONDENTE PARA A OPÇÃO QUE QUEIRA: ")
        if opcao not in ["1","2","3","4"]:
            print("Opção inválida! digite novamente.")
            continue 
        elif opcao == "1": 
            valor = float(input("Digite o valor em que deseja depositar na sua conta:"))
            saldo = operacoes.depositar(saldo,valor)
        elif opcao == "2": 
            valor = float(input("Digite o valor em que deseja sacar na sua conta:"))
            saldo = operacoes.sacar(saldo,valor)
        elif opcao == "3": 
            operacoes.verifica_saldo(saldo)
        elif opcao == "4": 
            print("Até a próxima :)")
            print("Saindo...")
            break 
if __name__ == "__main__":
    main()

