---
id: CKB-BE-0008
title: Forms
module: Backend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: backend/
dependencies:
  - validators.md
  - services.md
related:
  - routes.md
  - flask.md
  - fastapi.md
last_update: 2026-07
---

# Forms

## Objetivo

Definir o padrão oficial da camada Forms da Workstation IA.

Os Forms são responsáveis por estruturar e organizar os dados recebidos pela aplicação antes de serem enviados para validação e processamento.

---

# Definição

Forms representam a camada de entrada da aplicação.

Sua responsabilidade é organizar os dados recebidos da interface e disponibilizá-los para os Validators e Services.

Os Forms não executam regras de negócio.

---

# Filosofia

Forms estruturam.

Validators validam.

Services processam.

Repositories persistem.

Cada camada possui uma única responsabilidade.

---

# Responsabilidades

Os Forms são responsáveis por:

- receber dados da interface
- organizar informações
- definir estrutura dos campos
- aplicar validações básicas (quando suportado)
- preparar dados para os Validators
- padronizar entradas

---

# Não é responsabilidade

Forms nunca devem:

- acessar banco de dados
- executar regras de negócio
- autenticar usuários
- realizar consultas
- executar cálculos
- persistir informações
- controlar permissões

---

# Arquitetura

```
Request

↓

Route

↓

Form

↓

Validator

↓

Service

↓

Repository
```

---

# Fluxo Oficial

```
Usuário

↓

Interface

↓

Form

↓

Validator

↓

Service

↓

Repository

↓

Banco
```

---

# Estrutura

```
forms/

login_form.py

user_form.py

project_form.py

task_form.py

dashboard_form.py

settings_form.py
```

Cada domínio deverá possuir seu próprio Form.

---

# Nomeação

Sempre utilizar.

```
LoginForm

UserForm

ProjectForm

TaskForm

DashboardForm
```

---

# Organização

Cada Form deverá representar apenas uma operação.

Exemplo.

```
CreateUserForm

UpdateUserForm

LoginForm

RegisterForm
```

Evitar Forms extremamente grandes.

---

# Campos

Todo campo deverá possuir:

- nome
- tipo
- obrigatoriedade
- descrição
- valor padrão (quando aplicável)

---

# Tipos Suportados

```
String

Integer

Float

Boolean

Date

Datetime

Email

Password

URL

File

Select

Textarea
```

---

# Uploads

Os Forms deverão estruturar informações sobre arquivos enviados.

A validação de tamanho e formato pertence aos Validators.

---

# Dados Opcionais

Campos opcionais deverão possuir tratamento explícito.

Nunca assumir valores inexistentes.

---

# Dados Obrigatórios

Campos obrigatórios deverão ser claramente definidos.

---

# Integração com Validators

Fluxo oficial.

```
Form

↓

Validator

↓

Service
```

O Form nunca decide se os dados são válidos.

---

# Integração com Services

Os Services recebem dados estruturados pelos Forms.

Nunca acessar dados brutos diretamente da requisição.

---

# WTForms

Framework homologado para aplicações Flask.

Quando utilizado.

Cada Form deverá permanecer isolado por domínio.

---

# FastAPI

Nas APIs.

Os Forms poderão ser substituídos pelos Schemas do Pydantic.

O conceito permanece o mesmo.

Estruturar dados.

---

# Segurança

Nunca confiar nos dados recebidos.

Todo dado estruturado deverá passar pela camada Validator.

---

# Performance

Forms devem ser leves.

Não executar processamento pesado.

---

# Testes

Cada Form deverá possuir testes para:

- estrutura
- campos obrigatórios
- tipos
- comportamento esperado

---

# Integração

```
Interface

↓

Form

↓

Validator

↓

Service

↓

Repository
```

---

# Boas Práticas

- Um Form por operação.
- Nomes descritivos.
- Não implementar regras de negócio.
- Não acessar banco.
- Manter estrutura simples.
- Documentar campos importantes.

---

# Padrão Oficial

Forms representam a camada oficial de estruturação dos dados da Workstation IA.

Toda entrada deverá ser organizada nesta camada antes de seguir para validação e processamento.

---

# Referências Oficiais

- WTForms Documentation
- Flask-WTF Documentation
- Pydantic Documentation
- FastAPI Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Camada Forms oficializada.
- Fluxo de estruturação definido.
- Convenções registradas.