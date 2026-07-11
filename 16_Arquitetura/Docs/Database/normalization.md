---
id: CKB-DB-0005
title: Database Normalization
module: Database
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: database/
dependencies:
  - modeling.md
  - entities.md
  - relationships.md
related:
  - indexing.md
  - performance.md
last_update: 2026-07
---

# Normalização

## Objetivo

Definir o padrão oficial de normalização utilizado pela Workstation IA.

Toda modelagem deverá seguir este documento antes de ser implementada.

---

# Definição

Normalização é o processo de organizar os dados para eliminar redundâncias, inconsistências e dependências inadequadas.

Seu objetivo é garantir:

- consistência
- integridade
- reutilização
- escalabilidade
- facilidade de manutenção

---

# Filosofia

Os dados devem existir apenas uma vez.

Toda duplicação deve possuir justificativa técnica.

Normalizar primeiro.

Desnormalizar somente quando houver ganho comprovado de desempenho.

---

# Processo Oficial

```
Requisitos

↓

MER

↓

DER

↓

1FN

↓

2FN

↓

3FN

↓

BCNF

↓

Implementação

↓

Testes

↓

Produção
```

---

# Primeira Forma Normal (1FN)

## Objetivo

Eliminar grupos repetitivos.

Garantir atomicidade.

---

## Regras

Cada campo deve possuir apenas um valor.

Não armazenar listas.

Não armazenar múltiplos valores na mesma coluna.

---

## Correto

```
user

id

name

email
```

---

## Incorreto

```
phones

"99999,88888"
```

---

# Segunda Forma Normal (2FN)

## Objetivo

Eliminar dependências parciais.

---

## Regras

Todos os atributos devem depender integralmente da chave primária.

---

## Correto

```
Pedido

↓

Cliente

↓

Produto
```

Cada entidade mantém apenas seus próprios atributos.

---

# Terceira Forma Normal (3FN)

## Objetivo

Eliminar dependências transitivas.

---

## Regra

Um atributo nunca deve depender de outro atributo que não seja a chave primária.

---

## Correto

```
Usuário

↓

Cidade_ID

↓

Tabela Cidade
```

Evitar repetir nome da cidade em várias tabelas.

---

# Boyce-Codd Normal Form (BCNF)

## Objetivo

Eliminar dependências restantes.

Utilizar quando houver modelos complexos.

---

# Formas Normais Adotadas

Obrigatório

```
1FN

2FN

3FN
```

Opcional

```
BCNF
```

quando necessário.

---

# Desnormalização

Permitida apenas quando houver:

- necessidade comprovada
- ganho mensurável
- documentação
- aprovação arquitetural

---

# Casos Permitidos

- Dashboards
- Business Intelligence
- Data Warehouse
- Relatórios
- Cache
- Materialized Views

---

# Casos Não Permitidos

Nunca duplicar dados apenas para facilitar consultas.

Nunca copiar atributos entre tabelas sem justificativa.

---

# Integridade

Toda normalização deverá preservar.

- integridade referencial
- integridade de domínio
- consistência dos dados

---

# Auditoria

Toda alteração estrutural deverá ser documentada.

Registrar:

- motivo
- impacto
- benefícios
- riscos

---

# Performance

Normalização prioriza consistência.

Performance será tratada por:

- índices
- cache
- consultas otimizadas
- paginação
- views

Nunca pela duplicação indiscriminada de dados.

---

# Integração

```
Modelagem

↓

Normalização

↓

SQLAlchemy

↓

Repository

↓

Service
```

---

# Exemplos

## Usuários

```
users

cities

states

countries
```

Nunca repetir cidade em todas as tabelas.

---

## Projetos

```
projects

status

categories

priorities
```

Cada informação pertence à sua própria entidade.

---

## Equipes

```
teams

users

team_users
```

Utilizar tabela associativa.

---

# Checklist

Antes de implementar verificar.

- Existe redundância?

- Existe dependência parcial?

- Existe dependência transitiva?

- Existe relacionamento correto?

- Existe documentação?

---

# Boas Práticas

- Modelar antes de programar.
- Utilizar 3FN como padrão.
- Documentar exceções.
- Evitar redundância.
- Utilizar tabelas associativas.
- Revisar o modelo periodicamente.

---

# Padrão Oficial

Toda estrutura da Workstation IA deverá atingir, no mínimo, a Terceira Forma Normal (3FN).

Qualquer desnormalização deverá ser documentada na Cortex Knowledge Base.

---

# Referências Oficiais

- Database System Concepts
- SQL Style Guide
- MySQL Documentation
- Database Design Best Practices
- Boyce-Codd Normal Form

---

# Changelog

## 1.0.0

- Documento criado.
- Processo oficial de normalização definido.
- Formas normais homologadas.
- Regras de desnormalização registradas.