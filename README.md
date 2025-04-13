# API de Controle de Ação

Este projeto é uma API desenvolvida para o gerenciamento de operações de compra e venda de ações no mercado financeiro. A aplicação permite o registro e acompanhamento de transações, bem como a consolidação e apuração da posição, indicando se há lucro ou prejuízo por ativo.

## Descrição

A API foi construída utilizando Python e organiza-se nos seguintes diretórios:

- `model/`: Contém os modelos de dados utilizados na aplicação.
- `schemas/`: Define os esquemas de validação para as entradas e saídas da API.
- `app.py`: Arquivo principal que inicializa a aplicação.
- `logger.py`: Responsável pelo gerenciamento de logs.
- `requirements.txt`: Lista as dependências do projeto.

## Funcionalidades

- **Gestão de Operações**: Registre e acompanhe compras e vendas de ações.
- **Posição Total**: Visualize o desempenho de cada ativo, identificando lucros e prejuízos.
- **Consulta de Cotações**: A API integra-se com serviços externos para obter cotações atuais de ações e fundos imobiliários.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção de APIs rápidas e eficientes.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **Pydantic**: Validação de dados e definição de esquemas.
- **Docker**: Contêinerização da aplicação para facilitar o deploy e escalabilidade.

## Como Executar

1. **Clone o Repositório**:

    ```bash
    git clone https://github.com/leoromariz/api-controle-de-acao.git

    cd api-controle-de-acao
    ```

2. **Crie um Ambiente Virtual:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # No Windows, use 'env\Scripts\activate'
    ```

3. **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as Variáveis de Ambiente:**

    ```bash
    BRAPI_API_TOKEN=seu_token_aqui
    DATABASE_URL=sqlite:///./test.db  # Ou configure conforme seu banco de dados
    ```
    Execute a Aplicação:

5. **Execute a Aplicação:**

    ```bash
    flask run
    ```
6. **Execute a API:**:

   ```bash
   flask run --host 0.0.0.0 --port 5000
   ```

## Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Fork este repositório.

2. Crie uma branch para sua feature (git checkout -b feature/nome-da-feature).

3. Realize as alterações desejadas.

4. Commit suas mudanças (git commit -am 'Adiciona nova feature').

5. Push para a branch (git push origin feature/nome-da-feature).

6. Abra um Pull Request detalhando suas alterações.
