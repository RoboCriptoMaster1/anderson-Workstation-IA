---
id: CKB-API-0006
title: Responses
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - requests.md
  - endpoints.md
related:
  - errors.md
  - documentation.md
  - pagination.md
last_update: 2026-07
---

# Responses

## Objetivo

Definir o padrão oficial para todas as respostas das APIs da Workstation IA.

Toda resposta enviada pela plataforma deverá possuir estrutura consistente, previsível, documentada e rastreável.

---

# Filosofia

Toda resposta comunica mais do que dados.

Ela comunica.

- resultado
- contexto
- rastreabilidade
- estado
- integridade

Uma resposta consistente facilita integrações, debugging e manutenção.

---

# Arquitetura

```
Request

↓

Authentication

↓

Authorization

↓

Validation

↓

Service

↓

Repository

↓

Database

↓

Response Builder

↓

Cliente
```

---

# Estrutura Oficial

Todas as respostas deverão seguir.

```json
{
    "success": true,
    "message": "",
    "data": {},
    "metadata": {},
    "request_id": "",
    "timestamp": ""
}
```

---

# Campos

## success

Tipo

```
Boolean
```

Indica sucesso ou falha.

---

## message

Mensagem amigável.

Exemplo.

```
Usuário criado com sucesso.
```

---

## data

Objeto contendo o resultado.

Pode ser.

- objeto
- lista
- null

---

## metadata

Informações complementares.

Exemplo.

```json
{
    "page": 1,
    "page_size": 20,
    "total": 400
}
```

---

## request_id

Identificador único da requisição.

Obrigatório.

---

## timestamp

Formato.

```
ISO 8601 UTC
```

Exemplo.

```
2026-07-10T14:30:00Z
```

---

# Resposta de Sucesso

```json
{
    "success": true,
    "message": "Operação realizada com sucesso.",
    "data": {},
    "metadata": {},
    "request_id": "...",
    "timestamp": "..."
}
```

---

# Lista de Dados

```json
{
    "success": true,
    "message": "Consulta realizada.",
    "data": [],
    "metadata": {
        "page": 1,
        "page_size": 20,
        "total_items": 300,
        "total_pages": 15
    },
    "request_id": "...",
    "timestamp": "..."
}
```

---

# Criação

HTTP

```
201 Created
```

Resposta.

```json
{
    "success": true,
    "message": "Recurso criado.",
    "data": {}
}
```

---

# Atualização

HTTP

```
200 OK
```

---

# Exclusão

HTTP

```
204 No Content
```

Quando houver corpo.

```
200 OK
```

---

# Paginação

Metadata.

```json
{
    "page": 2,
    "page_size": 50,
    "total_items": 1380,
    "total_pages": 28,
    "has_next": true,
    "has_previous": true
}
```

---

# Links

Opcional.

```json
{
    "links": {
        "self": "...",
        "next": "...",
        "previous": "..."
    }
}
```

---

# Respostas Assíncronas

HTTP

```
202 Accepted
```

Exemplo.

```json
{
    "success": true,
    "message": "Processamento iniciado.",
    "job_id": "..."
}
```

---

# Arquivos

Download.

Headers.

```
Content-Type

Content-Length

Content-Disposition
```

---

# Erros

Toda falha deverá utilizar.

```json
{
    "success": false,
    "message": "",
    "errors": [],
    "request_id": "",
    "timestamp": ""
}
```

---

# Estrutura de Erro

```json
{
    "field": "email",
    "code": "INVALID_EMAIL",
    "message": "Formato inválido."
}
```

---

# Códigos HTTP

```
200 OK

201 Created

202 Accepted

204 No Content

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

422 Unprocessable Entity

429 Too Many Requests

500 Internal Server Error

503 Service Unavailable
```

---

# Internacionalização

Mensagens poderão ser traduzidas.

Idioma obtido através de.

```
Accept-Language
```

---

# Auditoria

Toda resposta deverá registrar.

- request_id
- duração
- endpoint
- usuário
- código HTTP

---

# Versionamento

Mudanças incompatíveis deverão gerar nova versão da API.

Nunca alterar contratos existentes.

---

# Segurança

Nunca retornar.

- stack trace
- SQL
- credenciais
- tokens
- caminhos internos
- exceções completas

Essas informações permanecerão apenas nos logs.

---

# Performance

As respostas deverão.

- minimizar payload
- utilizar compressão
- evitar campos desnecessários
- permitir cache quando aplicável

---

# Fluxo Oficial

```
Service

↓

Response Builder

↓

JSON

↓

HTTP

↓

Cliente
```

---

# Checklist

Antes da publicação.

- Estrutura padronizada.

- HTTP correto.

- request_id presente.

- timestamp presente.

- metadata correta.

- Sem informações sensíveis.

- Documentação atualizada.

---

# Boas Práticas

- Sempre responder JSON.
- Utilizar mensagens claras.
- Padronizar metadata.
- Utilizar códigos HTTP corretos.
- Nunca quebrar contratos.
- Registrar auditoria.
- Facilitar integração.

---

# Padrão Oficial

Todas as respostas da Workstation IA deverão seguir este documento.

A estrutura JSON oficial será utilizada por toda a plataforma, incluindo Frontend, Mobile, Cortex, Agentes Inteligentes e integrações externas.

---

# Referências Oficiais

- RFC 9110 HTTP Semantics
- JSON RFC 8259
- OpenAPI Specification
- Microsoft REST API Guidelines
- Google API Design Guide

---

# Changelog

## 1.0.0

- Documento criado.
- Estrutura oficial de Responses definida.
- Padrão JSON homologado.
- Metadata, paginação e respostas assíncronas documentadas.
- Contrato oficial da API estabelecido.