---
id: CKB-FE-0005
title: React
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - html.md
  - css.md
  - javascript.md
  - typescript.md
related:
  - nextjs.md
  - tailwind.md
  - gsap.md
last_update: 2026-07
---

# React

## Objetivo

Definir os padrões oficiais para utilização do React na Workstation IA.

React é a biblioteca oficial responsável pela construção da interface baseada em componentes.

---

# Definição

React é uma biblioteca JavaScript criada para construção de interfaces reativas.

Na Workstation IA, toda interface moderna deverá ser construída utilizando React.

---

# Objetivos

- Componentização
- Reutilização
- Escalabilidade
- Performance
- Organização
- Manutenção

---

# Filosofia

Toda interface deve ser composta por pequenos componentes independentes.

Nunca criar componentes gigantes.

---

# Arquitetura

```
Pages

↓

Layouts

↓

Sections

↓

Components

↓

Hooks

↓

Services

↓

API
```

---

# Estrutura Oficial

```
src/

components/

layouts/

pages/

hooks/

services/

contexts/

types/

utils/

assets/
```

---

# Componentes

Cada componente deverá possuir responsabilidade única.

Exemplo

```
Button

Card

Input

Modal

Table

Sidebar

Navbar

DashboardCard
```

---

# Organização

Cada componente deverá possuir sua própria pasta.

```
Button/

Button.tsx

Button.module.css

Button.test.tsx

index.ts
```

---

# Props

Toda propriedade deverá possuir tipagem.

Nunca utilizar:

```
any
```

---

# Estado

Priorizar:

```
useState
```

Para estados locais.

Utilizar Context apenas quando realmente necessário.

---

# Hooks

Hooks personalizados deverão iniciar com:

```
use
```

Exemplo

```
useAuth()

useProjects()

useDashboard()

useTheme()
```

---

# Regras dos Hooks

Nunca utilizar Hooks:

- dentro de loops
- dentro de condições
- dentro de funções comuns

Sempre no topo do componente.

---

# Context

Utilizar apenas para estados globais.

Exemplos

- Tema
- Usuário autenticado
- Configurações
- Idioma

---

# Componentes

Dividir em categorias.

## UI

Componentes genéricos.

```
Button

Input

Card

Badge

Avatar
```

---

## Business

Componentes específicos.

```
ProjectCard

TaskList

DashboardChart

UserProfile
```

---

# Comunicação

Fluxo oficial

```
Props

↓

Callback

↓

State

↓

Render
```

---

# Eventos

Separar eventos da renderização.

Evitar lógica extensa dentro do JSX.

---

# JSX

Priorizar JSX limpo.

Evitar:

- ternários complexos
- múltiplos operadores
- funções enormes

---

# Performance

Utilizar quando necessário

```
memo

useMemo

useCallback

lazy

Suspense
```

Não utilizar otimizações sem necessidade comprovada.

---

# Renderização

Cada componente deve renderizar apenas o necessário.

Evitar re-renderizações desnecessárias.

---

# Animações

React controla estrutura.

GSAP controla animações.

Nunca substituir GSAP por animações React quando houver necessidade de animações complexas.

---

# Tailwind

Framework oficial.

Componentes devem utilizar Tailwind como padrão.

CSS adicional apenas quando necessário.

---

# TypeScript

Todo componente deverá ser escrito em TypeScript.

---

# Testes

Componentes críticos deverão possuir testes.

Prioridade

- Forms
- Dashboard
- Login
- Navegação
- Componentes reutilizáveis

---

# Integração

```
React

↓

Next.js

↓

Tailwind

↓

GSAP

↓

Services

↓

API
```

---

# Boas Práticas

- Componentes pequenos.
- Responsabilidade única.
- Props tipadas.
- Reutilização máxima.
- Separação entre UI e lógica.
- Evitar duplicação.
- Documentar componentes reutilizáveis.

---

# Padrão Oficial

React é a biblioteca oficial para construção da interface da Workstation IA.

Toda implementação deverá respeitar a arquitetura definida pelo Cortex.

---

# Ferramentas Homologadas

- React
- React DOM
- React DevTools
- TypeScript
- Tailwind CSS
- GSAP
- ESLint
- Prettier

---

# Referências Oficiais

- React Documentation
- React DevTools
- MDN Web Docs
- TypeScript Handbook

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura React definida.
- Estrutura oficial homologada.
- Boas práticas registradas.