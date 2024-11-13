import json
import os
from time import sleep


if os.path.getsize("login_json") > 0:  
    with open("login_json") as login_json:
        dados = json.load(login_json)
        print(dados)
else:
    print("O arquivo JSON está vazio.")


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'login_json')

def login_usuario():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

    with open(arquivo, 'r') as f:
        return json.load(f)

def cadastro_usuario():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

def adicionar_usuario(nome, idade, CPF, Senha):
    usuarios = login_usuario()

    usuarios.append({'nome': nome, 'idade': idade, 'CPF': CPF , 'senha': Senha})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("Cadastro realizado com sucesso!")

def atualizar_usuario(nome_antigo, novo_nome, nova_idade, novo_cpf, nova_senha):
    usuarios = login_usuario()

    for usuario in usuarios:
        if usuario['nome'] == nome_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            usuario['CPF'] = novo_cpf
            usuario['senha'] = nova_senha

            break

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("Cadastro atualizado com sucesso")

def excluir_usuario(cpf):
    usuarios = login_usuario()

    for usuario in usuarios:  
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("Cadastro excluido com sucesso")

def buscar_usuario(nome):
    usuarios = login_usuario()
    
    encontrado = False

    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}, cpf:{usuario['cpf']}, senha:{usuario['senha']}")
            encontrado = True
    if not encontrado:
        print("CADASTRADO não encontrado.")

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO EcoFim <<<---- ")
    print("          1 - Entra ")
    print("          2 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)
    
def exibir_menu():
    print("\nMENU:")
    print("1. Cadastrar ")
    print("2. ATUALIZAR Cadastro")
    print("3. EXCLUIR Cadastro")
    print("4. Entra")
    print("5. VOLTAR AO MENU ANTERIOR")

def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True: 
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME:\n>>>")
                        idade = input(" DIGITE A IDADE:\n>>>")
                        cpf = input("DIGITE O CPF\n>>>")
                        senha = input("DIGITE UMA SENHA\n>>>")
                        adicionar_usuario(nome, idade, cpf, senha)
                    elif opcao == "2":
                        nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                        nova_idade = input("DIGITE A NOVA IDADE:\n>>>")
                        novo_cpf = input("DIGITE O NOVO CPF\n>>>")
                        nova_senha = input("DIGITE A NOVA SENHA\n>>>")
                        atualizar_usuario(nome_antigo, novo_nome, nova_idade, novo_cpf, nova_senha)
                    elif opcao == "3":
                        nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        excluir_usuario(nome)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME DO USUÁRIO:\n>>>")
                        senha = input("DIGITE A SENHA\n>>>")
                        cpf = input("DIGITE O CPF:\n>>>")
                        buscar_usuario(nome, senha, cpf)
                    elif opcao == "5":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("")
                sleep(3)
                break
            case __:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()