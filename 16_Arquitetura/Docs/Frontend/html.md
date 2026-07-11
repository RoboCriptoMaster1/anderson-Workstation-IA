---
id: CKB-FE-0001
title: HTML5
module: Frontend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: frontend/
dependencies:
  - css.md
  - javascript.md
related:
  - react.md
  - nextjs.md
last_update: 2026-07
---

# HTML5

## Objetivo

Definir os padrões oficiais para utilização do HTML na Workstation IA.

Este documento estabelece como toda interface deve ser estruturada.

---

# Definição

HTML (HyperText Markup Language) é a linguagem oficial de marcação utilizada para estruturar documentos web.

Na Workstation IA o HTML é responsável apenas pela estrutura semântica da interface.

---

# Responsabilidades

- estruturar conteúdo
- definir hierarquia
- melhorar acessibilidade
- facilitar SEO
- servir como base para CSS e JavaScript

---

# Não é responsabilidade do HTML

- estilização
- animações
- regras de negócio
- manipulação de dados
- lógica da aplicação

---

# Estrutura Oficial

```html
<!DOCTYPE html>

<html lang="pt-BR">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title></title>

</head>

<body>

</body>

</html>
```

---

# Estrutura Semântica

Sempre utilizar elementos semânticos.

```text
header

nav

main

section

article

aside

footer
```

Evitar:

```
div

div

div

div

div
```

quando existir um elemento apropriado.

---

# Hierarquia

Cada página deve possuir apenas um

```html
<h1>
```

Os demais títulos devem seguir sequência lógica.

```
h1

↓

h2

↓

h3

↓

h4
```

---

# Imagens

Sempre utilizar

```html
alt
```

Exemplo

```html
<img src="logo.png"
alt="Logo da Workstation IA">
```

---

# Links

Sempre utilizar URLs relativas quando possível.

Adicionar atributos de segurança para links externos.

```html
target="_blank"

rel="noopener noreferrer"
```

---

# Formulários

Todo formulário deverá possuir:

- label
- placeholder quando necessário
- validação
- mensagens de erro
- acessibilidade

---

# Inputs

Sempre utilizar o tipo correto.

Exemplos

```html
email

password

number

date

file

search

url

tel
```

---

# Botões

Nunca utilizar

```html
<div onclick="">
```

Sempre utilizar

```html
<button>
```

---

# IDs

Devem ser únicos.

---

# Classes

Devem representar função.

Evitar nomes genéricos.

Ruim

```
box

teste

item1
```

Bom

```
user-card

dashboard-header

project-list
```

---

# Organização

Cada página deverá possuir:

```
Header

↓

Navigation

↓

Main

↓

Sections

↓

Footer
```

---

# SEO

Utilizar:

- title
- meta description
- heading hierarchy
- alt
- semantic HTML

---

# Acessibilidade

Obrigatório:

- aria-label quando necessário
- alt em imagens
- contraste adequado
- navegação por teclado
- foco visível

---

# Performance

Evitar:

- HTML duplicado
- elementos desnecessários
- estrutura profunda

---

# Integração

HTML

↓

CSS

↓

JavaScript

↓

React

↓

Next.js

---

# Boas Práticas

Sempre utilizar HTML semântico.

Evitar excesso de divs.

Organizar estrutura antes da estilização.

Separar conteúdo da apresentação.

---

# Padrão Oficial

Toda interface da Workstation IA deverá ser construída inicialmente utilizando estrutura HTML semântica.

---

# Referências Oficiais

HTML Living Standard

MDN Web Docs

W3C

---

# Changelog

## 1.0.0

Documento criado.

Padrões oficiais definidos.