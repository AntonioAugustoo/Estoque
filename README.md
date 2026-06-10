# 📦 Estoque API — C216 Inatel

Este projeto foi desenvolvido como **Projeto Final** da disciplina **C216 — Laboratório de Sistemas Distribuídos** no **Inatel**. O objetivo é construir um sistema completo de controle de estoque com backend, frontend e banco de dados, orquestrado via Docker Compose.

---

## 🚀 O Projeto

O sistema permite o gerenciamento de produtos, categorias e fornecedores através de uma interface web e uma API REST completa. A aplicação roda inteiramente em containers Docker, sem necessidade de instalação manual de dependências.

### ✅ Funcionalidades

- Cadastro, listagem e remoção de **produtos**
- Cadastro, listagem e remoção de **categorias**
- Cadastro, listagem e remoção de **fornecedores**
- Vinculação de fornecedores a produtos (relação N para M)
- Dashboard com totais em tempo real
- Testes automatizados do backend

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-----------|
| Backend | FastAPI + Python |
| Banco de dados | PostgreSQL |
| Frontend | HTML + CSS + JavaScript |
| Servidor web | Nginx |
| Testes | Pytest + HTTPX + Anyio |
| Orquestração | Docker + Docker Compose |

---

## 📁 Estrutura do Projeto

```
estoque-api/
├── backend/
│   ├── db/
│   │   ├── connection.py       ← Conexão assíncrona com o banco
│   │   └── init.sql            ← Schema e criação das tabelas
│   ├── routes/
│   │   ├── categorias.py       ← Endpoints de categorias
│   │   ├── fornecedores.py     ← Endpoints de fornecedores
│   │   └── produtos.py         ← Endpoints de produtos
│   ├── schemas/
│   │   ├── categoria.py        ← Modelos Pydantic de categoria
│   │   ├── fornecedor.py       ← Modelos Pydantic de fornecedor
│   │   └── produto.py          ← Modelos Pydantic de produto
│   ├── services/
│   │   ├── categoria_service.py
│   │   ├── fornecedor_service.py
│   │   └── produto_service.py
│   ├── tests/
│   │   └── test_api.py         ← Testes automatizados
│   ├── main.py                 ← Entrypoint da API
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       ├── main.js         ← Dashboard
│   │       ├── produtos.js     ← Página de produtos
│   │       └── categorias.js   ← Página de categorias
│   ├── index.html              ← Dashboard
│   ├── produtos.html           ← Gerenciamento de produtos
│   ├── categorias.html         ← Gerenciamento de categorias e fornecedores
│   ├── nginx.conf
│   └── Dockerfile
│
├── .env                        ← Variáveis de ambiente (não versionado)
├── docker-compose.yml
└── README.md
```

---

## 🗄️ Estrutura do Banco de Dados

```
categorias          fornecedores
│                   │
│  N:1              │  N:M
▼                   ▼
produtos ──────── produto_fornecedor
```

| Tabela | Descrição |
|--------|-----------|
| `categorias` | Categorias dos produtos |
| `fornecedores` | Fornecedores cadastrados |
| `produtos` | Produtos do estoque, vinculados a uma categoria |
| `produto_fornecedor` | Tabela de junção N:M entre produtos e fornecedores |

---

## 🔌 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Healthcheck da API |
| GET | `/produtos/` | Listar todos os produtos |
| GET | `/produtos/{id}` | Buscar produto por ID |
| POST | `/produtos/` | Criar produto |
| PUT | `/produtos/{id}` | Atualizar produto |
| DELETE | `/produtos/{id}` | Deletar produto |
| POST | `/produtos/{id}/fornecedores` | Vincular fornecedor ao produto |
| GET | `/produtos/{id}/fornecedores` | Listar fornecedores do produto |
| GET | `/categorias/` | Listar categorias |
| GET | `/categorias/{id}` | Buscar categoria por ID |
| POST | `/categorias/` | Criar categoria |
| DELETE | `/categorias/{id}` | Deletar categoria |
| GET | `/fornecedores/` | Listar fornecedores |
| GET | `/fornecedores/{id}` | Buscar fornecedor por ID |
| POST | `/fornecedores/` | Criar fornecedor |
| DELETE | `/fornecedores/{id}` | Deletar fornecedor |

A documentação interativa completa está disponível em `http://localhost:8000/docs` após subir o projeto.

---

## ▶️ Como Executar

**Pré-requisitos:** Docker e Docker Compose instalados.

**1. Clone o repositório:**
```bash
git clone https://github.com/AntonioAugustoo/estoque-api.git
cd estoque-api
```

**2. Crie o arquivo `.env` na raiz:**
```env
POSTGRES_USER=estoque_user
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=estoque_db
```

**3. Suba os containers:**
```bash
docker compose up --build
```

**4. Acesse a aplicação:**

| Serviço | URL |
|---------|-----|
| Frontend | http://localhost |
| API | http://localhost:8000 |
| Documentação | http://localhost:8000/docs |

---

## 🧪 Executando os Testes

Com os containers rodando, os testes sobem automaticamente junto com o projeto. Para rodar manualmente:

```bash
docker compose run --rm tests
```

---

## 👤 Autor

**Antonio Augusto D'Assumpção**
Matrícula: 221
Inatel — Instituto Nacional de Telecomunicações
C216 — Laboratório de Sistemas Distribuídos