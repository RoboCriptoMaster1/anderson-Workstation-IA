---
id: CKB-KNOW-0009
title: Templates
module: Knowledge
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: knowledge/
dependencies:
  - architecture.md
  - conventions.md
  - patterns.md
  - checklists.md
related:
  - roadmap.md
  - decisions.md
  - glossary.md
last_update: 2026-07
---

# Templates

## Objetivo

Centralizar todos os templates oficiais utilizados pela Workstation IA.

Todo novo documento, módulo, agente, serviço, API ou componente deverá ser criado a partir destes modelos.

O objetivo é garantir padronização, rastreabilidade e integração automática com o Cortex.

---

# Filosofia

Não começar do zero.

Começar do padrão.

Toda documentação nasce de um template.

Todo template representa conhecimento consolidado.

---

# Estrutura

```
Templates

↓

Documentação

↓

Implementação

↓

Versionamento

↓

Knowledge Base
```

---

# Template de Documento

```yaml
---
id:
title:
module:
version:
status:
owner:
project:
author:
parent:
dependencies:
related:
last_update:
---
```

---

## Estrutura Obrigatória

```
Objetivo

Definição

Arquitetura

Fluxo

Boas Práticas

Padrão Oficial

Referências

Changelog
```

---

# Template README

```markdown
# Nome do Projeto

## Objetivo

## Arquitetura

## Tecnologias

## Estrutura

## Instalação

## Configuração

## Execução

## Testes

## Roadmap

## Licença
```

---

# Template ADR

```markdown
# ADR-XXXX

Título

Status

Autor

Data

Contexto

Problema

Alternativas

Decisão

Justificativa

Consequências

Referências
```

---

# Template de Módulo

```text
module/

README.md

models/

repositories/

services/

routes/

validators/

forms/

tests/

docs/
```

---

# Template Model

```python
class Entity(db.Model):

    __tablename__ = ""

    id = db.Column(...)

    created_at = ...

    updated_at = ...
```

---

# Template Repository

```python
class Repository:

    def create():

    def find_by_id():

    def update():

    def delete():

    def list():
```

---

# Template Service

```python
class Service:

    def execute():

    def validate():

    def process():
```

---

# Template Route

```python
@bp.route()

def endpoint():
```

---

# Template API

```http
GET

POST

PUT

PATCH

DELETE
```

Estrutura.

```
Request

↓

Validation

↓

Service

↓

Repository

↓

Response
```

---

# Template Endpoint

```json
{
    "success": true,
    "message": "",
    "data": {},
    "errors": []
}
```

---

# Template SQL

```sql
CREATE TABLE ...

PRIMARY KEY

FOREIGN KEY

INDEX
```

---

# Template Migration

```
Upgrade

↓

Validate

↓

Rollback

↓

Version
```

---

# Template Docker

```docker
Dockerfile

docker-compose.yml

.env

.dockerignore
```

---

# Template Teste

```python
def test_feature():

    assert ...
```

---

# Template Commit

```
feat:

fix:

docs:

style:

refactor:

test:

perf:

build:

ci:

chore:
```

---

# Template Branch

```
main

develop

feature/

bugfix/

hotfix/

release/
```

---

# Template Sprint

```markdown
Sprint

Objetivo

Backlog

Entregas

Riscos

Checklist

Retrospectiva
```

---

# Template Roadmap

```markdown
Versão

Objetivo

Módulos

Prioridade

Status

Entrega
```

---

# Template Prompt

```
Objetivo

↓

Contexto

↓

Entradas

↓

Regras

↓

Restrições

↓

Ferramentas

↓

Resultado Esperado
```

---

# Template Agente

```markdown
Nome

Missão

Especialidade

Ferramentas

Responsabilidades

Limites

Integrações

Workflows
```

---

# Template Workflow

```
Entrada

↓

Processamento

↓

Validação

↓

Resultado
```

---

# Template Knowledge

```markdown
Metadata

Objetivo

Definição

Arquitetura

Fluxo

Boas Práticas

Padrão Oficial

Referências

Changelog
```

---

# Template Checklist

```
Planejamento

Arquitetura

Implementação

Testes

Documentação

Validação

Entrega
```

---

# Template Changelog

```markdown
## x.y.z

Adicionado

Alterado

Corrigido

Removido
```

---

# Template Release

```markdown
Versão

Data

Objetivo

Mudanças

Correções

Dependências

Notas
```

---

# Template MCP Tool

```yaml
tool:

name:

description:

parameters:

permissions:

returns:

version:
```

---

# Template Memory

```yaml
memory:

id:

category:

priority:

created_at:

updated_at:

source:
```

---

# Template RAG

```yaml
document:

id:

module:

keywords:

embedding:

version:
```

---

# Integração

```
Templates

↓

Knowledge Base

↓

Cortex

↓

Claude

↓

Implementação
```

---

# Critérios

Todo template deverá.

- possuir metadata;
- possuir versão;
- possuir objetivo;
- seguir as convenções;
- ser reutilizável;
- possuir documentação.

---

# Boas Práticas

- Nunca criar documentos fora dos templates.
- Atualizar templates quando a arquitetura evoluir.
- Evitar duplicação.
- Versionar alterações.
- Padronizar toda a plataforma.

---

# Padrão Oficial

Todos os documentos, módulos, APIs, agentes, workflows e componentes da Workstation IA deverão ser criados utilizando os templates definidos neste documento.

O Cortex utilizará estes modelos para geração automática de novos artefatos da plataforma.

---

# Referências Oficiais

- Docs as Code
- Markdown Guide
- ADR Specification
- Conventional Commits
- Semantic Versioning
- Clean Architecture
- Domain Driven Design

---

# Changelog

## 1.0.0

- Documento criado.
- Templates oficiais da Workstation IA definidos.
- Modelos de documentação, código, APIs, IA e Knowledge Base homologados.