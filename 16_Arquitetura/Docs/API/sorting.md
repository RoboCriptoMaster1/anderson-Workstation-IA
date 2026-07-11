---
id: CKB-API-0017
title: Sorting
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - filtering.md
  - pagination.md
  - endpoints.md
related:
  - requests.md
  - responses.md
  - graphql.md
  - sdk.md
last_update: 2026-07
---

# Sorting

## Objetivo

Definir oficialmente a arquitetura de ordenação da Workstation IA.

Este documento estabelece como listas de dados deverão ser ordenadas em toda a plataforma, garantindo consistência, previsibilidade e alto desempenho.

Toda ordenação deverá seguir este padrão.

---

# Filosofia

Ordenar é organizar.

Uma ordenação consistente facilita navegação, paginação, auditoria e análise.

Toda coleção deverá possuir uma ordem determinística.

---

# Missão

Disponibilizar mecanismos padronizados de ordenação para APIs REST, GraphQL, SDKs, Cortex e ferramentas MCP.

---

# Arquitetura

```
Cliente

↓

Request

↓

Validation

↓

Filtering

↓

Sorting

↓

Pagination

↓

Repository

↓

Database

↓

Response
```

---

# Estrutura Oficial

Parâmetros.

```
sort

order
```

Exemplo.

```
GET

/api/v1/users?sort=name&order=asc
```

---

# Direções

Permitidas.

```
asc

desc
```

---

# Ordenação Crescente

```
order=asc
```

---

# Ordenação Decrescente

```
order=desc
```

---

# Campos Permitidos

Cada endpoint deverá definir explicitamente quais campos poderão ser utilizados.

Exemplo.

```
name

created_at

updated_at

status

priority

email

last_login
```

Nunca permitir ordenação por qualquer campo arbitrário.

---

# Ordenação Múltipla

Permitida.

Formato.

```
sort=priority,-created_at,name
```

Onde.

```
priority

↓

ASC

-created_at

↓

DESC

name

↓

ASC
```

---

# Campos Relacionados

Permitidos quando documentados.

Exemplo.

```
project.name

owner.name

department.title
```

---

# Ordenação Padrão

Caso nenhum parâmetro seja informado.

Utilizar.

```
created_at DESC
```

ou outro padrão definido pelo módulo.

---

# Ordenação Estável

Obrigatória.

Quando dois registros possuírem o mesmo valor.

Utilizar chave secundária.

Exemplo.

```
created_at DESC

↓

id ASC
```

---

# Valores Nulos

Política oficial.

```
NULLS LAST
```

Quando suportado pelo banco.

---

# Sensibilidade

Ordenações textuais deverão considerar.

- locale
- idioma
- acentuação

Quando aplicável.

---

# Datas

Formato.

```
ISO 8601
```

Ordenação cronológica obrigatória.

---

# Números

Ordenação numérica.

Nunca textual.

---

# Booleanos

Ordem padrão.

```
true

↓

false
```

Configurável por módulo.

---

# Performance

Toda ordenação deverá utilizar.

- índices
- planos de execução
- consultas otimizadas

Evitar ORDER BY em campos não indexados em grandes tabelas.

---

# Banco de Dados

Sempre utilizar.

```
ORDER BY
```

através do ORM.

Nunca concatenar SQL manualmente.

---

# Índices

Criar índices para campos frequentemente utilizados.

Exemplos.

```
created_at

updated_at

status

priority

name
```

---

# GraphQL

Ordenação através de Input Types.

Exemplo.

```
UserSortInput

ProjectSortInput

TaskSortInput
```

Campos.

```
field

direction
```

---

# SDK

Todos os SDKs deverão abstrair.

- campo
- direção
- múltiplas ordenações

---

# Cortex

O Cortex deverá selecionar automaticamente a ordenação mais adequada conforme o contexto.

Exemplos.

Logs.

```
created_at DESC
```

Usuários.

```
name ASC
```

Dashboard.

```
priority DESC
```

---

# MCP

Ferramentas MCP deverão validar.

- campos
- direção
- limites

antes da execução.

---

# Segurança

Nunca permitir.

- SQL Injection
- campos não autorizados
- ORDER BY arbitrário

Toda ordenação deverá ser validada.

---

# Auditoria

Registrar.

- campo
- direção
- usuário
- endpoint
- duração

---

# Observabilidade

Monitorar.

- consultas lentas
- uso de índices
- planos de execução
- ordenações frequentes

---

# Fluxo Oficial

```
Request

↓

Validation

↓

Filtering

↓

Sorting

↓

Pagination

↓

Database

↓

Response
```

---

# Checklist

Antes da publicação.

- Campos autorizados.

- Índices criados.

- Ordenação documentada.

- Ordenação estável.

- Performance validada.

- Segurança implementada.

---

# Boas Práticas

- Ordenar antes de paginar.
- Utilizar índices.
- Definir ordenação padrão.
- Validar campos.
- Documentar comportamento.
- Evitar ordenações custosas.
- Registrar auditoria.

---

# Padrão Oficial

Toda ordenação da Workstation IA deverá seguir este documento.

REST, GraphQL, SDKs, Cortex e servidores MCP utilizarão exatamente o mesmo modelo de ordenação, garantindo comportamento consistente em toda a plataforma.

---

# Referências Oficiais

- SQL Standard ORDER BY
- PostgreSQL Documentation
- MySQL Documentation
- OpenAPI Specification
- GraphQL Specification
- Microsoft REST API Guidelines
- Google API Design Guide

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de ordenação definida.
- Ordenação simples e múltipla documentadas.
- Integração com REST, GraphQL, SDKs, Cortex e MCP homologada.
- Estratégias de segurança e performance estabelecidas.