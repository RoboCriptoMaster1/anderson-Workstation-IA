---
id: CKB-FE-0011
title: Framer Motion
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
related:
  - gsap.md
  - scrolltrigger.md
  - lenis.md
last_update: 2026-07
---

# Framer Motion

## Objetivo

Definir o padrão oficial para utilização do Framer Motion na Workstation IA.

Embora o GSAP seja a biblioteca oficial de animações da plataforma, o Framer Motion poderá ser utilizado em cenários específicos relacionados ao React.

---

# Definição

Framer Motion é uma biblioteca de animação voltada para aplicações React.

Possui integração nativa com componentes React e facilita a criação de microinterações.

---

# Status

Homologado

Uso Controlado

---

# Filosofia

O Framer Motion não substitui o GSAP.

Ele complementa o ecossistema apenas quando oferecer vantagens claras.

Toda animação cinematográfica continuará sendo responsabilidade do GSAP.

---

# Responsabilidades

Framer Motion poderá ser utilizado para:

- animações de componentes React
- transições entre páginas
- animações de estado
- hover
- focus
- drag
- gestures
- layout animations
- AnimatePresence

---

# Não utilizar para

- Storytelling
- Scroll Cinemático
- Landing Pages Cinematográficas
- Timelines
- Scroll Progress
- Scroll Pin
- Hero Animado
- Narrativas Visuais

Essas implementações pertencem ao GSAP.

---

# Hierarquia Oficial

```
GSAP

↓

ScrollTrigger

↓

Lenis

↓

Framer Motion

↓

CSS
```

---

# Quando Utilizar

Utilizar Framer Motion para:

- abertura de modais
- dropdowns
- sidebars
- menus
- notificações
- accordions
- tabs
- microinterações
- animações entre estados

---

# Quando NÃO Utilizar

Não utilizar para:

- Scroll
- Pin
- Storytelling
- Parallax
- Timelines
- Motion Design
- Sequências complexas

---

# Integração

```
React

↓

Framer Motion

↓

Componentes
```

---

# Componentes Homologados

- Modal
- Drawer
- Tooltip
- Popover
- Toast
- Sidebar
- Accordion
- Tabs
- Floating Menu

---

# Componentes Não Recomendados

- Hero
- Dashboard Scroll
- Timeline
- Landing Animation
- Roadmap
- Scroll Reveal

---

# Organização

```
animations/

motion/

modal.ts

drawer.ts

sidebar.ts

toast.ts

page-transition.ts
```

---

# Layout Animations

Permitidas.

Utilizar apenas quando agregarem valor à experiência.

---

# AnimatePresence

Homologado.

Principal utilização.

- Entrada
- Saída
- Troca de componentes

---

# Gestures

Permitidos.

Exemplos

- Drag
- Hover
- Tap
- Focus

---

# Performance

Evitar múltiplas animações simultâneas.

Evitar componentes excessivamente animados.

Priorizar simplicidade.

---

# TypeScript

Obrigatório.

Toda implementação deverá ser tipada.

---

# React

Framer Motion deverá ser utilizado exclusivamente em componentes React.

---

# Compatibilidade

Compatível com:

- React
- Next.js
- Tailwind CSS
- TypeScript

---

# Boas Práticas

- Utilizar apenas quando necessário.
- Evitar duplicar animações existentes no GSAP.
- Centralizar animações reutilizáveis.
- Documentar componentes animados.

---

# Padrão Oficial

GSAP permanece como biblioteca principal de animações.

Framer Motion será utilizado apenas para animações específicas da interface React.

Sempre priorizar a ferramenta mais adequada para cada cenário.

---

# Ferramentas Homologadas

- Framer Motion
- React
- TypeScript
- Next.js

---

# Referências Oficiais

- Framer Motion Documentation
- Motion.dev
- React Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Framer Motion homologado para animações específicas em React.
- Limites de utilização definidos.
- Integração oficial registrada.