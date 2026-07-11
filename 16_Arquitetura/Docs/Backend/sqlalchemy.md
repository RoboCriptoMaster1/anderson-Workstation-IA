---
id: CKB-BE-0004
title: SQLAlchemy
module: Backend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: backend/
dependencies:
  - python.md
  - flask.md
related:
  - repositories.md
  - services.md
  - routes.md
last_update: 2026-07
---

# SQLAlchemy

## Objetivo

Definir o padrão oficial para utilização do SQLAlchemy na Workstation IA.

SQLAlchemy é o ORM oficial responsável pela persistência de dados da plataforma.

---

# Definição

SQLAlchemy é um ORM (Object Relational Mapper) utilizado para mapear objetos Python em tabelas do banco de dados.

Ele abstrai a escrita manual de SQL e padroniza toda a camada de persistência.

---

# Filosofia

O SQLAlchemy representa a única camada autorizada de comunicação entre a aplicação e o banco de dados.

Nenhuma outra camada deverá acessar o banco diretamente.

---

# Responsabilidades

SQLAlchemy é responsável por:

- ORM
- Sessões
- Persistência
- Relacionamentos
- Consultas
- Transações
- Mapeamento de entidades

---

# Não é responsabilidade

SQLAlchemy não deve conter:

- regras de negócio
- validações
- autenticação
- lógica de interface
- renderização

---

# Arquitetura

```
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

# Fluxo Oficial

```
Request

↓

Service

↓

Repository

↓

SQLAlchemy

↓

MySQL

↓

Repository

↓

Service

↓

Response
```

---

# Estrutura

```
database/

database.py

base.py

session.py

models/

repositories/

migrations/
```

---

# Sessões

Toda operação deverá utilizar uma Session controlada.

Nunca criar sessões espalhadas pela aplicação.

A criação da sessão deverá ser centralizada.

---

# Engine

Uma única Engine por aplicação.

A configuração deverá ser realizada durante a inicialização.

---

# Models

Cada tabela deverá possuir um Model.

Exemplo

```
User

Project

Task

Category

Status
```

---

# Relacionamentos

Utilizar apenas os relacionamentos necessários.

Tipos homologados

- One-to-One
- One-to-Many
- Many-to-One
- Many-to-Many

Sempre documentar relacionamentos complexos.

---

# Chaves Primárias

Padrão oficial

```
Integer

Primary Key

Auto Increment
```

Sempre utilizar nomes consistentes.

Exemplo

```
id

id_user

id_project
```

---

# Convenções

Nomes de tabelas

snake_case

Plural.

Exemplo

```
users

projects

tasks
```

---

# Migrações

Ferramenta oficial

```
Flask-Migrate

Alembic
```

Nunca alterar tabelas manualmente em produção.

Toda alteração estrutural deverá gerar migração.

---

# Queries

Toda consulta deverá ser executada pelos Repositories.

Nunca executar consultas diretamente em:

- Routes
- Services
- Validators
- Forms

---

# Transações

Toda operação crítica deverá utilizar transações.

Em caso de erro.

Rollback obrigatório.

---

# Soft Delete

Sempre que possível utilizar Soft Delete.

Campo padrão.

```
deleted_at
```

ou

```
is_active
```

Evitar exclusões permanentes.

---

# Auditoria

Sempre prever campos.

```
created_at

updated_at

deleted_at

created_by

updated_by
```

---

# Performance

Evitar.

- SELECT *
- consultas N+1
- múltiplos commits
- consultas duplicadas

Utilizar.

- eager loading
- lazy loading quando apropriado
- índices
- paginação

---

# Repositories

SQLAlchemy deverá ser utilizado exclusivamente pelos Repositories.

Fluxo oficial.

```
Service

↓

Repository

↓

SQLAlchemy
```

---

# Segurança

Nunca montar SQL manualmente.

Utilizar ORM.

Evitar SQL Injection.

---

# Configuração

Toda configuração deverá utilizar.

```
.env
```

Nunca expor credenciais.

---

# Banco Oficial

Principal.

```
MySQL
```

Compatível.

- PostgreSQL
- SQLite

---

# Testes

Toda camada de persistência deverá possuir testes.

Prioridade.

- CRUD
- Relacionamentos
- Consultas
- Transações

---

# Integração

```
Python

↓

Flask

↓

Repository

↓

SQLAlchemy

↓

MySQL
```

---

# Bibliotecas Homologadas

- SQLAlchemy
- Flask-Migrate
- Alembic
- PyMySQL
- mysqlclient

---

# Boas Práticas

- Centralizar sessões.
- Criar Models simples.
- Utilizar Repository Pattern.
- Nunca acessar banco fora dos Repositories.
- Utilizar migrações.
- Versionar alterações estruturais.

---

# Padrão Oficial

SQLAlchemy é o ORM oficial da Workstation IA.

Toda comunicação com o banco deverá ocorrer exclusivamente através desta camada.

---

# Referências Oficiais

- SQLAlchemy Documentation
- Alembic Documentation
- Flask-Migrate Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- SQLAlchemy homologado como ORM oficial.
- Arquitetura de persistência definida.
- Convenções de banco registradas.