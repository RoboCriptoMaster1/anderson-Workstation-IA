---
id: CKB-FE-0006
title: Next.js
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - react.md
  - typescript.md
  - tailwind.md
related:
  - gsap.md
  - scrolltrigger.md
  - lenis.md
last_update: 2026-07
---

# Next.js

## Objetivo

Definir os padrões oficiais para utilização do Next.js na Workstation IA.

O Next.js é o framework oficial para desenvolvimento das aplicações Front-end da plataforma.

---

# Definição

Next.js é um framework React utilizado para construção de aplicações modernas, escaláveis e otimizadas.

Ele fornece recursos nativos para:

- roteamento
- renderização
- otimização
- APIs
- SEO
- performance

---

# Objetivos

- Padronização
- Escalabilidade
- Performance
- SEO
- Componentização
- Modularidade

---

# Arquitetura

```
App

↓

Layouts

↓

Pages

↓

Components

↓

Hooks

↓

Services

↓

API

↓

Backend
```

---

# Estrutura Oficial

```
src/

app/

components/

layouts/

hooks/

services/

lib/

types/

utils/

styles/

public/
```

---

# App Router

Padrão oficial.

Toda nova aplicação utilizará:

```
app/
```

Evitar utilização do Pages Router em novos projetos.

---

# Layouts

Utilizar layouts compartilhados.

Exemplo

```
RootLayout

DashboardLayout

AuthLayout

AdminLayout
```

---

# Componentes

Separar componentes em:

```
UI

Business

Shared

Layouts
```

---

# Server Components

Priorizar sempre que possível.

Vantagens:

- menor consumo de JavaScript
- melhor performance
- melhor SEO

---

# Client Components

Utilizar apenas quando necessário.

Casos:

- eventos
- estados
- animações
- interação

Sempre declarar:

```typescript
"use client";
```

---

# Renderização

Prioridade

```
Server Components

↓

Static Rendering

↓

Streaming

↓

Client Components
```

---

# Rotas

Utilizar estrutura oficial.

```
app/

dashboard/

projects/

users/

settings/
```

---

# APIs

Utilizar Route Handlers.

```
app/api/
```

Sempre separar regras de negócio.

---

# Services

Toda comunicação deverá passar por Services.

Nunca acessar APIs diretamente dentro dos componentes quando houver reutilização.

---

# Organização

Cada funcionalidade deverá possuir seu próprio módulo.

Exemplo

```
projects/

components/

hooks/

services/

types/
```

---

# TypeScript

Obrigatório.

Não criar aplicações oficiais em JavaScript puro.

---

# Tailwind

Framework oficial.

Toda interface deverá utilizar Tailwind CSS.

---

# GSAP

Responsável pelas animações.

Next.js controla a aplicação.

GSAP controla movimento.

---

# Scroll

Smooth Scroll

↓

Lenis

↓

ScrollTrigger

↓

GSAP

---

# Imagens

Utilizar

```typescript
next/image
```

Nunca utilizar `<img>` quando houver suporte do Next.js.

---

# Fontes

Utilizar

```typescript
next/font
```

Evitar carregamento manual.

---

# SEO

Utilizar Metadata API.

Toda página deverá possuir:

- title
- description
- open graph
- twitter cards

---

# Performance

Priorizar

- Server Components
- Lazy Loading
- Code Splitting
- Image Optimization
- Font Optimization

---

# Estado

Local

↓

useState

Global

↓

Context

ou

biblioteca homologada

---

# Segurança

Nunca expor:

- tokens
- secrets
- credenciais

Utilizar:

```
.env.local
```

---

# Estrutura Recomendada

```
app/

components/

hooks/

services/

types/

utils/

styles/

public/

middleware.ts

next.config.ts

package.json
```

---

# Ferramentas Homologadas

- React
- TypeScript
- Tailwind CSS
- GSAP
- ScrollTrigger
- Lenis
- ESLint
- Prettier

---

# Integração

```
Next.js

↓

React

↓

TypeScript

↓

Tailwind

↓

GSAP

↓

Services

↓

Backend
```

---

# Boas Práticas

- Utilizar Server Components como padrão.
- Componentizar toda interface.
- Evitar lógica extensa dentro das páginas.
- Separar responsabilidades.
- Documentar módulos reutilizáveis.
- Manter estrutura consistente.

---

# Padrão Oficial

Next.js é o framework oficial da Workstation IA.

Toda aplicação Front-end deverá seguir esta arquitetura.

---

# Referências Oficiais

- Next.js Documentation
- React Documentation
- TypeScript Handbook
- Vercel Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial definida.
- Padrões homologados.
- Estrutura inicial registrada.