---
id: CKB-DB-0003
title: Entities
module: Database
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: database/
dependencies:
  - modeling.md
  - mysql.md
related:
  - relationships.md
  - normalization.md
  - ../backend/sqlalchemy.md
  - ../backend/repositories.md
last_update: 2026-07
---

# Entidades

## Objetivo

Definir o padrão oficial para modelagem de entidades da Workstation IA.

As entidades representam o núcleo do domínio do sistema.

Toda estrutura de banco de dados deverá nascer a partir das entidades.

---

# Definição

Uma entidade representa um objeto real ou conceitual pertencente ao domínio da aplicação.

Cada entidade possui:

- identidade
- atributos
- relacionamentos
- regras
- ciclo de vida

---

# Filosofia

Toda entidade representa apenas um conceito.

Nunca misturar responsabilidades.

Cada entidade deve possuir identidade própria.

---

# Fluxo Oficial

```
Problema

↓

Domínio

↓

Entidade

↓

Relacionamentos

↓

MER

↓

DER

↓

Model

↓

Repository

↓

Service
```

---

# Características

Uma entidade deverá possuir.

- identidade única
- atributos coerentes
- relacionamentos definidos
- documentação
- responsabilidade única

---

# Identidade

Toda entidade deverá possuir.

```
id

INT

AUTO_INCREMENT

PRIMARY KEY
```

A identidade nunca deverá mudar durante o ciclo de vida da entidade.

---

# Estrutura

Modelo geral.

```
Entidade

↓

Identidade

↓

Atributos

↓

Relacionamentos

↓

Metadados
```

---

# Exemplo

## Usuário

```
id

name

email

password

created_at

updated_at

deleted_at
```

---

## Projeto

```
id

name

description

status_id

user_id

created_at

updated_at
```

---

## Tarefa

```
id

title

description

project_id

status_id

priority

deadline

created_at

updated_at
```

---

# Atributos

Cada atributo deverá representar apenas uma informação.

Evitar campos compostos.

Correto.

```
first_name

last_name
```

Evitar.

```
full_name
```

quando houver necessidade de manipulação.

---

# Tipos

Utilizar tipos apropriados.

```
INT

VARCHAR

TEXT

BOOLEAN

DATE

DATETIME

DECIMAL

FLOAT

JSON
```

---

# Relacionamentos

Toda entidade poderá possuir.

```
1:1

1:N

N:N
```

Todos deverão ser documentados.

---

# Entidades Fortes

Possuem existência própria.

Exemplos.

```
Usuário

Projeto

Equipe

Cliente
```

---

# Entidades Fracas

Dependem de outra entidade.

Exemplos.

```
Comentário

Anexo

Histórico

Log
```

---

# Metadados

Toda entidade deverá possuir.

```
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

# Estado

Sempre que aplicável.

Utilizar.

```
status_id
```

Evitar múltiplos campos booleanos.

---

# Auditoria

Toda entidade crítica deverá registrar.

- criação
- alteração
- exclusão
- responsável

---

# Integridade

A entidade deverá garantir.

- identidade
- consistência
- integridade referencial

---

# Modelos SQLAlchemy

Cada entidade deverá possuir um Model correspondente.

Fluxo.

```
Entidade

↓

Model

↓

Repository

↓

Service
```

---

# Repositories

Cada entidade deverá possuir Repository próprio.

Exemplo.

```
UserRepository

ProjectRepository

TaskRepository
```

---

# Services

Cada entidade deverá possuir Service próprio.

Exemplo.

```
UserService

ProjectService

TaskService
```

---

# Evolução

Novos atributos poderão ser adicionados.

Nunca remover atributos críticos sem migração.

Toda alteração deverá ser versionada.

---

# Documentação

Cada entidade deverá possuir.

- descrição
- finalidade
- atributos
- relacionamentos
- regras
- histórico de alterações

---

# Casos de Uso

Entidades homologadas para a Workstation IA.

- User
- Project
- Task
- Category
- Status
- Team
- Dashboard
- Report
- Notification
- Log
- Audit
- File
- AI Agent
- Prompt
- Workflow
- API Key

---

# Integração

```
MER

↓

DER

↓

SQLAlchemy Model

↓

Repository

↓

Service

↓

Route
```

---

# Boas Práticas

- Uma entidade representa um conceito.
- Evitar duplicação de atributos.
- Utilizar nomes claros.
- Modelar antes de implementar.
- Documentar relacionamentos.
- Versionar alterações estruturais.

---

# Padrão Oficial

Toda entidade da Workstation IA deverá seguir este padrão.

Nenhuma entidade poderá ser implementada sem documentação oficial dentro da Cortex Knowledge Base.

---

# Referências Oficiais

- Domain Driven Design
- Entity Pattern
- SQLAlchemy Documentation
- Clean Architecture
- Evans DDD

---

# Changelog

## 1.0.0

- Documento criado.
- Estrutura oficial de entidades definida.
- Padrões de identidade registrados.
- Integração com SQLAlchemy documentada.