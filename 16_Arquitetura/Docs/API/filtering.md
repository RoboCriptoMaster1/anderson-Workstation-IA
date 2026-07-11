---
id: CKB-API-0016
title: Filtering
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - pagination.md
  - requests.md
  - endpoints.md
related:
  - sorting.md
  - responses.md
  - graphql.md
last_update: 2026-07
---

# Filtering

## Objetivo

Definir oficialmente a arquitetura de filtros da Workstation IA.

Este documento estabelece como consultas poderão restringir, combinar e pesquisar dados de forma consistente, segura e performática.

Todos os endpoints que retornarem coleções deverão suportar o modelo oficial de filtros.

---

# Filosofia

Buscar menos.

Encontrar mais.

Filtrar antes de processar.

Toda filtragem deve ser previsível, documentada e otimizada.

---

# Missão

Permitir consultas flexíveis sem comprometer desempenho, segurança e padronização.

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

Os filtros serão enviados através da Query String.

Exemplo.

```
GET

/api/v1/users?status=active
```

---

# Operadores Oficiais

```
eq

ne

gt

gte

lt

lte

like

contains

starts_with

ends_with

between

in

not_in

is_null

is_not_null
```

---

# Igual

```
status=active
```

Equivalente.

```
status:eq=active
```

---

# Diferente

```
status:ne=inactive
```

---

# Maior

```
age:gt=18
```

---

# Maior ou Igual

```
salary:gte=5000
```

---

# Menor

```
price:lt=100
```

---

# Menor ou Igual

```
price:lte=999
```

---

# LIKE

```
name:like=anderson
```

---

# Contém

```
description:contains=dashboard
```

---

# Começa com

```
name:starts_with=Ana
```

---

# Termina com

```
email:ends_with=.com
```

---

# BETWEEN

```
created_at:between=2026-01-01,2026-12-31
```

---

# IN

```
status:in=active,pending
```

---

# NOT IN

```
category:not_in=test,temp
```

---

# Valores Nulos

```
deleted_at:is_null=true
```

---

# Valores Não Nulos

```
deleted_at:is_not_null=true
```

---

# Pesquisa Livre

Parâmetro oficial.

```
q=
```

Exemplo.

```
?q=financeiro
```

---

# Pesquisa Multicampos

O parâmetro.

```
q
```

poderá pesquisar simultaneamente.

- nome
- descrição
- código
- tags

Conforme configuração do módulo.

---

# Filtros Compostos

Permitidos.

Exemplo.

```
status=active

category=finance

priority=high
```

---

# Operadores Lógicos

Suporte para.

```
AND

OR

NOT
```

---

# Exemplo

```
status=active

AND

priority=high
```

---

# Datas

Formato.

```
ISO 8601
```

Exemplo.

```
created_after=2026-07-01T00:00:00Z
```

---

# Intervalos

```
created_before

created_after

updated_before

updated_after
```

---

# Booleanos

```
true

false
```

---

# UUID

Aceitar.

```
UUID v4
```

---

# Ordenação

Executada após filtros.

Fluxo.

```
Filtering

↓

Sorting

↓

Pagination
```

---

# Paginação

Sempre aplicada após a filtragem.

---

# Banco de Dados

Filtros deverão utilizar.

- índices
- consultas parametrizadas
- prepared statements

Nunca concatenar SQL manualmente.

---

# Segurança

Obrigatório.

- validação
- sanitização
- prepared statements
- limites de filtros
- proteção contra SQL Injection

---

# Performance

Priorizar.

- índices
- filtros seletivos
- cache
- consultas otimizadas

---

# Campos Permitidos

Cada endpoint deverá definir explicitamente.

- campos filtráveis
- operadores permitidos
- tipos aceitos

Nunca permitir filtros arbitrários.

---

# GraphQL

Os filtros serão representados por Input Types.

Exemplo.

```
UserFilterInput

ProjectFilterInput

TaskFilterInput
```

---

# SDK

Todos os SDKs deverão abstrair a criação dos filtros.

---

# Cortex

O Cortex deverá gerar filtros automaticamente quando necessário.

Sempre respeitando os operadores homologados.

---

# MCP

Ferramentas MCP deverão validar filtros antes da execução.

---

# Auditoria

Registrar.

- filtros utilizados
- usuário
- endpoint
- duração
- quantidade de registros

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

- Campos definidos.

- Operadores documentados.

- Índices criados.

- SQL parametrizado.

- Performance validada.

- Documentação atualizada.

---

# Boas Práticas

- Filtrar antes de paginar.
- Utilizar consultas parametrizadas.
- Limitar operadores.
- Documentar filtros.
- Evitar consultas custosas.
- Reutilizar filtros comuns.
- Registrar auditoria.

---

# Padrão Oficial

Todos os filtros da Workstation IA deverão seguir este documento.

Os operadores homologados representam a única forma oficial de filtragem da plataforma.

REST, GraphQL, SDKs, Cortex e servidores MCP deverão utilizar exatamente este padrão.

---

# Referências Oficiais

- OpenAPI Specification
- GraphQL Specification
- OWASP SQL Injection Prevention Cheat Sheet
- RFC 9110 HTTP Semantics
- Microsoft REST API Guidelines
- Google API Design Guide

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de filtros definida.
- Operadores padronizados.
- Integração com REST, GraphQL, SDKs, Cortex e MCP documentada.
- Estratégias de segurança e performance homologadas.