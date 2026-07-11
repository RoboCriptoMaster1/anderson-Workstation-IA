---
id: CKB-SEC-0010
title: Secure Headers
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - session-management.md
  - principles.md
related:
  - cors.md
  - csrf.md
  - xss.md
  - api-security.md
last_update: 2026-07
---

# Secure Headers

## Objetivo

Definir oficialmente os cabeçalhos HTTP de segurança utilizados pela Workstation IA.

Este documento estabelece as políticas obrigatórias para proteção de aplicações Web, APIs REST, GraphQL, WebSockets e interfaces administrativas contra ataques comuns, incluindo XSS, Clickjacking, MIME Sniffing, Cross-Origin Attacks e vazamento de informações.

---

# Filosofia

Toda resposta HTTP representa uma oportunidade de proteção.

Os navegadores modernos devem receber políticas explícitas de segurança.

Nenhuma aplicação deverá depender apenas do comportamento padrão do navegador.

---

# Missão

Garantir que todas as aplicações da Workstation IA sejam protegidas por políticas modernas de segurança HTTP.

---

# Arquitetura

```
Cliente

↓

HTTPS

↓

API Gateway

↓

Secure Headers

↓

Application

↓

Response
```

---

# Cabeçalhos Obrigatórios

Toda resposta HTTP deverá considerar os seguintes cabeçalhos.

```
Strict-Transport-Security

Content-Security-Policy

X-Content-Type-Options

X-Frame-Options

Referrer-Policy

Permissions-Policy

Cross-Origin-Opener-Policy

Cross-Origin-Embedder-Policy

Cross-Origin-Resource-Policy
```

---

# Strict-Transport-Security

Objetivo.

Forçar utilização exclusiva de HTTPS.

Exemplo.

```
Strict-Transport-Security:
max-age=31536000;
includeSubDomains;
preload
```

Nunca utilizar HSTS antes da implantação completa de HTTPS.

---

# Content-Security-Policy (CSP)

Objetivo.

Controlar a origem de.

- scripts
- estilos
- imagens
- fontes
- frames
- conexões

Exemplo.

```
default-src 'self';

script-src 'self';

style-src 'self';

img-src 'self' data: https:;

connect-src 'self' https://api.workstation.ai;

object-src 'none';

frame-ancestors 'none';

base-uri 'self';
```

Evitar.

```
unsafe-inline

unsafe-eval
```

Sempre que possível.

---

# X-Content-Type-Options

Objetivo.

Impedir MIME Sniffing.

Valor.

```
nosniff
```

---

# X-Frame-Options

Objetivo.

Proteger contra Clickjacking.

Valor recomendado.

```
DENY
```

Alternativa.

```
SAMEORIGIN
```

---

# Referrer-Policy

Objetivo.

Controlar envio do cabeçalho Referer.

Valor recomendado.

```
strict-origin-when-cross-origin
```

---

# Permissions-Policy

Objetivo.

Controlar acesso às APIs do navegador.

Exemplo.

```
camera=()

microphone=()

geolocation=(self)

payment=()

usb=()

fullscreen=(self)
```

---

# Cross-Origin-Opener-Policy (COOP)

Objetivo.

Isolar o contexto da janela.

Valor recomendado.

```
same-origin
```

---

# Cross-Origin-Embedder-Policy (COEP)

Objetivo.

Controlar recursos incorporados.

Valor recomendado.

```
require-corp
```

---

# Cross-Origin-Resource-Policy (CORP)

Objetivo.

Restringir compartilhamento de recursos.

Valor recomendado.

```
same-origin
```

---

# Server

Evitar divulgar tecnologia utilizada.

Remover ou anonimizar.

```
Server

X-Powered-By
```

---

# Cache-Control

Para conteúdo sensível.

```
Cache-Control:
no-store,
no-cache,
must-revalidate,
private
```

---

# Pragma

Compatibilidade.

```
Pragma:
no-cache
```

---

# Expires

Conteúdo sensível.

```
Expires: 0
```

---

# Cookies

Sempre utilizar.

```
Secure

HttpOnly

SameSite=Strict
```

Quando apropriado.

---

# APIs

Todas as APIs deverão retornar os cabeçalhos compatíveis com seu contexto.

As políticas poderão variar para.

- REST
- GraphQL
- WebSockets
- Downloads

---

# CSP Report

Opcionalmente utilizar.

```
Content-Security-Policy-Report-Only
```

Durante implantação de novas políticas.

---

# Frontend

Aplicações SPA deverão obedecer integralmente à política CSP.

Bibliotecas externas deverão ser explicitamente autorizadas.

---

# Cortex

As interfaces do Cortex seguirão exatamente as mesmas políticas de segurança HTTP.

---

# MCP

Painéis administrativos de servidores MCP também deverão utilizar estes cabeçalhos.

---

# Monitoramento

Monitorar.

- violações CSP
- tentativas de Clickjacking
- recursos bloqueados
- falhas de configuração
- cabeçalhos ausentes

---

# Auditoria

Registrar.

- alterações
- políticas aplicadas
- exceções
- violações CSP

---

# Segurança

Nunca permitir.

- HTTP simples
- Inline Scripts desnecessários
- MIME Sniffing
- Clickjacking
- Divulgação de versão do servidor

---

# Fluxo Oficial

```
Request

↓

HTTPS

↓

Application

↓

Security Headers

↓

Response

↓

Browser Enforcement
```

---

# Checklist

Antes da implantação.

- HSTS ativo.

- CSP configurada.

- X-Frame-Options definido.

- X-Content-Type-Options ativo.

- Referrer-Policy configurada.

- Permissions-Policy revisada.

- COOP, COEP e CORP implementados.

---

# Boas Práticas

- Utilizar HTTPS em 100% das requisições.
- Restringir CSP ao mínimo necessário.
- Remover cabeçalhos que revelem tecnologia.
- Revisar políticas periodicamente.
- Monitorar violações CSP.
- Testar compatibilidade entre navegadores.
- Automatizar validações em CI/CD.

---

# Padrão Oficial

Toda resposta HTTP emitida pela Workstation IA deverá obedecer às políticas definidas neste documento.

Os cabeçalhos de segurança serão obrigatórios para aplicações Web, APIs, Cortex, painéis administrativos, SDKs com interface Web e servidores MCP.

---

# Referências Oficiais

- OWASP Secure Headers Project
- OWASP ASVS
- OWASP Content Security Policy Cheat Sheet
- RFC 6797 (HSTS)
- MDN Web Docs HTTP Security Headers
- W3C Content Security Policy Level 3
- NIST SP 800-53
- CIS Controls v8

---

# Changelog

## 1.0.0

- Documento criado.
- Política oficial de Secure Headers definida.
- Configuração de HSTS, CSP, COOP, COEP, CORP e demais cabeçalhos documentada.
- Integração com APIs, Frontend, Cortex e servidores MCP homologada.
- Controles de auditoria e monitoramento estabelecidos.