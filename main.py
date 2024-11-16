import login_PEDRO


def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. login_PEDRO")
        print("2. ")
        print("3. ")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login_PEDRO.menu_produto()
        elif opcao == "2":
       #     .menu_cliente()
       # elif opcao == "3":
      #      .menu_pedido()
      #  elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
