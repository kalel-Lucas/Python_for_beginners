def depositar(saldo, valor): 
    if valor<=0:
        print("Digite um valor válido, por favor!")
        return saldo
    else: 
        return saldo+valor 

def sacar(saldo, valor):
    if valor <= 0:
        print("Valor de saque inválido.")
        return saldo
    elif valor > saldo:
        print("Saldo insuficiente.")
        return saldo
    else: saldo - valor

def verifica_saldo(saldo): 
    print(saldo)
