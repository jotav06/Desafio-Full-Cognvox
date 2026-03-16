# Sistema de Login - COGNVOX

Projeto desenvolvido como desafio técnico da residência do Projeto Bolsa Futuro Digital da SOFTEX-PE junto à empresa COGNVOX. Trata-se de um sistema de autenticação utilizando **Flask**, **MySQL** e **JWT**, com arquitetura organizada em **routes, controllers, services e middlewares**.

---

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- JWT(PyJWT)
- Bcrypt
- Flask-CORS
- HTML / CSS

---

## Estrutura do projeto
```

Desafio-Full-Cognvox
│
├── backend
│ ├── app.py
│ ├── database.py
│ ├── controllers
│ │ └── auth_controller.py
│ │
│ ├── services
│ │ └── auth_service.py
│ │
│ ├── routes
│ │ └── auth_routes.py
│ │
│ └── middlewares
│ └── auth_middleware.py
│
├── frontend
│ ├── templates
│ │ ├── login.html
│ │ └── dashboard.html
│ │
│ └── static
│ ├── css
│ └── img
```
---

## Funcionalidades

- Login de usuário
- Autenticação com **JWT**
- Proteção de rotas com **middleware**
- Hash de senha com **bcrypt**
- Criação automática de banco e tabelas
- Usuário inicial criado automaticamente

--- 

## Variáveis de ambiente

Crie um arquivo .env na pasta **backend**:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=login_cognvox

SECRET_KEY=super_secret_key
```
---

## Como executar o projeto

### 1 Clonar o repositório

git clone https://github.com/jotav06/Desafio-Full-Cognvox.git

### 2 Entrar na pasta backend

cd backend

### 3 Instalar dependências

pip install -r requirements.txt

### 4 Executar o projeto

python app.py

O servidor iniciará em:

http://localhost:5000

---

## Usuário padrão

O sistema cria automaticamente um usuário inicial:
```
Email : admin@email.com
Senha: 123456
```

---

## Autor

   <td align="center">
      <a href="https://github.com/jotav06">
        <img src="https://github.com/jotav06.png" width="100" style="border-radius:50%"><br>
        <sub><b>João Victor Silva</b></sub>
      </a>
    </td>






