import os
from time import sleep
import json

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


# Função para calcular o valor a ser poupado
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


def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO PLANEJAMENTO FINANCEIRO <<<---- ")
    print("          1 - CALCULAR POUPANÇA ")
    print("          2 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)


def exibir_menu_poupanca():
    print("\nMENU DE PLANEJAMENTO FINANCEIRO:")
    print("1. CALCULAR POUPANÇA")
    print("2. VOLTAR AO MENU PRINCIPAL")


def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            case 1:
                while True: 
                    exibir_menu_poupanca()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        try:
                            salario = float(input("DIGITE O SEU SALÁRIO (ex: 15000):\n>>>"))
                            poupanca = calcular_poupanca(salario)
                            print(f"\n🎯 COM UM SALÁRIO DE R${salario:.2f}, VOCÊ DEVE POUPAR R${poupanca:.2f}.")
                        except ValueError:
                            print("😡 POR FAVOR, DIGITE UM VALOR VÁLIDO PARA O SALÁRIO!")
                    
                    elif opcao == "2":
                        print("VOLTANDO AO MENU PRINCIPAL...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 2:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main()

              