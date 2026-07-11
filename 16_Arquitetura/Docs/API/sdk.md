---
id: CKB-API-0010
title: SDK
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - openapi.md
  - documentation.md
  - authentication.md
  - authorization.md
related:
  - webhooks.md
  - websocket.md
  - graphql.md
last_update: 2026-07
---

# SDK

## Objetivo

Definir oficialmente a arquitetura dos SDKs da Workstation IA.

Os SDKs representam a forma oficial de integração entre aplicações externas e a plataforma.

Todos os SDKs deverão ser gerados a partir da especificação OpenAPI oficial.

---

# Filosofia

Uma API deve ser simples.

Um SDK deve torná-la ainda mais simples.

O desenvolvedor não deve preocupar-se com detalhes de autenticação, serialização, retries ou tratamento de erros.

---

# Missão

Disponibilizar bibliotecas oficiais para múltiplas linguagens mantendo comportamento consistente entre todas elas.

---

# Arquitetura

```
OpenAPI

↓

SDK Generator

↓

SDK Oficial

↓

Aplicação Cliente

↓

API

↓

Workstation IA
```

---

# Linguagens Homologadas

SDKs oficiais.

```
Python

JavaScript

TypeScript

Java

Go

C#

PHP

Dart

Kotlin

Swift
```

---

# Estrutura

```
sdk/

python/

javascript/

typescript/

java/

go/

csharp/

php/

dart/

swift/
```

---

# Organização

Cada SDK deverá possuir.

```
Authentication

Client

Configuration

Models

Requests

Responses

Exceptions

Utilities

Examples

Tests
```

---

# Cliente Principal

Todo SDK deverá possuir um Client central.

Exemplo.

```
WorkstationClient
```

Responsabilidades.

- autenticação
- comunicação HTTP
- serialização
- retries
- tratamento de erros
- logging

---

# Configuração

Cada SDK deverá permitir.

- Base URL
- Timeout
- Retries
- Ambiente
- Proxy
- Headers
- Rate Limit

---

# Autenticação

Suporte oficial.

```
Bearer JWT

Refresh Token

OAuth 2.0

API Key

Service Account
```

---

# Requests

Todas as chamadas deverão.

- validar parâmetros
- serializar automaticamente
- adicionar headers
- registrar request_id

---

# Responses

Toda resposta deverá retornar.

- objeto tipado
- metadata
- request_id
- status HTTP

---

# Tratamento de Erros

Cada SDK deverá possuir exceções específicas.

Exemplos.

```
AuthenticationException

AuthorizationException

ValidationException

RateLimitException

ApiException

TimeoutException

ServerException
```

---

# Retry

Permitido para.

- timeout
- erro temporário
- indisponibilidade

Estratégia.

```
Exponential Backoff
```

---

# Timeouts

Padrão.

```
30 segundos
```

Configurável.

---

# Logging

Níveis.

```
DEBUG

INFO

WARNING

ERROR

CRITICAL
```

---

# Cache

Opcional.

Suporte.

- memória
- Redis
- disco

---

# Serialização

Formato oficial.

```
JSON UTF-8
```

---

# Upload

Suporte para.

```
multipart/form-data
```

---

# Download

Suporte para.

- arquivos
- streams
- downloads grandes

---

# Paginação

Todos os SDKs deverão abstrair.

```
page

page_size

next

previous
```

---

# Observabilidade

Registrar.

- request_id
- endpoint
- duração
- retries
- status

---

# Integração com Cortex

O Cortex poderá utilizar os SDKs para.

- executar integrações
- consumir APIs
- automatizar processos
- criar agentes

---

# Integração com MCP

Servidores MCP poderão utilizar os SDKs oficiais em vez de chamadas HTTP diretas.

---

# Geração Automática

Origem.

```
OpenAPI

↓

SDK Generator

↓

Publicação
```

Nunca editar código gerado manualmente.

---

# Distribuição

Python.

```
PyPI
```

JavaScript.

```
NPM
```

Java.

```
Maven Central
```

Go.

```
Go Modules
```

PHP.

```
Packagist
```

C#.

```
NuGet
```

---

# Versionamento

Todos os SDKs seguirão.

```
Semantic Versioning
```

Compatibilidade baseada na versão da API.

---

# Testes

Cada SDK deverá possuir.

- testes unitários
- testes de integração
- exemplos funcionais
- validação automática

---

# Documentação

Cada SDK deverá conter.

- instalação
- configuração
- autenticação
- exemplos
- tratamento de erros
- migração entre versões

---

# Segurança

Nunca armazenar.

- tokens
- credenciais
- chaves privadas

Todos os segredos deverão permanecer externos.

---

# Fluxo Oficial

```
OpenAPI

↓

SDK

↓

Cliente

↓

API

↓

Response

↓

Aplicação
```

---

# Checklist

Antes da publicação.

- SDK gerado.

- Testes executados.

- Documentação atualizada.

- Compatibilidade validada.

- OpenAPI sincronizado.

- Exemplos publicados.

---

# Boas Práticas

- Nunca modificar código gerado.
- Automatizar publicação.
- Manter compatibilidade.
- Versionar corretamente.
- Documentar exemplos.
- Utilizar tipagem forte.
- Reutilizar modelos OpenAPI.

---

# Padrão Oficial

Todos os SDKs da Workstation IA deverão ser gerados automaticamente a partir da especificação OpenAPI oficial.

Os SDKs representam a forma recomendada de integração entre aplicações externas, Cortex, agentes inteligentes e a plataforma.

---

# Referências Oficiais

- OpenAPI Generator
- Swagger Codegen
- OpenAPI Specification 3.1
- Semantic Versioning
- PyPI Packaging Guide
- NPM Documentation
- Maven Central
- NuGet Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial dos SDKs definida.
- Processo de geração automática documentado.
- Integração com OpenAPI, Cortex e MCP homologada.