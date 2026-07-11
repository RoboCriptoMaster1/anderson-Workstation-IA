---
id: CKB-BE-0007
title: Validators
module: Backend
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: backend/
dependencies:
  - python.md
  - flask.md
related:
  - forms.md
  - services.md
  - routes.md
last_update: 2026-07
---

# Validators

## Objetivo

Definir a camada oficial de validação da Workstation IA.

Os Validators são responsáveis exclusivamente por validar dados antes que eles cheguem às regras de negócio.

---

# Definição

Validator é a camada responsável por verificar se os dados recebidos possuem formato válido.

Ela garante integridade estrutural.

Não decide regras de negócio.

---

# Filosofia

Validators verificam estrutura.

Services verificam regras.

Repositories persistem.

Cada camada possui uma única responsabilidade.

---

# Responsabilidades

Os Validators são responsáveis por validar:

- tipos
- formatos
- obrigatoriedade
- tamanho
- expressões regulares
- estrutura de objetos
- listas
- arquivos enviados

---

# Não é responsabilidade

Validators nunca devem:

- acessar banco
- verificar existência de usuários
- autenticar
- calcular valores
- aplicar regras de negócio
- executar consultas
- salvar informações

---

# Arquitetura

```
Request

↓

Route

↓

Validator

↓

Form

↓

Service

↓

Repository
```

---

# Fluxo Oficial

```
Entrada

↓

Validator

↓

Dados válidos

↓

Service
```

Caso inválido.

```
Entrada

↓

Validator

↓

Erro

↓

Response
```

---

# Estrutura

```
validators/

user_validator.py

project_validator.py

task_validator.py

auth_validator.py

dashboard_validator.py
```

Cada domínio deverá possuir seu próprio Validator.

---

# Nomeação

Sempre utilizar.

```
UserValidator

ProjectValidator

TaskValidator

AuthValidator
```

---

# Tipos de Validação

## Campos obrigatórios

Exemplo.

- nome
- email
- senha

---

## Tipos

Exemplo.

```
string

integer

boolean

float

date
```

---

## Comprimento

Exemplo.

```
mínimo

máximo
```

---

## Expressões Regulares

Exemplos.

- CPF
- CNPJ
- CEP
- telefone
- email
- URL

---

## Datas

Validar.

- formato
- datas futuras
- datas inválidas

---

## Arquivos

Validar.

- extensão
- tamanho
- tipo MIME

---

## Listas

Validar.

- quantidade
- tipos
- estrutura

---

# Mensagens

Toda validação deverá retornar mensagens claras.

Exemplo.

```
Email inválido.

Senha obrigatória.

Projeto não informado.
```

Evitar mensagens técnicas.

---

# Padronização

Formato oficial.

```json
{
  "success": false,
  "errors": [
    {
      "field": "email",
      "message": "E-mail inválido."
    }
  ]
}
```

---

# Organização

Separar validações por domínio.

Nunca criar Validators gigantes.

---

# Reutilização

Validações comuns deverão ser reutilizadas.

Exemplos.

- Email
- Senha
- UUID
- CPF
- Datas

---

# Segurança

Sempre validar:

- entradas do usuário
- parâmetros
- uploads
- payloads JSON
- query strings

Nunca confiar em dados recebidos.

---

# Performance

Executar validações antes de qualquer processamento pesado.

Evitar validações duplicadas.

---

# Testes

Cada Validator deverá possuir testes.

Testar:

- sucesso
- erro
- limites
- entradas inválidas
- valores nulos

---

# Integração

```
Route

↓

Validator

↓

Form

↓

Service
```

---

# Boas Práticas

- Validar cedo.
- Retornar mensagens claras.
- Não acessar banco.
- Não executar regras de negócio.
- Reutilizar validações.
- Escrever testes.

---

# Padrão Oficial

Validators representam a primeira barreira de proteção da aplicação.

Nenhuma regra de negócio deverá ser implementada nesta camada.

Toda validação estrutural deverá ocorrer antes da execução dos Services.

---

# Referências Oficiais

- Pydantic Documentation
- WTForms Documentation
- Marshmallow Documentation
- OWASP Input Validation Cheat Sheet

---

# Changelog

## 1.0.0

- Documento criado.
- Camada Validator oficializada.
- Fluxo de validação definido.
- Padrões registrados.