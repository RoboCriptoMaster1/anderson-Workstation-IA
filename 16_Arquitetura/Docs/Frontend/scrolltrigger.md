---
id: CKB-FE-0009
title: ScrollTrigger
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - gsap.md
  - lenis.md
related:
  - react.md
  - nextjs.md
last_update: 2026-07
---

# ScrollTrigger

## Objetivo

Definir o padrão oficial para utilização do ScrollTrigger na Workstation IA.

O ScrollTrigger é o plugin oficial responsável por todas as animações controladas por scroll.

---

# Definição

ScrollTrigger é um plugin do GSAP que sincroniza animações com a posição do scroll da página.

Na Workstation IA, nenhuma animação baseada em scroll deverá ser implementada fora do ScrollTrigger.

---

# Filosofia

O scroll deve contar uma história.

Cada seção deve representar uma etapa da experiência do usuário.

O usuário não apenas navega.

Ele percorre uma narrativa.

---

# Responsabilidades

ScrollTrigger é responsável por:

- controlar animações por scroll
- sincronizar timelines
- pin sections
- revelar elementos
- controlar progresso
- iniciar e finalizar animações

---

# Não é responsabilidade

ScrollTrigger não controla:

- Smooth Scroll
- Layout
- Estilização
- Regras de negócio

---

# Arquitetura

```
Usuário

↓

Lenis

↓

ScrollTrigger

↓

GSAP Timeline

↓

Componentes
```

---

# Fluxo Oficial

```
Scroll

↓

ScrollTrigger

↓

Timeline

↓

Animação

↓

Renderização
```

---

# Configuração Oficial

Registrar o plugin.

```javascript
gsap.registerPlugin(ScrollTrigger)
```

---

# Estrutura Recomendada

```
animations/

scroll/

hero-scroll.ts

cards-scroll.ts

timeline-scroll.ts

dashboard-scroll.ts
```

---

# Trigger

Toda animação deve possuir um elemento gatilho.

Exemplo

```
trigger:

".hero"

".dashboard"

".cards"

".timeline"
```

Nunca utilizar elementos genéricos quando houver identificadores específicos.

---

# Start

Priorizar.

```
top 80%

top 75%

top center

top bottom
```

---

# End

Sempre definir quando necessário.

Exemplo.

```
bottom center

bottom top

+=500
```

---

# Scrub

Utilizar quando houver sincronização contínua.

```
scrub: true

ou

scrub: 1
```

Evitar scrub em microinterações.

---

# Pin

Utilizar apenas em experiências cinematográficas.

Exemplos.

- Hero
- Storytelling
- Roadmap
- Timeline
- Dashboards

Evitar excesso de Pin.

---

# Toggle Actions

Configuração recomendada.

```
play

reverse

restart

none
```

Escolher conforme experiência desejada.

---

# Match Media

Responsividade obrigatória.

Utilizar.

```javascript
ScrollTrigger.matchMedia()
```

para adaptar animações entre:

- Desktop
- Tablet
- Mobile

---

# Refresh

Sempre atualizar quando necessário.

Exemplo.

```
ScrollTrigger.refresh()
```

Após:

- carregamento de imagens
- mudança dinâmica de layout
- carregamento assíncrono

---

# Timelines

Priorizar.

```
Timeline

↓

ScrollTrigger

↓

Stagger

↓

Labels
```

Evitar múltiplos triggers independentes para a mesma sequência.

---

# Storytelling

Fluxo recomendado.

```
Entrada

↓

Foco

↓

Movimento

↓

Saída

↓

Próxima Seção
```

---

# Performance

Animar apenas.

```
transform

opacity
```

Evitar:

- width
- height
- margin
- top
- left

quando possível.

---

# GPU

Priorizar.

```
translate3d()

scale()

rotate()

opacity
```

---

# Integração com Lenis

Fluxo oficial.

```
Lenis

↓

requestAnimationFrame

↓

ScrollTrigger.update()

↓

GSAP
```

Nunca utilizar Smooth Scroll diferente do Lenis sem justificativa técnica.

---

# Integração com React

Inicializar após montagem.

Utilizar.

```
useGSAP()

ou

useLayoutEffect()
```

---

# Integração com Next.js

Executar apenas em Client Components.

```
"use client"
```

---

# Casos de Uso

- Hero Cinemático
- Storytelling
- Dashboards
- Landing Pages
- Roadmaps
- Timelines
- Cards
- Reveal
- Progress Indicators

---

# Acessibilidade

Respeitar.

```
prefers-reduced-motion
```

Toda animação deverá possuir comportamento degradável.

---

# Boas Práticas

- Utilizar timelines.
- Organizar animações por módulo.
- Evitar excesso de ScrollTriggers.
- Documentar animações complexas.
- Testar em múltiplos dispositivos.
- Manter fluidez acima de efeitos.

---

# Padrão Oficial

Toda animação baseada em scroll deverá utilizar ScrollTrigger.

Nenhuma implementação deverá utilizar eventos manuais de scroll quando o ScrollTrigger atender ao requisito.

---

# Ferramentas Homologadas

- GSAP
- ScrollTrigger
- Lenis
- React
- Next.js

---

# Referências Oficiais

- GSAP ScrollTrigger Documentation
- GreenSock Learning Center
- GSAP React Guide

---

# Changelog

## 1.0.0

- Documento criado.
- ScrollTrigger homologado como padrão oficial para animações de scroll.
- Arquitetura de Scroll definida.
- Boas práticas registradas.