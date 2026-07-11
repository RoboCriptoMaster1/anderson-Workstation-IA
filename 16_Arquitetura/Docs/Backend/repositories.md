---
id: CKB-BE-0006
title: Repositories
module: Backend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: backend/
dependencies:
  - sqlalchemy.md
  - services.md
related:
  - models.md
  - routes.md
last_update: 2026-07
---

# Repositories

## Objetivo

Definir o padrão oficial da camada Repository da Workstation IA.

Esta camada é responsável exclusivamente pela persistência dos dados.

---

# Definição

Repository é a camada intermediária entre os Services e o banco de dados.

Sua responsabilidade é abstrair completamente o acesso ao banco de dados.

Nenhuma outra camada poderá acessar diretamente o SQLAlchemy.

---

# Filosofia

Repository não toma decisões.

Repository não possui regras de negócio.

Repository apenas fornece dados.

---

# Responsabilidades

Os Repositories são responsáveis por:

- consultas
- inserções
- atualizações
- exclusões
- paginação
- filtros
- ordenação
- persistência

---

# Não é responsabilidade

Repositories nunca devem:

- validar regras
- autenticar usuários
- calcular valores
- renderizar páginas
- responder requisições HTTP
- controlar permissões
- acessar templates

Essas responsabilidades pertencem aos Services.

---

# Arquitetura

```
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

SQLAlchemy

↓

MySQL
```

---

# Fluxo Oficial

```
Service

↓

Repository

↓

Session

↓

Model

↓

SQLAlchemy

↓

MySQL
```

---

# Estrutura

```
repositories/

user_repository.py

project_repository.py

task_repository.py

category_repository.py

status_repository.py
```

Cada entidade deverá possuir seu próprio Repository.

---

# Nomeação

Sempre utilizar.

```
UserRepository

ProjectRepository

TaskRepository

DashboardRepository
```

---

# Métodos

Os métodos deverão representar operações de persistência.

Exemplos.

```
find_by_id()

find_all()

find_by_email()

create()

update()

delete()

exists()

count()

paginate()
```

Evitar nomes vagos.

---

# Sessão

Toda operação deverá utilizar a sessão oficial da aplicação.

Nunca criar sessões locais.

---

# SQLAlchemy

O SQLAlchemy somente poderá ser utilizado nesta camada.

Nenhuma outra camada poderá realizar consultas diretamente.

---

# Models

Repositories trabalham diretamente com Models.

Fluxo.

```
Repository

↓

Model

↓

SQLAlchemy

↓

Banco
```

---

# Services

Services nunca acessam o banco.

Toda comunicação ocorre através dos Repositories.

```
Service

↓

Repository
```

---

# Queries

Toda consulta deverá possuir objetivo específico.

Evitar métodos genéricos.

Correto.

```
find_user_by_email()

find_active_projects()

find_tasks_by_project()
```

Evitar.

```
search()

find()

execute()
```

---

# Paginação

Toda listagem grande deverá possuir paginação.

Nunca retornar milhares de registros desnecessariamente.

---

# Ordenação

Sempre permitir ordenação quando aplicável.

---

# Filtros

Implementar filtros reutilizáveis.

Evitar duplicação de consultas.

---

# Soft Delete

Quando adotado.

Repository será responsável por respeitar a política de exclusão lógica.

---

# Transações

Repositories não controlam regras.

Mas devem participar corretamente das transações abertas pelos Services.

---

# Performance

Priorizar.

- índices
- eager loading
- lazy loading quando apropriado
- consultas específicas
- paginação

Evitar.

- SELECT *
- consultas duplicadas
- N+1 Queries

---

# Logs

Repositories não deverão registrar regras.

Logs estruturais poderão existir para auditoria quando necessário.

---

# Tratamento de Erros

Erros de persistência deverão ser propagados aos Services.

Não ocultar exceções.

---

# Testabilidade

Cada Repository deverá possuir testes próprios.

Testar.

- CRUD
- filtros
- consultas
- paginação
- relacionamentos

---

# Dependency Injection

Repositories deverão ser injetados nos Services.

Evitar instanciá-los diretamente dentro das regras de negócio.

---

# Integração

```
Service

↓

Repository

↓

SQLAlchemy

↓

MySQL
```

---

# Exemplo de Organização

```
repositories/

UserRepository

ProjectRepository

TaskRepository

CategoryRepository

StatusRepository
```

---

# Boas Práticas

- Uma entidade por Repository.
- Métodos pequenos.
- Consultas reutilizáveis.
- Nunca implementar regra de negócio.
- Nunca responder HTTP.
- Nunca acessar templates.
- Documentar consultas complexas.

---

# Padrão Oficial

Repositories representam a única camada autorizada para acesso ao banco de dados.

Qualquer acesso direto ao SQLAlchemy fora desta camada será considerado uma violação da arquitetura oficial do Cortex.

---

# Referências Oficiais

- Repository Pattern
- SQLAlchemy Documentation
- Clean Architecture
- Domain Driven Design
- Patterns of Enterprise Application Architecture

---

# Changelog

## 1.0.0

- Documento criado.
- Repository Pattern oficializado.
- Fluxo de persistência definido.
- Padrões arquiteturais registrados.