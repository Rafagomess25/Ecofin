
import json
import os
from time import sleep


arquivo = os.path.join(os.path.dirname(__file__), 'login_json')

def carregar_dados():
    if os.path.exists(arquivo) and os.path.getsize(arquivo) > 0:
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        print("O arquivo JSON está vazio ou não existe.")
        return []

def criar_arquivo_login():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

def adicionar_usuario(nome, idade, cpf, senha):
    usuarios = carregar_dados()
    usuarios.append({'nome': nome, 'idade': idade, 'cpf': cpf, 'senha': senha})
    
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    
    print("Cadastro realizado com sucesso!")

def atualizar_usuario(nome_antigo, novo_nome, nova_idade, novo_cpf, nova_senha):
    usuarios = carregar_dados()
    for usuario in usuarios:
        if usuario['nome'] == nome_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            usuario['cpf'] = novo_cpf
            usuario['senha'] = nova_senha
            break
    
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    
    print("Cadastro atualizado com sucesso!")

def excluir_usuario(cpf):
    usuarios = carregar_dados()
    usuarios = [usuario for usuario in usuarios if usuario['cpf'] != cpf]
    
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    
    print("Cadastro excluído com sucesso!")

def buscar_usuario(nome):
    usuarios = carregar_dados()
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}, CPF: {usuario['cpf']}, SENHA: {usuario['senha']}")
            return
    print("Cadastro não encontrado.")


def menu_produto():
    print("\n--- Menu ---")
    print("1. Cadastrar usuário")
    print("2. Atualizar cadastro")
    print("3. Excluir cadastro")
    print("4. Buscar usuário")
    print("5. Voltar ao menu principal")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome:\n>>> ")
        idade = input("Digite a idade:\n>>> ")
        cpf = input("Digite o CPF:\n>>> ")
        senha = input("Digite uma senha:\n>>> ")
        adicionar_usuario(nome, idade, cpf, senha)

    elif opcao == "2":
        nome_antigo = input("Digite o nome a ser atualizado:\n>>> ")
        novo_nome = input("Digite o novo nome:\n>>> ")
        nova_idade = input("Digite a nova idade:\n>>> ")
        novo_cpf = input("Digite o novo CPF:\n>>> ")
        nova_senha = input("Digite a nova senha:\n>>> ")
        atualizar_usuario(nome_antigo, novo_nome, nova_idade, novo_cpf, nova_senha)

    elif opcao == "3":
        cpf = input("Digite o CPF do usuário a ser excluído:\n>>> ")
        excluir_usuario(cpf)

    elif opcao == "4":
        nome = input("Digite o nome do usuário:\n>>> ")
        buscar_usuario(nome)

    elif opcao == "5":
        print("Voltando ao menu principal...")
        sleep(3)
        return 

    else:
        print("Opção inválida! Tente novamente.")
