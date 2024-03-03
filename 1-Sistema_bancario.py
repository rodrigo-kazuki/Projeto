menu = """
[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques =0
LIMITE_SAQUES =3

while True:
    opcao = input(menu)
    if opcao == "a":
        deposito = float(input("Quanto deseja depositar?"))
        if deposito>0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"Deposito realizado:R${deposito:.2f}")
        else:
            print("Operação falhou! Informe um valor válido")       
    elif opcao == "b":
        saque = float(input("Quanto deseja sacar?"))
        if saque <= saldo and saque <= 500 and numero_saques<LIMITE_SAQUES:
            saldo -= saque
            numero_saques +=1
            extrato += f"Saque R${saque:.2f}\n"
            print(f"Saque de R${saque:.2f} realizado")
        else:
            print("Não é possivel realizar o saque")
    elif opcao == "c":
        print("\n=============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:R$: R$ {saldo:.2f}")
        print("===================================")
    elif opcao == "d":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
