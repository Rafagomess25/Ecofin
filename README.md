# Ecofin - Gerenciador de Finanças

Bem-vindo ao Ecofin, um gerenciador de finanças pessoais que permite controlar suas despesas e rendas de forma eficiente. Este programa é um CRUD (Create, Read, Update, Delete) que auxilia no planejamento e controle financeiro.

## Funcionalidades

- **Login/Produtos**: Gerencia o login dos usuários e produtos.
- **Gastos**: Adiciona, lista, atualiza e exclui despesas.
- **Planejamento Financeiro**: Calcula e registra poupanças baseadas no salário, listando históricos de poupança.
- **Renda**: Adiciona, consulta, atualiza e exclui informações sobre rendas e investimentos.

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicializa o programa e gerencia o menu principal.
- `gastos.py`: CRUD de despesas, onde você pode adicionar, listar, atualizar e excluir despesas.
- `login.py`: Gerencia o login dos usuários e produtos, incluindo funcionalidades de adicionar, atualizar, buscar e excluir usuários.
- `planejamento.py`: Gerencia o planejamento financeiro, permitindo calcular e registrar poupanças baseadas no salário.
- `renda.py`: CRUD de rendas e investimentos, permitindo adicionar, consultar, atualizar e excluir informações sobre clientes e seus investimentos.

## Requisitos

- Python 3.x
- Biblioteca `json` (inclusa na biblioteca padrão do Python)
- Biblioteca `os` (inclusa na biblioteca padrão do Python)
- Biblioteca `time` (inclusa na biblioteca padrão do Python)

## Instalação

1. **Clone o repositório:**
    ```bash
    git clone 
    ```

2. **Navegue até o diretório do projeto:**
    ```bash
    cd ecofin
    ```

3. **Execute o programa:**
    ```bash
    python main.py
    ```

## Uso

1. **Menu Principal:**
    - Escolha uma opção do menu principal para acessar as diferentes funcionalidades do programa.

2. **Login/Produtos:**
    - **Cadastrar Usuário**: Digite o nome, idade, CPF e senha do usuário.
    - **Atualizar Cadastro**: Atualize as informações de um usuário existente.
    - **Excluir Cadastro**: Remove um usuário do sistema pelo CPF.
    - **Buscar Usuário**: Procura um usuário específico pelo nome.

3. **Gastos:**
    - **Adicionar Despesa**: Digite o nome e o valor da despesa.
    - **Listar Despesas**: Exibe todas as despesas cadastradas.
    - **Atualizar Despesa**: Atualiza o nome e o valor de uma despesa existente.
    - **Excluir Despesa**: Remove uma despesa do sistema.
    - **Buscar Despesa**: Procura uma despesa específica pelo nome.
    - **Verificar Limite de Orçamento**: Calcula se você está dentro do seu orçamento.

4. **Planejamento Financeiro:**
    - **Calcular Poupança**: Calcula a poupança com base no salário informado.
    - **Histórico de Poupanças**: Lista todos os cálculos de poupança registrados.

5. **Renda:**
    - **Criar Novo Cliente**: Adiciona um novo cliente e seu investimento inicial.
    - **Consultar Cliente**: Exibe as informações de um cliente pelo ID.
    - **Atualizar Valor Investido**: Atualiza o valor investido de um cliente.
    - **Excluir Cliente**: Remove um cliente do sistema.

## Contribuição

Se você deseja contribuir com o projeto, sinta-se à vontade para fazer um fork e enviar pull requests. Sugestões e melhorias são sempre bem-vindas!

