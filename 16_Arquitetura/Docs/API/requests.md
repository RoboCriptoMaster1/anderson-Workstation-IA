---
id: CKB-API-0005
title: Requests
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - readme.md
  - authentication.md
  - authorization.md
  - endpoints.md
related:
  - responses.md
  - errors.md
  - documentation.md
  - validation.md
last_update: 2026-07
---

# Requests

## Objetivo

Definir o padrão oficial para todas as requisições realizadas às APIs da Workstation IA.

Este documento estabelece como clientes, sistemas externos, agentes do Cortex e serviços internos deverão enviar informações para a plataforma.

---

# Filosofia

Toda entrada de dados deve ser previsível.

Toda requisição deve ser validada.

Toda informação deve ser rastreável.

Nenhum dado recebido deve ser considerado confiável até ser validado.

---

# Arquitetura

```
Cliente

↓

HTTPS

↓

Headers

↓

Path Parameters

↓

Query Parameters

↓

Request Body

↓

Validator

↓

Service

↓

Repository

↓

Database
```

---

# Estrutura Geral

Toda requisição poderá conter.

```
Headers

↓

Path Parameters

↓

Query Parameters

↓

Body

↓

Files
```

---

# Content-Type

Padrão oficial.

```
application/json
```

Outros suportados.

```
multipart/form-data

application/octet-stream

application/pdf

text/plain

application/xml
```

---

# Charset

Obrigatório.

```
UTF-8
```

---

# Headers Obrigatórios

```
Authorization

Content-Type

Accept

X-Request-ID

User-Agent
```

---

# Authorization

Formato.

```
Authorization:

Bearer JWT
```

---

# Accept

```
application/json
```

---

# X-Request-ID

Toda requisição deverá possuir um identificador único.

Objetivo.

- rastreamento
- auditoria
- debugging

---

# Path Parameters

Utilizados para identificar recursos.

Exemplo.

```
GET

/users/{id}
```

---

# Query Parameters

Utilizados para filtros.

Exemplos.

```
?page=1

&page_size=20

&sort=name

&order=asc

&status=active

&q=dashboard
```

---

# Body

Formato oficial.

```
JSON
```

Exemplo.

```json
{
    "name": "Anderson",
    "email": "anderson@email.com",
    "status": "active"
}
```

---

# Body Obrigatório

Campos obrigatórios deverão ser definidos através dos Validators.

Nunca confiar apenas no Frontend.

---

# Upload de Arquivos

Formato.

```
multipart/form-data
```

Campos.

```
file

description

category
```

---

# Tipos Permitidos

Documentos.

```
pdf

docx

xlsx

csv

txt
```

Imagens.

```
png

jpg

jpeg

webp

svg
```

---

# Limite de Upload

Padrão.

```
25 MB
```

Configuração poderá variar por módulo.

---

# Download

Toda resposta deverá informar.

```
Content-Type

Content-Disposition

Content-Length
```

---

# Serialização

Utilizar.

```
JSON UTF-8
```

Objetivos.

- interoperabilidade
- simplicidade
- padronização

---

# Validação

Toda entrada deverá validar.

- tipo
- tamanho
- formato
- obrigatoriedade
- unicidade
- regras de negócio

---

# Sanitização

Obrigatória.

Remover.

- scripts
- HTML malicioso
- SQL Injection
- caracteres inválidos

---

# Datas

Formato oficial.

```
ISO 8601
```

Exemplo.

```
2026-07-10T15:30:00Z
```

---

# Horários

Sempre armazenar em UTC.

Conversão realizada apenas na apresentação.

---

# Valores Monetários

Formato.

```
Decimal
```

Nunca utilizar Float.

---

# Booleanos

Formato.

```
true

false
```

---

# Arrays

Formato.

```json
[
    {},
    {},
    {}
]
```

---

# Objetos

Sempre utilizar nomes descritivos.

Exemplo.

```json
{
    "project": {},
    "owner": {},
    "permissions": []
}
```

---

# Paginação

Receber.

```
page

page_size
```

---

# Ordenação

Receber.

```
sort

order
```

---

# Pesquisa

Receber.

```
q
```

---

# Internacionalização

Aceitar.

```
Accept-Language
```

Exemplo.

```
pt-BR

en-US

fr-FR
```

---

# Auditoria

Registrar.

- usuário
- endpoint
- método
- IP
- request_id
- horário
- duração

---

# Segurança

Toda requisição deverá.

- utilizar HTTPS
- validar JWT
- validar permissões
- sanitizar entradas
- limitar tamanho
- registrar auditoria

---

# Rate Limit

Aplicado antes da validação.

Objetivos.

- evitar abuso
- proteger infraestrutura
- impedir ataques automatizados

---

# Fluxo Oficial

```
Cliente

↓

Request

↓

Authentication

↓

Authorization

↓

Validation

↓

Sanitization

↓

Service

↓

Repository

↓

Database

↓

Response
```

---

# Checklist

Antes da publicação.

- Headers definidos.

- JSON válido.

- Validators implementados.

- Sanitização ativa.

- Auditoria configurada.

- Upload protegido.

- Rate Limit configurado.

---

# Boas Práticas

- Validar toda entrada.
- Nunca confiar no cliente.
- Utilizar UTF-8.
- Utilizar JSON.
- Padronizar datas.
- Limitar uploads.
- Registrar auditoria.

---

# Padrão Oficial

Todas as requisições da Workstation IA deverão seguir este documento.

Nenhum endpoint poderá aceitar dados sem validação, sanitização e auditoria.

---

# Referências Oficiais

- RFC 9110 HTTP Semantics
- JSON RFC 8259
- OpenAPI Specification
- OWASP Input Validation Cheat Sheet
- OWASP File Upload Cheat Sheet

---

# Changelog

## 1.0.0

- Documento criado.
- Padrão oficial de Requests definido.
- Estrutura de entrada documentada.
- Regras de validação, sanitização e upload homologadas.