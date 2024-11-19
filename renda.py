import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'dados.json')

crud_renda = "dados.json"

if not os.path.exists(crud_renda):
    with open(crud_renda, 'w') as arquivo:
        json.dump([], arquivo) 
        
def criar_menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Criar novo cliente")
        print("2. Consultar informações de um cliente")
        print("3. Atualizar valor investido")
        print("4. Excluir cliente")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            id = input("Digite o ID do cliente: ")
            nome = input("Digite o nome do cliente: ")
            valor_inicial = float(input("Digite o valor inicial do investimento: "))
            criar_cliente(id, nome, valor_inicial)
        elif opcao == "2":
            id = input("Digite o ID do cliente: ")
            cliente = ler_cliente(id)
            if cliente:
                print(cliente)
            else:
                print("Cliente não encontrado.")
        elif opcao == "3":
            id = input("Digite o ID do cliente: ")
            novo_valor = float(input("Digite o novo valor do investimento: "))
            atualizar_cliente(id, novo_valor)
        elif opcao == "4":
            id = input("Digite o ID do cliente: ")
            deletar_cliente(id)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def criar_cliente(id, nome, valor_inicial):
  
    cliente = {
        "id": id,
        "nome": nome,
        "valor_inicial": valor_inicial,
        "rendimento_estimado": calcular_rendimento(valor_inicial) 
    }
    
    with open("dados.json", "r+") as arquivo:
        dados = json.load(arquivo)
        dados.append(cliente)
        arquivo.seek(0)
        json.dump(dados, arquivo, indent=4)
        
def ler_cliente(id):
    
    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)
        for cliente in dados:
            if cliente["id"] == id:
                return cliente
    return None

def atualizar_cliente(id, novo_valor):
   
    with open("dados.json", "r+") as arquivo:
        dados = json.load(arquivo)
        for cliente in dados:
            if cliente["id"] == id:
                cliente["valor_inicial"] = novo_valor
                cliente["rendimento_estimado"] = calcular_rendimento(novo_valor)
                break
        arquivo.seek(0)
        json.dump(dados, arquivo, indent=4)
        
def deletar_cliente(id):
    
    with open("dados.json", "r+") as arquivo:
        dados = json.load(arquivo)
        dados = [cliente for cliente in dados if cliente["id"] != id]
        arquivo.seek(0)
        arquivo.truncate()  
        json.dump(dados, arquivo, indent=4)
        
def calcular_rendimento(valor_inicial):
    
    taxa_juros = 0.05 # 5% ao mês 
    meses = 12
    rendimento = valor_inicial * (1 + taxa_juros) ** meses
    return round(rendimento, 2)

if __name__ == "__main__":
    criar_menu()
