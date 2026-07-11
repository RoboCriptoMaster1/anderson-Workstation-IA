---
id: CKB-API-0009
title: OpenAPI
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - documentation.md
  - endpoints.md
  - requests.md
  - responses.md
related:
  - sdk.md
  - webhooks.md
  - versioning.md
last_update: 2026-07
---

# OpenAPI

## Objetivo

Definir oficialmente a especificação OpenAPI utilizada pela Workstation IA.

Este documento estabelece como todas as APIs deverão ser descritas, documentadas, versionadas e disponibilizadas para clientes, SDKs, Cortex e servidores MCP.

A especificação OpenAPI representa o contrato oficial da plataforma.

---

# Filosofia

O código implementa.

O OpenAPI descreve.

O Cortex compreende.

Toda API publicada deverá possuir especificação OpenAPI atualizada.

---

# Missão

Manter um contrato técnico único para todas as APIs da Workstation IA.

---

# Padrão Oficial

Versão adotada.

```
OpenAPI 3.1
```

Formato.

```
YAML
```

Arquivo principal.

```
openapi.yaml
```

---

# Estrutura Oficial

```
api/

openapi.yaml

components/

paths/

schemas/

examples/

security/

tags/

webhooks/
```

---

# Estrutura Geral

```
openapi

↓

info

↓

servers

↓

tags

↓

paths

↓

components

↓

security

↓

webhooks
```

---

# Info

Campos obrigatórios.

```
title

description

version

contact

license
```

---

# Servers

Ambientes oficiais.

```
Development

Homologation

Production
```

Exemplo.

```
https://dev.api.workstation.ai

https://hml.api.workstation.ai

https://api.workstation.ai
```

---

# Tags

Organização oficial.

```
Authentication

Users

Projects

Tasks

Dashboard

Reports

Files

Notifications

Administration

Cortex

AI
```

---

# Paths

Cada endpoint deverá possuir.

- resumo
- descrição
- parâmetros
- request
- responses
- segurança
- exemplos

---

# Components

Estrutura.

```
Schemas

Responses

Parameters

Headers

Examples

RequestBodies

SecuritySchemes
```

Todos reutilizáveis.

---

# Schemas

Cada entidade deverá possuir um Schema.

Exemplo.

```
User

Project

Task

Dashboard

Notification

Role

Permission
```

---

# Responses

Respostas reutilizáveis.

```
SuccessResponse

ValidationError

Unauthorized

Forbidden

NotFound

Conflict

InternalError
```

---

# Parameters

Parâmetros reutilizáveis.

```
page

page_size

sort

order

id

request_id
```

---

# Headers

Headers oficiais.

```
Authorization

Content-Type

Accept

Accept-Language

X-Request-ID
```

---

# Security Schemes

Padrão oficial.

```
Bearer JWT
```

Futuro.

```
OAuth2

API Key

OpenID Connect
```

---

# Request Bodies

Cada operação deverá documentar.

- campos
- obrigatórios
- opcionais
- exemplos
- validações

---

# Examples

Todo endpoint deverá possuir.

- Request
- Response
- Erro
- Paginação

---

# Links

Quando aplicável.

Relacionar operações.

Exemplo.

```
Create User

↓

Get User

↓

Update User
```

---

# Callbacks

Utilizar para operações assíncronas.

Exemplo.

```
Importação

↓

Webhook

↓

Resultado
```

---

# Webhooks

Documentar.

- eventos
- payload
- autenticação
- assinatura

---

# Extensões

Permitidas.

Formato.

```
x-workstation

x-cortex

x-module

x-owner

x-permissions
```

Utilizadas para integração com o Cortex.

---

# Versionamento

Cada versão possuirá seu próprio contrato.

```
v1

v2

v3
```

Nunca quebrar contratos existentes.

---

# Geração Automática

O OpenAPI será utilizado para gerar.

- Swagger UI
- Redoc
- SDKs
- Coleções Postman
- Coleções Insomnia
- Clientes HTTP
- Documentação
- Ferramentas MCP

---

# Integração com o Cortex

O Cortex utilizará o OpenAPI para.

- compreender APIs
- descobrir endpoints
- validar parâmetros
- gerar integrações
- construir SDKs
- auxiliar agentes

---

# Integração com MCP

Servidores MCP poderão importar automaticamente.

```
OpenAPI

↓

Endpoints

↓

Schemas

↓

Ferramentas
```

---

# Integração com RAG

Fluxo.

```
OpenAPI

↓

Knowledge Base

↓

Embeddings

↓

RAG

↓

Claude
```

---

# Segurança

Nunca documentar.

- tokens válidos
- credenciais reais
- segredos
- chaves privadas

Todos os exemplos deverão utilizar dados fictícios.

---

# Organização

```
Paths

↓

Components

↓

Schemas

↓

Examples

↓

Security

↓

Tags
```

---

# Observabilidade

Documentar.

- Request ID
- Correlation ID
- Rate Limit
- Cache
- Paginação
- Versionamento

---

# Checklist

Antes da publicação.

- OpenAPI válido.

- YAML validado.

- Schemas reutilizáveis.

- Security definida.

- Exemplos completos.

- Swagger funcionando.

- Redoc atualizado.

- SDK regenerado.

---

# Boas Práticas

- Reutilizar Components.
- Evitar duplicação.
- Utilizar exemplos completos.
- Versionar contratos.
- Validar YAML automaticamente.
- Automatizar geração.
- Manter compatibilidade.

---

# Padrão Oficial

Toda API da Workstation IA deverá possuir um contrato OpenAPI 3.1.

O arquivo `openapi.yaml` será considerado a especificação oficial da plataforma.

O Cortex, os Agentes Inteligentes e os Servidores MCP utilizarão esta especificação como fonte primária para descoberta, validação e integração das APIs.

---

# Referências Oficiais

- OpenAPI Specification 3.1
- Swagger Documentation
- Redoc Documentation
- JSON Schema Draft 2020-12
- AsyncAPI Specification
- RFC 9110 HTTP Semantics

---

# Changelog

## 1.0.0

- Documento criado.
- Especificação OpenAPI oficial definida.
- Estrutura do `openapi.yaml` documentada.
- Integração com Swagger, Redoc, Cortex, MCP e SDKs homologada.