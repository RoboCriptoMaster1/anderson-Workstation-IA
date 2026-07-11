---
id: CKB-BE-0002
title: Flask
module: Backend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: backend/
dependencies:
  - python.md
  - sqlalchemy.md
related:
  - fastapi.md
  - services.md
  - repositories.md
  - routes.md
last_update: 2026-07
---

# Flask

## Objetivo

Definir o padrão oficial para utilização do Flask na Workstation IA.

Flask é o framework principal responsável pela camada Backend da plataforma.

---

# Definição

Flask é um microframework Python utilizado para construção de aplicações web.

Na Workstation IA ele é responsável pela camada principal da aplicação.

---

# Filosofia

O Flask deve permanecer leve.

Toda complexidade deve ser distribuída entre as camadas da arquitetura.

O framework coordena o fluxo.

As regras pertencem aos Services.

---

# Responsabilidades

Flask é responsável por:

- inicialização da aplicação
- gerenciamento das rotas
- Blueprints
- sessões
- autenticação
- templates
- integração com SQLAlchemy
- configuração da aplicação

---

# Não é responsabilidade

Flask não executa:

- regras de negócio
- consultas SQL
- cálculos
- validações complexas

Essas responsabilidades pertencem às respectivas camadas.

---

# Arquitetura Oficial

```
Flask

↓

Blueprints

↓

Routes

↓

Validators

↓

Forms

↓

Services

↓

Repositories

↓

Models

↓

SQLAlchemy

↓

MySQL
```

---

# Estrutura Oficial

```
app/

__init__.py

routes/

models/

repositories/

services/

validators/

forms/

templates/

static/

config/

instance/

extensions/

middlewares/

tests/
```

---

# Application Factory

Padrão obrigatório.

A aplicação deverá utilizar Factory Pattern.

```
create_app()
```

Toda inicialização deverá ocorrer dentro da Factory.

---

# Blueprints

Toda funcionalidade deverá possuir Blueprint próprio.

Exemplo.

```
auth/

dashboard/

users/

projects/

tasks/

settings/
```

Nunca centralizar todas as rotas em um único arquivo.

---

# Configuração

Toda configuração deverá utilizar Classes.

Exemplo.

```
DevelopmentConfig

TestingConfig

ProductionConfig
```

Nunca espalhar configurações pela aplicação.

---

# Variáveis de Ambiente

Obrigatório utilizar.

```
.env
```

Nunca armazenar:

- senhas
- tokens
- URLs privadas
- API Keys

no código.

---

# Extensões

Toda extensão deverá ficar centralizada.

```
extensions/

database.py

login_manager.py

csrf.py

cache.py
```

---

# Templates

Utilizar Jinja2.

Organização.

```
templates/

layouts/

components/

pages/

partials/
```

---

# Static

Organização.

```
static/

css/

js/

img/

fonts/

icons/
```

---

# Sessões

Utilizar gerenciamento centralizado.

Nunca armazenar informações sensíveis em sessão.

---

# Autenticação

Framework homologado.

```
Flask-Login
```

Complementos.

- JWT quando necessário
- OAuth2 em integrações externas

---

# Banco de Dados

Toda comunicação deverá ocorrer através do SQLAlchemy.

Nunca utilizar SQL diretamente nas Routes.

---

# Fluxo Oficial

```
Request

↓

Blueprint

↓

Route

↓

Validator

↓

Form

↓

Service

↓

Repository

↓

Model

↓

SQLAlchemy

↓

MySQL

↓

Response
```

---

# Organização

Cada módulo deverá possuir.

```
routes

services

repositories

validators

forms
```

---

# Logging

Registrar.

- autenticação
- erros
- integrações
- auditoria

---

# Tratamento de Erros

Centralizar.

```
404

401

403

500
```

Criar páginas específicas.

---

# Testes

Framework oficial.

```
Pytest
```

Testar.

- Services
- Routes
- Repositories

---

# Performance

Priorizar.

- Blueprints
- Lazy Loading quando aplicável
- SQLAlchemy otimizado
- consultas eficientes

---

# Segurança

Obrigatório.

- CSRF
- XSS Protection
- SQL Injection Protection
- HTTPS
- Environment Variables

---

# Integração

```
Flask

↓

SQLAlchemy

↓

MySQL

↓

Jinja2

↓

Bootstrap ou Tailwind

↓

GSAP (Frontend)
```

---

# Bibliotecas Homologadas

- Flask
- Flask-Login
- Flask-Migrate
- Flask-WTF
- Flask-CORS
- Flask-Limiter
- SQLAlchemy
- Python-dotenv

---

# Boas Práticas

- Utilizar Factory Pattern.
- Organizar Blueprints.
- Separar responsabilidades.
- Nunca colocar regra de negócio nas Routes.
- Nunca acessar banco diretamente nas Views.
- Documentar APIs e módulos.

---

# Padrão Oficial

Flask é o framework principal do Backend da Workstation IA.

Toda implementação deverá respeitar a arquitetura oficial definida pelo Cortex.

---

# Referências Oficiais

- Flask Documentation
- Flask Mega Tutorial
- SQLAlchemy Documentation
- Jinja2 Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Flask homologado como framework principal do Backend.
- Arquitetura oficial registrada.
- Padrões de desenvolvimento definidos.