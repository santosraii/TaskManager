# Gerenciador de Tarefas

Este é um aplicativo de Gerenciamento de Tarefas desenvolvido com Flask, SQLAlchemy e Flask-SocketIO. Ele permite criar, editar, excluir e reordenar tarefas de forma interativa e eficiente.

## Funcionalidades

- Criar tarefas com nome, custo e data limite.
- Editar tarefas existentes.
- Excluir tarefas.
- Reordenar tarefas com arrastar e soltar.
- Mensagens de confirmação para ações como criação, edição e exclusão de tarefas.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- [Python](https://www.python.org/downloads/) (>=3.6)
- [PostgreSQL](https://www.postgresql.org/download/) (>=9.5)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

## Instalação

Siga os passos abaixo para instalar e configurar o projeto em sua máquina local:

1. Clone o repositório:

    ```bash
    git clone https://github.com/santosraii/TaskManager.git
    cd TaskManager
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o PostgreSQL:

    Crie um banco de dados PostgreSQL e um usuário para o seu projeto. Aqui está um exemplo básico de como fazer isso no terminal psql:

    ```sql
    CREATE DATABASE task_manager;
    CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
    ALTER ROLE seu_usuario SET client_encoding TO 'utf8';
    ALTER ROLE seu_usuario SET default_transaction_isolation TO 'read committed';
    ALTER ROLE seu_usuario SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE task_manager TO seu_usuario;
    ```

5. Configure as variáveis de ambiente:

    Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

    ```plaintext
    SQLALCHEMY_DATABASE_URI=postgresql://seu_usuario:sua_senha@localhost/task_manager
    SECRET_KEY=sua_chave_secreta
    ```

    Certifique-se de que seu `config.py` lê essas variáveis de ambiente. Você pode usar a biblioteca `python-dotenv` para isso. Instale-a com:

    ```bash
    pip install python-dotenv
    ```

    E configure seu `config.py` para ler o arquivo `.env`:

    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    ```

6. Inicialize o banco de dados:

    Abra um shell Python e execute:

    ```bash
    python
    ```

    Em seguida, no shell Python:

    ```python
    from app import db
    db.create_all()
    exit()
    ```

## Execução

Para rodar o aplicativo localmente, use o comando:

```bash
python app.py
```

Acesse o aplicativo no navegador em http://127.0.0.1:5000.

## Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir com o projeto:

Fork o repositório.

Crie um branch para a sua feature (git checkout -b feature/nova-feature).

Commit suas alterações (git commit -am 'Adiciona nova feature').

Push para o branch (git push origin feature/nova-feature).

Abra um Pull Request.
