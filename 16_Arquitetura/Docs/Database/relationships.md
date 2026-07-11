---
id: CKB-DB-0004
title: Relationships
module: Database
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: database/
dependencies:
  - modeling.md
  - entities.md
related:
  - normalization.md
  - migrations.md
  - ../backend/sqlalchemy.md
last_update: 2026-07
---

# Relacionamentos

## Objetivo

Definir o padrão oficial para modelagem de relacionamentos entre entidades da Workstation IA.

Os relacionamentos representam como as entidades interagem entre si e garantem a integridade do domínio da aplicação.

---

# Definição

Relacionamentos descrevem a associação entre duas ou mais entidades.

Toda relação deverá representar uma regra real do domínio.

Nunca criar relacionamentos apenas por conveniência técnica.

---

# Filosofia

Os relacionamentos devem refletir a realidade do negócio.

Modelar primeiro o domínio.

Depois implementar o banco.

Nunca o contrário.

---

# Fluxo Oficial

```
Domínio

↓

Entidades

↓

Relacionamentos

↓

MER

↓

DER

↓

SQL

↓

SQLAlchemy
```

---

# Tipos Oficiais

A Workstation IA utiliza quatro tipos de relacionamento.

```
1:1

1:N

N:1

N:N
```

---

# Um para Um (1:1)

Uma entidade possui apenas uma correspondente.

Exemplos

```
Usuário

↓

Perfil
```

```
Empresa

↓

Configuração
```

Utilizar somente quando existir dependência exclusiva.

---

# Um para Muitos (1:N)

Relacionamento mais comum.

Exemplo

```
Usuário

↓

Projetos
```

Um usuário pode possuir vários projetos.

Cada projeto pertence a apenas um usuário.

---

# Muitos para Um (N:1)

Representa o lado inverso.

Exemplo

```
Projeto

↓

Usuário
```

---

# Muitos para Muitos (N:N)

Sempre utilizar tabela intermediária.

Nunca implementar diretamente.

Exemplo

```
Usuário

↓

user_roles

↓

Role
```

Outro exemplo.

```
Projeto

↓

project_members

↓

Usuário
```

---

# Tabelas Associativas

Toda relação N:N deverá possuir tabela própria.

Exemplo.

```
project_users

task_tags

user_roles

project_permissions
```

Essas tabelas poderão possuir atributos adicionais.

---

# Chaves Estrangeiras

Todo relacionamento deverá utilizar Foreign Keys.

Exemplo.

```
project.user_id

↓

users.id
```

Nunca criar relacionamentos implícitos.

---

# Integridade Referencial

Obrigatória.

Toda Foreign Key deverá possuir política explícita.

---

# ON DELETE

Preferência oficial.

```
RESTRICT
```

ou

```
SET NULL
```

```
CASCADE
```

somente quando fizer sentido para o domínio.

---

# ON UPDATE

Preferência.

```
CASCADE
```

---

# Cardinalidade

Toda relação deverá ser documentada.

Exemplo.

```
Usuário

1

↓

N

Projetos
```

---

# Relacionamentos Circulares

Evitar.

Quando inevitáveis.

Documentar completamente.

---

# Relacionamentos Opcionais

Sempre utilizar NULL quando fizer sentido.

Nunca utilizar valores fictícios.

---

# Relacionamentos Obrigatórios

Utilizar.

```
NOT NULL
```

quando o domínio exigir.

---

# SQLAlchemy

Relacionamentos deverão utilizar.

```
relationship()

ForeignKey()

back_populates
```

Evitar relacionamentos não documentados.

---

# Performance

Relacionamentos deverão considerar.

- índices
- joins
- paginação
- eager loading
- lazy loading

Evitar consultas N+1.

---

# Documentação

Todo relacionamento deverá possuir.

- origem
- destino
- cardinalidade
- descrição
- regra de negócio

---

# Exemplos Oficiais

## Usuário → Projetos

```
1:N
```

---

## Projeto → Tarefas

```
1:N
```

---

## Categoria → Tarefas

```
1:N
```

---

## Status → Tarefas

```
1:N
```

---

## Usuário ↔ Equipes

```
N:N
```

Tabela associativa.

```
team_users
```

---

## Projeto ↔ Usuários

```
N:N
```

Tabela.

```
project_members
```

---

# Fluxo Arquitetural

```
Entidade

↓

Relacionamento

↓

Model SQLAlchemy

↓

Repository

↓

Service

↓

Interface
```

---

# Casos de Uso

Relacionamentos homologados.

- Usuário → Projeto
- Projeto → Tarefa
- Usuário → Comentário
- Projeto → Arquivo
- Dashboard → Widgets
- Usuário ↔ Permissões
- Equipe ↔ Usuários
- Workflow ↔ Etapas
- IA ↔ Prompts

---

# Boas Práticas

- Sempre utilizar Foreign Keys.
- Documentar cardinalidade.
- Evitar redundância.
- Utilizar tabelas associativas em N:N.
- Nunca criar relacionamentos implícitos.
- Modelar primeiro, implementar depois.

---

# Padrão Oficial

Todo relacionamento da Workstation IA deverá seguir este documento.

Nenhuma associação entre entidades poderá existir sem documentação na Cortex Knowledge Base.

---

# Referências Oficiais

- MySQL Documentation
- SQLAlchemy ORM Relationships
- Crow's Foot Notation
- Domain Driven Design
- Database Design Best Practices

---

# Changelog

## 1.0.0

- Documento criado.
- Relacionamentos oficiais definidos.
- Cardinalidades padronizadas.
- Regras de integridade documentadas.