import time

menu = """
Escolha a opção desejada:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
      valor_do_deposito = int(input("Digite o valor a ser depositado: "))
      if valor_do_deposito > 0:
        saldo += valor_do_deposito
        extrato += f"DEPÓSITO: R${valor_do_deposito:.2f}\n"
      else:
        print("Valor inválido para depósito.")

    elif opcao == "s":
      valor_do_saque = int(input("Digite o valor do saque: "))
      if valor_do_saque <= saldo and valor_do_saque > 0:
        if valor_do_saque <= limite:
          if numero_saques < LIMITE_SAQUES:
            numero_saques += 1
            saldo -= valor_do_saque
            extrato += f"SAQUE: R${valor_do_saque:.2f}\n"
            print("Contagem de notas...")
            time.sleep(3)
            print("Valor liberado. Retire as cédulas.")
          else:
            print("Limite de saque diário excedido, por favor fale com o seu gerente.")
        else:
          print("Limite por saque excedido. Reduza o valor do saque.")
      else:
        print("Saldo insuficiente! Consulte seu saldo.")

    elif opcao == "e":
      print("Extrato".center(46, "-"))
      print(extrato)
      print("-" * 46)
      print(f"SALDO: R${saldo:.2f}")

    elif opcao == "q":
      break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")