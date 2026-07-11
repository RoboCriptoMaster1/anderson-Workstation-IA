---
id: CKB-FE-0002
title: CSS3
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - html.md
related:
  - tailwind.md
  - gsap.md
  - react.md
last_update: 2026-07
---

# CSS3

## Objetivo

Definir os padrões oficiais de estilização da Workstation IA.

Toda interface deverá seguir este documento.

---

# Definição

CSS (Cascading Style Sheets) é responsável pela apresentação visual da interface.

Sua responsabilidade é exclusivamente visual.

---

# Responsabilidades

- layout
- tipografia
- cores
- espaçamento
- responsividade
- animações simples
- estados visuais

---

# Não é responsabilidade

- regras de negócio
- manipulação de dados
- requisições
- lógica
- persistência

---

# Filosofia

A interface da Workstation IA deve transmitir:

- profissionalismo
- clareza
- elegância
- simplicidade
- tecnologia
- consistência

---

# Organização

Cada módulo deverá possuir seus próprios arquivos.

Exemplo

```
css/

variables.css

reset.css

layout.css

components.css

utilities.css

animations.css

responsive.css
```

---

# Ordem de Importação

```
Reset

↓

Variables

↓

Typography

↓

Layout

↓

Components

↓

Utilities

↓

Responsive
```

---

# Variáveis

Todas as cores deverão utilizar Custom Properties.

Exemplo

```css
:root{

--bg:#0A0E14;

--surface:#121822;

--primary:#4FD8E8;

--secondary:#6C63FF;

--warning:#FFB238;

}
```

Nunca utilizar cores fixas repetidamente.

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

# Sistema de Espaçamento

Escala oficial

```
4

8

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

Evitar valores aleatórios.

---

# Layout

Priorizar:

CSS Grid

↓

Flexbox

↓

Position

Evitar layouts baseados em float.

---

# Responsividade

Mobile First.

Breakpoints oficiais

```
480px

768px

1024px

1280px

1536px
```

---

# Nomenclatura

Utilizar nomes descritivos.

Correto

```
dashboard-card

project-header

user-avatar
```

Evitar

```
box

item

teste

div1
```

---

# Componentes

Todo componente deve ser reutilizável.

Evitar CSS específico para apenas uma tela quando puder ser reutilizado.

---

# Estados

Sempre prever:

```
hover

focus

active

disabled

loading
```

---

# Sombras

Utilizar sombras discretas.

Evitar exageros.

---

# Bordas

Border Radius oficial

```
4px

8px

12px

16px

20px

24px
```

---

# Animações

CSS será utilizado apenas para:

- transitions
- hover
- focus
- microinterações

Toda animação complexa deverá utilizar GSAP.

---

# Performance

Evitar

- seletores complexos
- !important
- duplicação
- regras conflitantes

---

# Tailwind CSS

Tailwind é o framework oficial.

CSS puro será utilizado apenas quando necessário.

---

# Acessibilidade

Garantir

- contraste adequado
- foco visível
- legibilidade
- tamanhos acessíveis

---

# Integração

HTML

↓

CSS

↓

Tailwind

↓

GSAP

↓

React

↓

Next.js

---

# Boas Práticas

Utilizar variáveis.

Reutilizar classes.

Organizar por responsabilidade.

Documentar padrões visuais.

---

# Padrão Oficial

Toda estilização deverá seguir o Design System oficial da Workstation IA.

---

# Referências Oficiais

CSS Specifications

MDN Web Docs

W3C

Tailwind CSS Documentation

---

# Changelog

## 1.0.0

Documento criado.

Padrões oficiais definidos.