---
id: CKB-FE-0010
title: Lenis
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - gsap.md
  - scrolltrigger.md
related:
  - react.md
  - nextjs.md
last_update: 2026-07
---

# Lenis

## Objetivo

Definir o padrão oficial para utilização do Lenis na Workstation IA.

O Lenis é a biblioteca oficial responsável pelo Smooth Scroll da plataforma.

---

# Definição

Lenis é uma biblioteca de Smooth Scroll utilizada para criar uma navegação contínua, fluida e consistente.

Na Workstation IA, o Lenis será responsável exclusivamente pelo controle do scroll.

---

# Filosofia

O scroll deve transmitir sensação de continuidade.

O usuário nunca deverá perceber travamentos ou mudanças bruscas de velocidade.

A movimentação deve ser natural, previsível e confortável.

---

# Responsabilidades

Lenis é responsável por:

- Smooth Scroll
- Controle de velocidade
- Interpolação do movimento
- Suavização da navegação
- Integração com ScrollTrigger

---

# Não é responsabilidade

Lenis não controla:

- animações
- timelines
- transições
- componentes
- layout
- estilos

Essas responsabilidades pertencem ao GSAP e ao ScrollTrigger.

---

# Arquitetura

```
Usuário

↓

Scroll

↓

Lenis

↓

ScrollTrigger

↓

GSAP

↓

Interface
```

---

# Fluxo Oficial

```
Wheel

↓

Touch

↓

Lenis

↓

requestAnimationFrame

↓

ScrollTrigger.update()

↓

GSAP Timeline
```

---

# Instalação

```
npm install lenis
```

---

# Inicialização Oficial

O Lenis deverá possuir apenas uma instância por aplicação.

Nunca criar múltiplas instâncias.

---

# Estrutura Recomendada

```
src/

lib/

lenis.ts
```

Toda configuração deverá permanecer centralizada.

---

# Integração com GSAP

Fluxo oficial.

```
Lenis

↓

requestAnimationFrame

↓

GSAP Ticker

↓

ScrollTrigger.update()
```

O GSAP deverá ser informado sempre que o Lenis atualizar o scroll.

---

# Integração com React

Inicializar apenas uma vez.

Preferencialmente no Layout principal.

Nunca criar uma nova instância por página.

---

# Integração com Next.js

Inicializar no Root Layout.

Toda aplicação utilizará a mesma instância.

---

# Configuração Recomendada

Priorizar movimentos suaves.

Evitar configurações extremamente lentas.

O objetivo é melhorar a experiência, não atrasar a navegação.

---

# Compatibilidade

Compatível com:

- GSAP
- ScrollTrigger
- React
- Next.js
- Tailwind CSS

---

# Responsividade

O comportamento deverá ser consistente em:

- Desktop
- Notebook
- Tablet
- Mobile

---

# Performance

Manter apenas um ciclo de atualização.

Evitar múltiplos requestAnimationFrame.

Evitar múltiplos listeners.

---

# Acessibilidade

Respeitar usuários que desativarem animações.

Caso necessário, permitir desabilitar o Smooth Scroll.

---

# Casos de Uso

- Landing Pages
- Dashboards
- Storytelling
- Portfólios
- Sistemas Premium
- Interfaces Cinematográficas

---

# Boas Práticas

- Uma única instância.
- Configuração centralizada.
- Integrar sempre com ScrollTrigger.
- Não substituir comportamento nativo sem necessidade.
- Testar em diferentes navegadores.

---

# Padrão Oficial

Toda aplicação da Workstation IA que utilizar animações por scroll deverá utilizar Lenis.

Não utilizar bibliotecas concorrentes de Smooth Scroll.

---

# Ferramentas Homologadas

- Lenis
- GSAP
- ScrollTrigger
- React
- Next.js

---

# Referências Oficiais

- Lenis Documentation
- Studio Freight Lenis
- GSAP Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Lenis homologado como biblioteca oficial de Smooth Scroll.
- Arquitetura de integração definida.
- Boas práticas registradas.