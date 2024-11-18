import gastos  
import login 
import planejamento  
import renda  
from time import sleep

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Login")
        print("2. Gastos")
        print("3. Planejamento Financeiro")
        print("4. Renda")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login.menu_produto()  
        elif opcao == "2":
            gastos.main()  
        elif opcao == "3":
            planejamento.menu_inicial()  #
        elif opcao == "4":
            renda.criar_menu()  
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
