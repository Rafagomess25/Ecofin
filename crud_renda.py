import json
import os
from time import sleep

# Caminho do arquivo
arquivo = os.path.join(os.path.dirname(__file__), 'dados.json')

# Se o arquivo não existir, cria ele com uma lista vazia
if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump([], f)  # Garante que o JSON seja uma lista vazia

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
    """Cria um novo cliente e adiciona ao arquivo JSON."""
    
    cliente = {
        "id": id,
        "nome": nome,
        "valor_inicial": valor_inicial,
        "rendimento_estimado": calcular_rendimento(valor_inicial)  # Calcula o rendimento estimado
    }
    
    with open(arquivo, "r+") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            dados = []  # Se o arquivo estiver vazio, inicializa uma lista vazia
        
        if not isinstance(dados, list):
            dados = []
        
        dados.append(cliente)
        
        f.seek(0)
        json.dump(dados, f, indent=4)
        f.truncate()  # Garante que o arquivo seja truncado corretamente

def ler_cliente(id):
    """Lê as informações de um cliente especifico pelo ID."""
    with open(arquivo, "r") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            return None  # Se o arquivo estiver vazio, retorna None
        
        for cliente in dados:
            if cliente["id"] == id:
                return cliente
    return None

def atualizar_cliente(id, novo_valor):
    """Atualiza o valor investido de um cliente."""
    with open(arquivo, "r+") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            dados = []  # Se o arquivo estiver vazio, inicializa uma lista vazia
        
        for cliente in dados:
            if cliente["id"] == id:
                cliente["valor_inicial"] = novo_valor
                cliente["rendimento_estimado"] = calcular_rendimento(novo_valor)
                break
        
        f.seek(0)
        json.dump(dados, f, indent=4)
        f.truncate()  # Garante que o arquivo seja truncado corretamente

def deletar_cliente(id):
    """Deleta um cliente do sistema."""
    with open(arquivo, "r+") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            return  # Se o arquivo estiver vazio, não faz nada
        
        dados = [cliente for cliente in dados if cliente["id"] != id]
        
        f.seek(0)
        json.dump(dados, f, indent=4)
        f.truncate()  # Garante que o arquivo seja truncado corretamente

def calcular_rendimento(valor_inicial):
    """Calcula o rendimento estimado após 1 ano."""
    taxa_juros = 0.05  # 5% ao mês
    meses = 12
    rendimento = valor_inicial * (1 + taxa_juros) ** meses
    return round(rendimento, 2)  # Arredonda o valor para 2 casas decimais

if __name__ == "__main__":
    criar_menu()
