---
id: CKB-KNOW-0003
title: Glossary
module: Knowledge
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: knowledge/
dependencies:
  - architecture.md
  - decisions.md
related:
  - conventions.md
  - roadmap.md
  - ../ai/cortex.md
last_update: 2026-07
---

# Glossário

## Objetivo

Definir o vocabulário oficial da Workstation IA.

Este documento padroniza todos os termos técnicos utilizados pela plataforma.

Todo módulo, agente, documentação e código deverão utilizar estas definições.

---

# Filosofia

A mesma palavra deve possuir o mesmo significado em toda a plataforma.

Não existirão interpretações diferentes para um mesmo conceito.

---

# Hierarquia

```
Termo

↓

Definição

↓

Contexto

↓

Exemplo

↓

Documentação Relacionada
```

---

# A

## Agent

Unidade especializada de inteligência coordenada pelo Cortex.

Cada agente possui responsabilidades específicas.

Exemplos.

- Frontend Agent
- Backend Agent
- Database Agent
- Security Agent

---

## API

Interface responsável pela comunicação entre sistemas.

Na Workstation IA todas seguem padrão REST.

---

## Architecture

Conjunto de decisões estruturais que definem como a plataforma é construída.

---

## ADR

Architectural Decision Record.

Documento que registra decisões arquiteturais permanentes.

---

# B

## Backend

Camada responsável pela lógica de negócio da plataforma.

Inclui.

- Flask
- SQLAlchemy
- Services
- Repositories
- Routes

---

## Blueprint

Mecanismo do Flask utilizado para organizar rotas por domínio.

---

## Business Rule

Regra de negócio implementada na camada Service.

---

# C

## Claude

Motor de raciocínio utilizado pelo Cortex.

Responsável pela análise, planejamento e geração de soluções.

Claude não representa a inteligência da plataforma.

Ele executa o raciocínio do Cortex.

---

## Context

Conjunto de informações utilizadas para compreender uma solicitação.

Inclui.

- projeto
- arquitetura
- memória
- documentação
- histórico

---

## CRUD

Operações fundamentais.

```
Create

Read

Update

Delete
```

---

## Cortex

Sistema Cognitivo Oficial da Workstation IA.

Responsável por.

- organizar conhecimento
- coordenar agentes
- manter memória
- consultar documentação
- decidir estratégias

É a inteligência central da plataforma.

---

# D

## Database

Camada responsável pela persistência dos dados.

---

## Documentation

Conjunto oficial de documentos da Knowledge Base.

---

## Docker

Tecnologia utilizada para padronizar ambientes.

---

# E

## Entity

Objeto do domínio representado no banco de dados.

---

## Embedding

Representação vetorial utilizada para indexação semântica.

Aplicado no RAG.

---

# F

## Frontend

Camada responsável pela interface do usuário.

Inclui.

- HTML
- CSS
- JavaScript
- React
- GSAP

---

## Form

Objeto responsável por estruturar entradas de dados.

---

# G

## Git

Sistema oficial de versionamento.

---

## GitHub

Repositório oficial dos projetos.

---

# I

## Index

Estrutura utilizada para acelerar consultas no banco.

---

## Infrastructure

Conjunto de recursos responsáveis pela execução da plataforma.

---

# K

## Knowledge Base

Fonte oficial de conhecimento da Workstation IA.

Toda informação permanente deverá existir aqui.

---

## KPI

Indicador-chave de desempenho.

Utilizado pelo módulo BI.

---

# L

## Long Memory

Memória permanente do Cortex.

Armazena.

- arquitetura
- padrões
- decisões
- preferências permanentes

---

# M

## Markdown

Formato oficial da documentação da plataforma.

---

## Memory

Sistema responsável pela memória do Cortex.

Possui.

- Short Memory
- Working Memory
- Long Memory

---

## Migration

Alteração versionada da estrutura do banco.

---

## Module

Agrupamento lógico de funcionalidades.

Exemplos.

- frontend
- backend
- database
- ai

---

## MCP

Model Context Protocol.

Barramento oficial de comunicação entre Claude, Cortex e ferramentas.

---

# N

## Node

Unidade lógica da arquitetura.

Pode representar módulos, componentes ou etapas de um workflow.

---

# O

## ORM

Object Relational Mapping.

Na plataforma utiliza-se SQLAlchemy.

---

# P

## Pattern

Padrão arquitetural adotado oficialmente.

---

## Prompt

Instrução estruturada enviada ao Claude.

---

## Prompt Engineering

Processo de construção de prompts consistentes.

---

## Project

Conjunto organizado de funcionalidades pertencentes à Workstation IA.

---

# R

## RAG

Retrieval-Augmented Generation.

Sistema responsável por recuperar conhecimento antes do raciocínio.

---

## Repository

Camada responsável pelo acesso ao banco.

Nunca implementa regra de negócio.

---

## Route

Camada responsável por receber requisições HTTP.

---

## Roadmap

Planejamento evolutivo da plataforma.

---

# S

## Service

Camada responsável pela regra de negócio.

---

## Sprint

Período de desenvolvimento contendo objetivos específicos.

---

## SQLAlchemy

ORM oficial da Workstation IA.

---

## Security

Conjunto de políticas responsáveis pela proteção da plataforma.

---

# T

## Task

Unidade de trabalho dentro da plataforma.

---

## Tool

Ferramenta disponibilizada através do MCP.

---

## Tool Calling

Processo de seleção e execução de ferramentas pelo Cortex.

---

## Template

Arquivo responsável pela renderização da interface.

---

# U

## User

Pessoa autenticada na plataforma.

---

# V

## Validator

Camada responsável pela validação de dados.

---

## Version

Identificador oficial de evolução dos documentos e módulos.

---

# W

## Workflow

Fluxo padronizado de execução de uma atividade.

Todos os workflows são coordenados pelo Cortex.

---

## Working Memory

Memória operacional do Cortex.

Armazena contexto do projeto em andamento.

---

## Workspace

Ambiente lógico de trabalho da Workstation IA.

Pode representar um projeto, equipe ou contexto operacional.

---

# Princípios

Todos os documentos deverão utilizar exatamente as definições descritas neste glossário.

Novos termos deverão ser registrados antes de serem utilizados oficialmente.

---

# Atualizações

Sempre que um novo conceito arquitetural surgir.

Criar.

```
Novo Termo

↓

Nova Definição

↓

Relacionamentos

↓

Versionamento
```

---

# Boas Práticas

- Utilizar terminologia oficial.
- Evitar sinônimos desnecessários.
- Atualizar o glossário continuamente.
- Referenciar documentos relacionados.
- Manter definições objetivas.

---

# Padrão Oficial

O Glossário representa o vocabulário oficial da Workstation IA.

Toda documentação, código, Knowledge Base, agentes e módulos deverão utilizar os termos definidos neste documento.

---

# Referências Oficiais

- IEEE Software Engineering Glossary
- Domain Driven Design
- Clean Architecture
- Anthropic Documentation
- Model Context Protocol (MCP)

---

# Changelog

## 1.0.0

- Documento criado.
- Vocabulário oficial da Workstation IA definido.
- Conceitos centrais do Cortex documentados.
- Terminologia padronizada para toda a plataforma.