---
id: CKB-FE-0008
title: GSAP
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - react.md
  - nextjs.md
  - tailwind.md
related:
  - scrolltrigger.md
  - lenis.md
  - framer-motion.md
last_update: 2026-07
---

# GSAP

## Objetivo

Definir os padrões oficiais para utilização do GSAP na Workstation IA.

GSAP é a biblioteca oficial responsável por todas as animações da plataforma.

---

# Definição

GSAP (GreenSock Animation Platform) é a biblioteca oficial de animação da Workstation IA.

Toda animação de alto nível deverá ser implementada utilizando GSAP.

---

# Filosofia

As animações da plataforma devem transmitir:

- fluidez
- elegância
- precisão
- continuidade
- sensação de produto premium

O objetivo não é apenas animar.

É comunicar.

---

# Responsabilidades

GSAP é responsável por:

- animações
- timelines
- sequenciamento
- transições
- storytelling
- motion design
- microinterações
- animações complexas

---

# Não é responsabilidade

GSAP não substitui:

- React
- Next.js
- Tailwind CSS
- CSS Layout

Cada tecnologia possui sua responsabilidade.

---

# Arquitetura

```
React

↓

Next.js

↓

GSAP

↓

ScrollTrigger

↓

Lenis

↓

Usuário
```

---

# Plugins Homologados

Plugins oficiais homologados pelo Cortex.

- ScrollTrigger
- SplitText
- Flip
- MotionPath
- Observer
- ScrollSmoother (quando licenciado)
- Draggable (quando necessário)

---

# Organização

Estrutura recomendada.

```
animations/

hero.ts

cards.ts

dashboard.ts

timeline.ts

navigation.ts

loading.ts

transitions.ts
```

---

# Timelines

Toda sequência complexa deverá utilizar:

```
gsap.timeline()
```

Evitar múltiplos `gsap.to()` independentes quando existir relação entre animações.

---

# Sequenciamento

Priorizar:

```
Timeline

↓

Labels

↓

Stagger

↓

Callbacks
```

Evitar sincronização manual.

---

# Scroll

Toda animação baseada em scroll deverá utilizar:

```
ScrollTrigger
```

Nunca utilizar listeners de scroll manuais quando o ScrollTrigger resolver o problema.

---

# Scroll Suave

Smooth Scroll oficial.

```
Lenis
```

Fluxo oficial.

```
Lenis

↓

ScrollTrigger

↓

GSAP
```

---

# Easing Oficial

Priorizar.

```
power2.out

power3.out

power4.out

expo.out
```

Evitar:

```
linear

bounce

elastic
```

Exceto quando fizer parte do conceito visual.

---

# Duração

Microinterações

```
0.20s

↓

0.40s
```

Componentes

```
0.40s

↓

0.80s
```

Transições

```
0.80s

↓

1.60s
```

Storytelling

Livre.

---

# Stagger

Sempre utilizar quando houver múltiplos elementos.

Exemplo.

```
0.05

↓

0.20
```

---

# Performance

Utilizar sempre:

```
transform

opacity
```

Evitar animar:

- width
- height
- top
- left

quando houver alternativa utilizando transform.

---

# GPU

Priorizar propriedades aceleradas por GPU.

```
translate

scale

rotate

opacity
```

---

# Responsividade

Toda animação deverá funcionar em:

- Desktop
- Tablet
- Mobile

Caso necessário utilizar:

```
ScrollTrigger.matchMedia()
```

---

# Acessibilidade

Respeitar:

```
prefers-reduced-motion
```

Usuários que desativarem animações deverão possuir experiência funcional.

---

# Organização dos Arquivos

Separar animações por domínio.

Exemplo.

```
Hero

Dashboard

Sidebar

Cards

Forms

Tables

Charts

Landing
```

---

# Integração com React

Sempre utilizar:

```
useGSAP()
```

ou

```
useLayoutEffect()
```

quando apropriado.

Nunca iniciar animações antes da montagem completa do componente.

---

# Integração com Next.js

Em componentes Client.

```
"use client"
```

Toda animação deverá ocorrer após hidratação.

---

# Padrões Visuais

As animações deverão transmitir.

- continuidade
- profundidade
- contexto
- direção
- hierarquia

Nunca apenas movimento.

---

# Boas Práticas

- Utilizar timelines.
- Organizar animações em módulos.
- Evitar duplicação.
- Reutilizar sequências.
- Documentar animações complexas.
- Testar em diferentes resoluções.

---

# Padrão Oficial

GSAP é a única biblioteca oficial para animações complexas da Workstation IA.

Qualquer exceção deverá ser documentada e aprovada pelo Cortex.

---

# Ferramentas Homologadas

- GSAP
- ScrollTrigger
- SplitText
- Flip
- Lenis
- React
- Next.js

---

# Referências Oficiais

- GSAP Documentation
- GreenSock Learning Center
- GSAP React Guide

---

# Changelog

## 1.0.0

- Documento criado.
- GSAP homologado como biblioteca oficial de animações.
- Arquitetura Motion definida.
- Padrões de animação registrados.