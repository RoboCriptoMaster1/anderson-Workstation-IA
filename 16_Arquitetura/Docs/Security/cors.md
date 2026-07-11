---
id: CKB-SEC-0011
title: Cross-Origin Resource Sharing (CORS)
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - secure-headers.md
  - authentication-security.md
  - ../api/endpoints.md
related:
  - csrf.md
  - api-security.md
  - websocket.md
  - graphql.md
last_update: 2026-07
---

# Cross-Origin Resource Sharing (CORS)

## Objetivo

Definir oficialmente a política de Cross-Origin Resource Sharing (CORS) da Workstation IA.

Este documento estabelece como aplicações externas poderão consumir APIs da plataforma de forma segura, controlada e auditável.

---

# Filosofia

Nem toda origem deve possuir acesso.

Toda origem deverá ser explicitamente autorizada.

O princípio padrão será.

```
Negar

↓

Validar

↓

Permitir
```

---

# Missão

Garantir comunicação segura entre navegadores, aplicações Web, SDKs, Cortex, servidores MCP e APIs da plataforma.

---

# Arquitetura

```
Browser

↓

Origin

↓

API Gateway

↓

CORS Validation

↓

Authentication

↓

Authorization

↓

Application

↓

Response
```

---

# Política Oficial

A Workstation IA utilizará.

```
Whitelist

↓

Origins Explicitamente Autorizadas
```

Nunca utilizar.

```
Access-Control-Allow-Origin: *
```

em APIs autenticadas.

---

# Origens Permitidas

Exemplos.

Produção.

```
https://app.workstation.ai

https://portal.workstation.ai
```

Homologação.

```
https://hml.workstation.ai
```

Desenvolvimento.

```
http://localhost:3000

http://localhost:5173
```

Cada ambiente possuirá sua própria lista.

---

# Métodos Permitidos

```
GET

POST

PUT

PATCH

DELETE

OPTIONS
```

---

# Headers Permitidos

```
Authorization

Content-Type

Accept

Accept-Language

X-Request-ID

X-Correlation-ID

If-None-Match

If-Match
```

---

# Headers Expostos

Quando necessário.

```
X-Request-ID

X-RateLimit-Limit

X-RateLimit-Remaining

X-RateLimit-Reset

ETag
```

---

# Credenciais

Quando houver autenticação baseada em cookies.

```
Access-Control-Allow-Credentials: true
```

Obrigatório.

Nunca combinar.

```
Allow-Credentials=true

+

Allow-Origin=*
```

---

# Preflight

Toda requisição.

```
OPTIONS
```

deverá validar.

- origem
- método
- headers
- credenciais

Antes da execução.

---

# Cache

Preflight poderá utilizar.

```
Access-Control-Max-Age

3600
```

Conforme política do ambiente.

---

# APIs REST

Seguirão integralmente esta política.

---

# GraphQL

Utilizará exatamente a mesma política de CORS das APIs REST.

---

# WebSockets

A origem deverá ser validada durante o Handshake.

Toda conexão proveniente de origem não autorizada deverá ser rejeitada.

---

# Upload de Arquivos

Além da origem.

Validar.

- autenticação
- autorização
- Content-Type
- tamanho
- integridade

---

# Ambientes

Desenvolvimento.

Mais permissivo.

Produção.

Mais restritivo.

Nunca compartilhar configurações entre ambientes.

---

# Multi-Tenant

Cada organização poderá possuir.

- domínios autorizados
- aplicações autorizadas
- integrações específicas

---

# Cortex

O Cortex deverá respeitar integralmente as políticas de origem quando consumir interfaces Web.

Integrações internas não dependerão de CORS.

---

# Servidores MCP

Os servidores MCP não estarão sujeitos ao mecanismo CORS quando utilizarem comunicação servidor-servidor.

Painéis Web dos servidores MCP deverão obedecer esta política.

---

# Auditoria

Registrar.

- origem
- método
- endpoint
- decisão
- usuário
- horário

---

# Monitoramento

Monitorar.

- origens rejeitadas
- tentativas repetidas
- falhas de configuração
- preflights
- acessos incomuns

---

# Segurança

Nunca permitir.

- Origin dinâmica sem validação
- Wildcards em produção
- Credenciais com origem aberta
- Headers não autorizados

---

# Fluxo Oficial

```
Browser

↓

Origin

↓

CORS

↓

Authentication

↓

Authorization

↓

Application

↓

Response
```

---

# Checklist

Antes da implantação.

- Whitelist configurada.

- Produção sem wildcard.

- Preflight validado.

- Headers revisados.

- Credenciais protegidas.

- Auditoria ativa.

- Monitoramento funcionando.

---

# Boas Práticas

- Utilizar listas explícitas de origens.
- Separar configurações por ambiente.
- Revisar periodicamente domínios autorizados.
- Nunca utilizar `*` em APIs autenticadas.
- Validar todas as requisições OPTIONS.
- Automatizar testes de CORS.
- Registrar todas as decisões de acesso.

---

# Padrão Oficial

Toda política CORS da Workstation IA deverá seguir este documento.

As regras aqui estabelecidas serão obrigatórias para APIs REST, GraphQL, aplicações Web, Cortex, painéis administrativos e interfaces Web dos servidores MCP.

---

# Referências Oficiais

- Fetch Living Standard (WHATWG)
- MDN Web Docs CORS
- OWASP Cross-Origin Resource Sharing Cheat Sheet
- OWASP ASVS
- RFC 9110 HTTP Semantics
- W3C Fetch Specification
- CIS Controls v8

---

# Changelog

## 1.0.0

- Documento criado.
- Política oficial de CORS definida.
- Configuração para REST, GraphQL, WebSockets e ambientes documentada.
- Integração com Cortex e servidores MCP homologada.
- Controles de auditoria, monitoramento e segurança estabelecidos.