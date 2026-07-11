---
id: CKB-SEC-0012
title: Cross-Site Request Forgery (CSRF)
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - secure-headers.md
  - cors.md
  - session-management.md
related:
  - xss.md
  - authentication-security.md
  - api-security.md
last_update: 2026-07
---

# Cross-Site Request Forgery (CSRF)

## Objetivo

Definir oficialmente a arquitetura de proteção contra ataques de Cross-Site Request Forgery (CSRF) da Workstation IA.

Este documento estabelece os mecanismos obrigatórios para impedir que aplicações maliciosas executem ações em nome de usuários autenticados.

---

# Filosofia

Toda requisição que altera dados deverá provar sua legitimidade.

A autenticação do usuário não é suficiente.

A origem da requisição também deverá ser validada.

---

# Missão

Garantir que somente requisições legítimas possam executar operações protegidas.

---

# Arquitetura

```
Browser

↓

Cookie

↓

CSRF Validation

↓

Authentication

↓

Authorization

↓

Application
```

---

# Escopo

Proteção obrigatória para.

- aplicações Web
- painéis administrativos
- portais internos
- formulários
- dashboards
- sistemas com autenticação baseada em cookies

---

# Métodos Protegidos

Obrigatório proteger.

```
POST

PUT

PATCH

DELETE
```

Requisições.

```
GET

HEAD

OPTIONS
```

não deverão alterar estado.

---

# Estratégias Homologadas

A plataforma suportará.

```
Synchronizer Token Pattern

Double Submit Cookie

Origin Validation

Referer Validation

SameSite Cookies
```

---

# CSRF Token

Cada sessão autenticada deverá possuir.

```
csrf_token
```

Características.

- aleatório
- imprevisível
- único por sessão
- criptograficamente seguro

---

# Envio

O token poderá ser enviado.

Header.

```
X-CSRF-Token
```

ou.

```
X-XSRF-Token
```

Nunca pela URL.

---

# Double Submit Cookie

Fluxo.

```
Cookie

↓

Header

↓

Comparação

↓

Validação
```

Os valores deverão ser idênticos.

---

# SameSite

Cookies deverão utilizar.

```
SameSite=Strict
```

Quando houver necessidade de integração entre domínios controlados.

```
SameSite=Lax
```

`SameSite=None` somente quando estritamente necessário e sempre com `Secure`.

---

# Origin Validation

Validar.

```
Origin
```

contra lista oficial de domínios autorizados.

Caso inválido.

```
403 Forbidden
```

---

# Referer Validation

Utilizar como mecanismo complementar.

Nunca como única proteção.

---

# APIs REST

APIs autenticadas via.

```
Bearer JWT
```

armazenado fora de cookies normalmente não necessitam proteção CSRF.

Quando utilizarem cookies.

A proteção será obrigatória.

---

# GraphQL

Mutations deverão seguir exatamente as mesmas regras das APIs REST.

---

# WebSockets

Durante o Handshake validar.

- Origin
- autenticação
- autorização

Quando cookies forem utilizados.

Aplicar as mesmas políticas.

---

# SPAs

Aplicações React, Vue, Angular e similares deverão.

- obter CSRF Token
- armazená-lo temporariamente
- enviá-lo em todas as requisições protegidas

---

# Upload

Uploads autenticados deverão validar.

- CSRF Token
- autenticação
- autorização
- origem

---

# Expiração

O token poderá ser renovado.

- após login
- após logout
- após renovação de sessão
- após alteração de privilégios

---

# Erros

Resposta.

```
403 Forbidden
```

Código.

```
INVALID_CSRF_TOKEN
```

---

# Auditoria

Registrar.

- falhas
- tokens inválidos
- origem
- usuário
- IP
- endpoint

---

# Monitoramento

Monitorar.

- tentativas repetidas
- tokens inválidos
- origens rejeitadas
- ataques automatizados

---

# Segurança

Nunca.

- reutilizar tokens previsíveis
- aceitar tokens pela URL
- desabilitar validação em produção
- confiar apenas no Referer

---

# Fluxo Oficial

```
Login

↓

Sessão

↓

CSRF Token

↓

Request

↓

Validation

↓

Application

↓

Response
```

---

# Checklist

Antes da implantação.

- CSRF Token implementado.

- SameSite configurado.

- Origin Validation ativa.

- Referer Validation complementar.

- Auditoria funcionando.

- Monitoramento ativo.

---

# Boas Práticas

- Utilizar tokens criptograficamente seguros.
- Renovar tokens em mudanças de sessão.
- Validar Origin sempre que possível.
- Utilizar SameSite.
- Registrar tentativas inválidas.
- Testar proteção automaticamente no CI/CD.
- Revisar políticas periodicamente.

---

# Padrão Oficial

Toda aplicação Web da Workstation IA que utilize autenticação baseada em cookies deverá implementar proteção CSRF conforme este documento.

A proteção aplica-se igualmente aos módulos administrativos, dashboards, aplicações SPA, GraphQL e interfaces Web do Cortex e dos servidores MCP.

---

# Referências Oficiais

- OWASP Cross-Site Request Forgery Prevention Cheat Sheet
- OWASP ASVS
- RFC 6265 (HTTP Cookies)
- MDN Web Docs SameSite Cookies
- NIST SP 800-53
- CIS Controls v8

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de proteção CSRF definida.
- Synchronizer Token, Double Submit Cookie e validação de Origin documentados.
- Integração com REST, GraphQL, SPAs, Cortex e servidores MCP homologada.
- Controles de auditoria, monitoramento e segurança estabelecidos. 