---
id: CKB-DB-0001
title: MySQL
module: Database
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: database/
dependencies:
  - ../backend/sqlalchemy.md
  - ../backend/repositories.md
related:
  - modeling.md
  - migrations.md
  - indexing.md
  - security.md
last_update: 2026-07
---

# MySQL

## Objetivo

Definir o padrão oficial para utilização do MySQL na Workstation IA.

O MySQL é o Sistema Gerenciador de Banco de Dados (SGBD) principal da plataforma.

---

# Definição

MySQL é um banco de dados relacional utilizado para armazenar todas as informações persistentes da Workstation IA.

Toda persistência oficial deverá utilizar MySQL.

---

# Filosofia

O banco de dados representa a memória permanente da plataforma.

Sua estrutura deve ser:

- consistente
- normalizada
- escalável
- documentada
- segura
- performática

---

# Responsabilidades

O MySQL é responsável por:

- persistência
- relacionamentos
- transações
- integridade
- índices
- consultas
- auditoria

---

# Não é responsabilidade

O banco de dados nunca deverá conter:

- regras de negócio
- autenticação
- lógica da aplicação
- regras de interface
- processamento de IA

Essas responsabilidades pertencem às camadas superiores.

---

# Arquitetura

```
Frontend

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

# Banco Oficial

Principal

```
MySQL 8.x
```

Compatíveis

- PostgreSQL
- SQLite (desenvolvimento)

---

# Engine

Padrão oficial

```
InnoDB
```

Motivos

- transações
- integridade referencial
- Foreign Keys
- rollback
- alta confiabilidade

---

# Charset

Obrigatório

```
utf8mb4
```

Collation

```
utf8mb4_unicode_ci
```

---

# Time Zone

Padrão

```
UTC
```

Toda conversão de horário deverá ocorrer na aplicação.

---

# Convenções

## Banco

snake_case

Exemplo

```
workstation_ia
```

---

## Tabelas

Plural

snake_case

Exemplo

```
users

projects

tasks

categories

status
```

---

## Colunas

snake_case

Exemplo

```
first_name

created_at

updated_at

deleted_at

project_id
```

---

## Chaves Primárias

Padrão

```
id
```

Tipo

```
INT AUTO_INCREMENT
```

---

## Chaves Estrangeiras

Sempre utilizar

```
nome_da_tabela_id
```

Exemplo

```
user_id

project_id

status_id

category_id
```

---

# Campos Obrigatórios

Toda tabela deverá possuir.

```
id

created_at

updated_at
```

Preferencialmente.

```
deleted_at

created_by

updated_by
```

---

# Integridade

Obrigatório utilizar.

- Primary Key
- Foreign Key
- Unique
- Not Null
- Default
- Check (quando suportado)

---

# Relacionamentos

Tipos homologados.

- 1:1
- 1:N
- N:N

Toda relação deverá ser documentada.

---

# Transações

Toda operação crítica deverá utilizar.

```
BEGIN

COMMIT

ROLLBACK
```

---

# Índices

Criar índices para.

- Foreign Keys
- Campos de busca
- Login
- Email
- Datas
- Relatórios

Evitar índices desnecessários.

---

# Soft Delete

Padrão oficial.

```
deleted_at
```

Evitar exclusões permanentes.

---

# Auditoria

Campos recomendados.

```
created_at

updated_at

deleted_at

created_by

updated_by
```

---

# Performance

Priorizar.

- índices
- consultas específicas
- paginação
- relacionamentos corretos
- normalização

Evitar.

- SELECT *
- tabelas gigantes
- consultas N+1
- duplicação

---

# Segurança

Nunca permitir.

- SQL Injection
- usuários sem privilégio
- acesso root pela aplicação
- credenciais no código

Sempre utilizar.

```
.env
```

---

# Backup

Estratégia oficial.

- backup diário
- backup completo semanal
- testes periódicos de restauração

---

# Versionamento

Toda alteração estrutural deverá utilizar.

```
Flask-Migrate

Alembic
```

Nunca alterar produção manualmente.

---

# Integração

```
Flask

↓

SQLAlchemy

↓

MySQL

↓

Backup

↓

Logs
```

---

# Ferramentas Homologadas

- MySQL Server
- MySQL Workbench
- SQLAlchemy
- Flask-Migrate
- Alembic
- PyMySQL

---

# Boas Práticas

- Utilizar InnoDB.
- Utilizar UTF8MB4.
- Criar índices corretamente.
- Normalizar tabelas.
- Utilizar Foreign Keys.
- Documentar alterações.
- Nunca acessar banco fora dos Repositories.

---

# Padrão Oficial

MySQL é o banco de dados oficial da Workstation IA.

Toda persistência deverá seguir os padrões definidos neste documento e na arquitetura oficial do Cortex.

---

# Referências Oficiais

- MySQL Documentation
- MySQL Reference Manual
- SQL Style Guide
- SQLAlchemy Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- MySQL homologado como SGBD oficial.
- Convenções de banco definidas.
- Arquitetura de persistência documentada.