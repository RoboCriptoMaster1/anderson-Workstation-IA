---
id: CKB-KNOW-0004
title: Conventions
module: Knowledge
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: knowledge/
dependencies:
  - architecture.md
  - glossary.md
related:
  - roadmap.md
  - decisions.md
  - ../backend/python.md
  - ../frontend/javascript.md
last_update: 2026-07
---

# Convenções

## Objetivo

Definir as convenções oficiais da Workstation IA.

Este documento estabelece os padrões utilizados em código, documentação, banco de dados, APIs, Git, arquitetura e organização do projeto.

Todo módulo deverá seguir estas convenções.

---

# Filosofia

Padronização reduz complexidade.

Código consistente é mais importante que código individualmente elegante.

Toda decisão deverá privilegiar legibilidade, previsibilidade e manutenção.

---

# Hierarquia

```
Arquitetura

↓

Convenções

↓

Código

↓

Documentação

↓

Deploy
```

---

# Idioma Oficial

Código

```
English
```

Documentação

```
Português
```

Interface

Configurável.

---

# Estrutura de Pastas

Padrão.

```
core/

frontend/

backend/

database/

api/

ai/

knowledge/

security/

devops/

testing/

scripts/

docs/
```

---

# Arquivos

Utilizar.

```
snake_case
```

Exemplo.

```
user_service.py

database_backup.md

task_routes.py
```

Nunca utilizar.

```
UserService.py

MeuArquivo.py

Arquivo Final.py
```

---

# Diretórios

Utilizar.

```
snake_case
```

---

# Classes

Utilizar.

```
PascalCase
```

Exemplos.

```
UserService

ProjectRepository

DashboardController

DatabaseManager
```

---

# Interfaces

Quando aplicável.

Prefixo.

```
I
```

Exemplo.

```
IRepository

IStorageProvider
```

---

# Métodos

Utilizar.

```
snake_case
```

Exemplos.

```
create_user()

find_project()

delete_task()

update_dashboard()
```

---

# Variáveis

Utilizar.

```
snake_case
```

Exemplo.

```
user_name

project_status

database_connection
```

---

# Constantes

Utilizar.

```
UPPER_CASE
```

Exemplo.

```
MAX_USERS

DEFAULT_TIMEOUT

API_VERSION
```

---

# Banco de Dados

Tabelas.

```
snake_case

plural
```

Exemplo.

```
users

projects

tasks

categories
```

---

# Colunas

Utilizar.

```
snake_case
```

Exemplo.

```
created_at

updated_at

deleted_at

user_id
```

---

# Chaves

Primária.

```
id
```

Estrangeiras.

```
user_id

project_id

status_id
```

---

# APIs

Endpoints.

```
/api/v1/users

/api/v1/projects

/api/v1/tasks
```

Utilizar substantivos.

Nunca verbos.

---

# HTTP

Padrão.

```
GET

POST

PUT

PATCH

DELETE
```

---

# JSON

Utilizar.

```
camelCase
```

Exemplo.

```json
{
  "userName": "",
  "projectStatus": ""
}
```

---

# Git

Branch principal.

```
main
```

Desenvolvimento.

```
develop
```

Features.

```
feature/

bugfix/

hotfix/

release/
```

---

# Commits

Padrão.

```
feat:

fix:

docs:

style:

refactor:

test:

perf:

build:

ci:

chore:
```

Exemplo.

```
feat: add task dashboard

fix: correct login validation

docs: update README
```

---

# Versionamento

Utilizar.

```
Semantic Versioning
```

Formato.

```
MAJOR.MINOR.PATCH
```

Exemplo.

```
1.0.0

1.1.0

1.1.3

2.0.0
```

---

# Markdown

Todo documento deverá possuir.

- metadata
- objetivo
- definição
- arquitetura
- fluxo
- boas práticas
- padrão oficial
- changelog

---

# Comentários

Comentar apenas quando necessário.

Explicar.

- decisões
- algoritmos complexos
- regras de negócio

Nunca comentar código óbvio.

---

# Imports

Ordem.

```
Bibliotecas padrão

↓

Bibliotecas externas

↓

Módulos internos
```

---

# Logs

Formato.

```
Data

Hora

Nível

Origem

Mensagem
```

---

# Testes

Nome.

```
test_user_service.py

test_routes.py

test_database.py
```

---

# Docker

Arquivos.

```
Dockerfile

docker-compose.yml

.dockerignore
```

---

# Variáveis de Ambiente

Arquivo.

```
.env
```

Nunca versionar.

---

# Documentação

Todos os módulos deverão possuir.

```
README.md
```

---

# Segurança

Nunca publicar.

- senhas
- tokens
- chaves
- credenciais

---

# Inteligência Artificial

Toda documentação de IA deverá seguir.

```
ai/

claude.md

cortex.md

memory.md

rag.md

mcp.md
```

---

# Knowledge Base

Todo documento deverá possuir.

```
CKB-ID
```

Único.

---

# Checklist

Antes de criar código.

- Segue arquitetura?

- Segue convenções?

- Está documentado?

- Está versionado?

- Está testado?

---

# Boas Práticas

- Escrever código limpo.
- Utilizar nomes descritivos.
- Evitar abreviações.
- Documentar decisões.
- Manter consistência.
- Reutilizar componentes.
- Seguir a arquitetura oficial.

---

# Padrão Oficial

Todas as convenções da Workstation IA são definidas por este documento.

Nenhum módulo poderá utilizar convenções próprias.

Toda a plataforma deverá permanecer consistente.

---

# Referências Oficiais

- PEP 8
- Google Python Style Guide
- Conventional Commits
- Semantic Versioning 2.0
- REST API Design Guidelines
- Clean Code
- Clean Architecture

---

# Changelog

## 1.0.0

- Documento criado.
- Convenções oficiais definidas.
- Padrões de nomenclatura estabelecidos.
- Convenções de Git, APIs, banco e documentação homologadas.