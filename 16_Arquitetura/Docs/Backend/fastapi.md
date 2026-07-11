---
id: CKB-BE-0003
title: FastAPI
module: Backend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: backend/
dependencies:
  - python.md
related:
  - flask.md
  - sqlalchemy.md
  - routes.md
  - services.md
last_update: 2026-07
---

# FastAPI

## Objetivo

Definir o padrão oficial para utilização do FastAPI na Workstation IA.

FastAPI será utilizado para construção de APIs modernas, serviços independentes e componentes de alta performance.

---

# Definição

FastAPI é um framework Python moderno baseado em tipagem estática, projetado para construção de APIs rápidas, escaláveis e bem documentadas.

Na Workstation IA ele complementa o Flask.

---

# Papel na Arquitetura

Flask permanece como framework principal da aplicação.

FastAPI será utilizado para:

- APIs públicas
- APIs internas
- Microserviços
- Serviços de IA
- Processamentos assíncronos
- Integrações externas

---

# Filosofia

Flask controla a aplicação.

FastAPI expõe serviços.

Cada framework possui responsabilidades específicas.

---

# Responsabilidades

FastAPI será responsável por:

- APIs REST
- documentação automática
- validação de dados
- processamento assíncrono
- autenticação por API
- integração entre módulos
- comunicação externa

---

# Não é responsabilidade

FastAPI não substitui:

- Flask
- Jinja2
- Templates
- Interface Web

---

# Arquitetura

```
Cliente

↓

FastAPI

↓

Routes

↓

Services

↓

Repositories

↓

SQLAlchemy

↓

MySQL
```

---

# Estrutura Oficial

```
api/

main.py

routers/

services/

repositories/

schemas/

models/

middlewares/

dependencies/

config/

tests/
```

---

# Inicialização

Arquivo principal

```
main.py
```

Responsável por:

- criar aplicação
- registrar rotas
- middlewares
- documentação

---

# Routers

Cada domínio deverá possuir Router próprio.

Exemplo

```
users.py

projects.py

tasks.py

dashboard.py

ai.py
```

---

# Schemas

Utilizar Pydantic.

Separar:

```
Request

↓

Response

↓

Shared Models
```

Nunca utilizar Models do banco diretamente nas respostas.

---

# Tipagem

Obrigatória.

Toda rota deverá possuir:

- tipos de entrada
- tipos de retorno
- documentação automática

---

# Async

Utilizar:

```python
async

await
```

Sempre que houver ganho real.

Evitar processamento síncrono em rotas críticas.

---

# Documentação

FastAPI deverá disponibilizar:

```
Swagger UI

/docs
```

e

```
ReDoc

/redoc
```

Essas documentações fazem parte da arquitetura oficial.

---

# Versionamento

As APIs deverão ser versionadas.

Exemplo

```
/api/v1/

/api/v2/
```

---

# Autenticação

Padrões homologados

- JWT
- OAuth2
- Bearer Token

---

# Banco de Dados

Toda persistência deverá utilizar:

```
SQLAlchemy
```

Nunca acessar banco diretamente nas rotas.

---

# Tratamento de Erros

Centralizar exceções.

Retornar respostas padronizadas.

Exemplo

```json
{
    "success": false,
    "message": "...",
    "code": "...",
    "details": []
}
```

---

# Estrutura de Resposta

Sucesso

```json
{
    "success": true,
    "data": {}
}
```

Erro

```json
{
    "success": false,
    "message": ""
}
```

---

# Performance

Priorizar:

- Async
- Tipagem
- Validação
- Processamentos independentes

---

# Segurança

Obrigatório

- HTTPS
- JWT
- Rate Limiting
- CORS
- Environment Variables

---

# Casos de Uso

- API da Workstation IA
- API do Cortex
- Integrações com IA
- Integrações MCP
- Dashboards
- Aplicativos Mobile
- Integrações de terceiros

---

# Integração

```
FastAPI

↓

Services

↓

Repositories

↓

SQLAlchemy

↓

MySQL

↓

JSON
```

---

# Bibliotecas Homologadas

- FastAPI
- Pydantic
- SQLAlchemy
- Uvicorn
- Alembic
- Python-dotenv

---

# Boas Práticas

- Utilizar tipagem em toda API.
- Separar Routers por domínio.
- Utilizar Pydantic.
- Versionar APIs.
- Documentar endpoints.
- Não implementar regras de negócio nas rotas.

---

# Padrão Oficial

FastAPI é o framework oficial para APIs e microserviços da Workstation IA.

Flask continua sendo o framework principal da aplicação.

Ambos coexistem de forma complementar.

---

# Referências Oficiais

- FastAPI Documentation
- Pydantic Documentation
- Uvicorn Documentation
- SQLAlchemy Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- FastAPI homologado para APIs e microserviços.
- Arquitetura oficial definida.
- Padrões de integração registrados.