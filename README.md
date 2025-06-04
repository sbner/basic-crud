# Notes App

Uma aplicação baseada em Django para gerenciar notas.

## Integrantes do Grupo

- Danilo Guarnieri de Menezes - 2084396
- Matheus Abner Ramos Miranda - 2093503
- Kauan Rios De Melo - 2900830
- Victor Teixeira - 1979909
- Thais Alves da Costa - 3143248

## Pré-requisitos para rodar a aplicação localmente

* Python 3.x (testado com Python 3.11)
* pip (instalador de pacotes Python)
* Git

## Configuração e Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <repository_url>  # Substitua <repository_url> pela URL real deste projeto
    cd <repository_directory> # Substitua <repository_directory> pelo nome do diretório clonado (ex: django-notes-app)
    ```

2.  **Crie e ative um ambiente virtual:**
    * **No macOS e Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **No Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instale as dependências:**
    Certifique-se de que seu ambiente virtual esteja ativado.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    Este projeto usa SQLite por padrão. O arquivo `db.sqlite3` será criado na raiz do projeto se não existir.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, para acessar a interface de administração do Django):**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções na tela para configurar um nome de usuário administrador, email (opcional) e senha.

## Executando o Servidor de Desenvolvimento

1.  **Inicie o servidor:**
    Certifique-se de que seu ambiente virtual esteja ativado.
    ```bash
    python manage.py runserver
    ```

2.  **Acesse a aplicação:**
    Abra seu navegador e acesse `http://127.0.0.1:8000/`.
    * A aplicação principal de notas estará disponível na URL raiz.
    * Se você criou um superusuário, a interface de administração do Django pode ser acessada em `http://127.0.0.1:8000/admin/`.

## Como Usar

Assim que o servidor de desenvolvimento estiver em execução, você pode interagir com o Notes App através do seu navegador.

1.  **Visualizar todas as notas:** Acesse a página principal navegando para `http://127.0.0.1:8000/`. Isso mostrará uma lista de todas as notas existentes.
2.  **Criar uma nova nota:** Clique no botão "Criar Nota" (ou navegue diretamente para `http://127.0.0.1:8000/create`). Preencha os campos do formulário (Título, Descrição, Prazo) e envie.
3.  **Atualizar uma nota:** Na página principal da lista, encontre a nota que deseja editar e clique no link "Editar" ao lado dela. Modifique os campos no formulário e envie.
4.  **Excluir uma nota:** Na página principal da lista, encontre a nota que deseja excluir e clique no link "Excluir" ao lado dela. Será solicitada a confirmação da exclusão.
5.  **Marcar uma nota como concluída:** Na página principal da lista, encontre a nota que deseja marcar como finalizada e clique no link "Concluir" ao lado dela.

Estas ações são realizadas diretamente através da interface web fornecida pela aplicação.

## Parando o Servidor

Para parar o servidor de desenvolvimento, pressione `Ctrl+C` no terminal onde o servidor está em execução.

## Desativando o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual executando:
```bash
deactivate
```

Este comando funciona no macOS, Linux e Windows (Git Bash ou PowerShell).