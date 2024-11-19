import json
import os
from time import sleep


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


def calcular_poupanca(salario):
    if salario >= 20000:
        poupanca = salario * 0.10
        return poupanca
    elif salario >= 10000:
        poupanca = salario * 0.07
        return poupanca
    else:
        poupanca = salario * 0.02
        return poupanca

def salvar_poupanca(salario, poupanca):
    if os.path.exists("planejamento.json"):
        with open("planejamento.json", "r") as f:
            dados = json.load(f)
    else:
        dados = []

    dados.append({"salario": salario, "poupanca": poupanca})

    with open("planejamento.json", "w") as f:
        json.dump(dados, f, indent=4)

    print(cor.VERDE + f"📊 Cálculo de poupança de R${salario:.2f} registrado!" + cor.RESET)
    sleep(2)

def listar_poupancas():
    if os.path.exists("planejamento.json"):
        with open("planejamento.json", "r") as f:
            dados = json.load(f)
        
        if dados:
            print(cor.CIANO + "\nHistórico de Poupanças:" + cor.RESET)
            for index, item in enumerate(dados, start=1):
                print(f"{index}. Salário: R${item['salario']:.2f} | Poupança: R${item['poupanca']:.2f}")
        else:
            print("Nenhum cálculo de poupança registrado até o momento.")
    else:
        print("Ainda não há registros de poupança.")
    sleep(3)

def exibir_menu_poupanca():
    print("\nMENU DE PLANEJAMENTO FINANCEIRO:")
    print("1. CALCULAR POUPANÇA")
    print("2. HISTÓRICO DE POUPANÇAS")
    print("3. VOLTAR AO MENU PRINCIPAL")


def crud_planejamento():
    while True:
        exibir_menu_poupanca()
        opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

        if opcao == "1":
            try:
                salario = float(input("DIGITE O SEU SALÁRIO (ex: 15000):\n>>>"))
                poupanca = calcular_poupanca(salario)
                print(f"🎯 COM UM SALÁRIO DE R${salario:.2f}, VOCÊ DEVE POUPAR R${poupanca:.2f}.")
                salvar_poupanca(salario, poupanca)
            except ValueError:
                print(cor.VERMELHO + "😡 POR FAVOR, DIGITE UM VALOR VÁLIDO PARA O SALÁRIO!" + cor.RESET)
        
        elif opcao == "2":
            listar_poupancas()
        
        elif opcao == "3":
            print("VOLTANDO AO MENU PRINCIPAL...")
            sleep(2)
            break

        else:
            print(cor.VERMELHO + "😡 OPÇÃO INVÁLIDA! TENTE NOVAMENTE!" + cor.RESET)
            sleep(1)
