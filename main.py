import gastos  
import login  
import planejamento  
import renda  
from time import sleep

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastro")
        print("2. Gastos")
        print("3. Planejamento Financeiro")
        print("4. Renda")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login.menu_produto()  # Chama o menu de cadastro
        elif opcao == "2":
            gastos.main()  # Chama o menu principal do CRUD de despesas
        elif opcao == "3":
            planejamento.crud_planejamento()  # Chama o CRUD de planejamento financeiro
        elif opcao == "4":
            renda.criar_menu()  # Chama o menu do CRUD de renda
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
