---
id: CKB-FE-0007
title: Tailwind CSS
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
related:
  - react.md
  - nextjs.md
  - gsap.md
last_update: 2026-07
---

# Tailwind CSS

## Objetivo

Definir o padrão oficial para utilização do Tailwind CSS na Workstation IA.

Tailwind CSS é o framework oficial de estilização da plataforma.

---

# Definição

Tailwind CSS é um framework Utility First utilizado para construir interfaces modernas, consistentes e altamente reutilizáveis.

Na Workstation IA ele substitui a maior parte do CSS tradicional.

---

# Objetivos

- Padronização
- Produtividade
- Escalabilidade
- Reutilização
- Consistência Visual
- Facilidade de Manutenção

---

# Filosofia

A interface deve ser construída através da composição de pequenas utilidades.

Evitar CSS customizado quando uma Utility oficial resolver o problema.

---

# Estrutura

```
src/

styles/

globals.css

tailwind.config.ts

postcss.config.js
```

---

# Configuração Oficial

Framework

```
Tailwind CSS
```

Linguagem

```
TypeScript
```

Integração

```
React

Next.js
```

---

# Design Tokens

Toda identidade visual deverá utilizar Design Tokens.

Exemplo

```
Primary

Secondary

Success

Warning

Danger

Surface

Background

Border

Text
```

Nunca utilizar valores aleatórios espalhados pela aplicação.

---

# Paleta Oficial

```
Background

#0A0E14

Surface

#121822

Primary

#4FD8E8

Secondary

#6C63FF

Warning

#FFB238

Text

#E8ECF1

Text Secondary

#8996A8
```

---

# Tipografia Oficial

Display

```
Space Grotesk
```

Interface

```
Inter
```

Código

```
JetBrains Mono
```

---

# Espaçamento

Escala oficial

```
1

2

4

6

8

10

12

16

20

24

32

40

48

64

80

96
```

Evitar medidas fora da escala.

---

# Layout

Prioridade

```
Grid

↓

Flex

↓

Position
```

---

# Componentização

Classes repetidas deverão ser abstraídas em componentes React.

Evitar copiar blocos grandes de classes.

---

# Responsividade

Breakpoints oficiais

```
sm

md

lg

xl

2xl
```

Toda interface deverá ser Mobile First.

---

# Estados

Utilizar variantes oficiais.

```
hover

focus

active

disabled

group-hover

peer
```

---

# Dark Mode

Dark Mode é o padrão oficial da Workstation IA.

Todas as interfaces deverão ser projetadas inicialmente para tema escuro.

Suporte ao tema claro poderá ser implementado posteriormente.

---

# CSS Customizado

Permitido apenas quando:

- Tailwind não oferecer solução
- integração com bibliotecas externas
- animações específicas
- compatibilidade

---

# Plugins Homologados

- Typography
- Forms
- Aspect Ratio
- Container Queries

Novos plugins deverão ser avaliados antes da adoção.

---

# Organização

Separar:

```
Layout

↓

Componentes

↓

Utilities

↓

Animações
```

---

# Integração com GSAP

Tailwind define aparência.

GSAP controla movimento.

Nunca utilizar Tailwind para substituir animações complexas.

---

# Performance

Evitar:

- classes duplicadas
- estilos inline
- CSS desnecessário
- componentes gigantes

Priorizar reutilização.

---

# Boas Práticas

- Utilizar Design Tokens.
- Criar componentes reutilizáveis.
- Evitar CSS fora do padrão.
- Utilizar nomenclatura consistente.
- Documentar componentes compartilhados.

---

# Padrão Oficial

Tailwind CSS é o framework oficial de estilização da Workstation IA.

Todo novo projeto deverá utilizá-lo como primeira escolha.

---

# Ferramentas Homologadas

- Tailwind CSS
- React
- Next.js
- TypeScript
- PostCSS
- Autoprefixer

---

# Referências Oficiais

- Tailwind CSS Documentation
- Tailwind UI
- Headless UI
- MDN Web Docs

---

# Changelog

## 1.0.0

- Documento criado.
- Tailwind CSS homologado como framework oficial.
- Padrões visuais definidos.
- Design System integrado ao Cortex.