---
id: CKB-DB-0006
title: Database Migrations
module: Database
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: database/
dependencies:
  - mysql.md
  - modeling.md
  - normalization.md
related:
  - ../backend/sqlalchemy.md
  - ../backend/flask.md
last_update: 2026-07
---

# Migrações

## Objetivo

Definir o padrão oficial para criação, controle e execução de migrações de banco de dados da Workstation IA.

Toda alteração estrutural deverá ser realizada através de migrações versionadas.

Alterações manuais em produção são proibidas.

---

# Definição

Migração é um conjunto de instruções versionadas responsáveis por evoluir ou restaurar a estrutura do banco de dados.

As migrações fazem parte do código-fonte.

Devem ser rastreadas pelo Git.

---

# Filosofia

O banco evolui junto com o software.

Nenhuma alteração estrutural poderá existir sem migração correspondente.

Toda mudança deverá ser reproduzível.

---

# Ferramentas Oficiais

Flask

```
Flask-Migrate
```

Engine

```
Alembic
```

ORM

```
SQLAlchemy
```

---

# Fluxo Oficial

```
Model

↓

Migration

↓

Review

↓

Git

↓

Deploy

↓

Produção
```

---

# Estrutura

```
migrations/

versions/

env.py

script.py.mako

alembic.ini
```

---

# Inicialização

Criar estrutura.

```bash
flask db init
```

---

# Criar Migração

Sempre utilizar.

```bash
flask db migrate -m "descrição"
```

Exemplo.

```bash
flask db migrate -m "create users table"
```

---

# Aplicar Migração

```bash
flask db upgrade
```

---

# Reverter

```bash
flask db downgrade
```

---

# Histórico

Visualizar histórico.

```bash
flask db history
```

---

# Revisão Atual

```bash
flask db current
```

---

# Revisão Mais Recente

```bash
flask db heads
```

---

# Processo Oficial

```
Alterar Model

↓

Gerar Migration

↓

Revisar SQL

↓

Executar Testes

↓

Commit

↓

Deploy
```

---

# Versionamento

Cada migração representa uma versão da estrutura do banco.

Nunca editar migrações antigas já aplicadas em produção.

Sempre criar uma nova migração.

---

# Convenção de Nome

Utilizar nomes descritivos.

Correto.

```
create_users_table

add_status_to_projects

create_tasks_table

add_indexes_users
```

Evitar.

```
update

teste

migration2
```

---

# Alterações Permitidas

- criar tabela
- remover tabela
- adicionar coluna
- remover coluna
- alterar índice
- alterar constraint
- criar relacionamento
- remover relacionamento

---

# Alterações Críticas

Devem possuir:

- backup
- revisão
- testes
- plano de rollback

---

# Rollback

Toda migração deverá permitir retorno seguro quando possível.

Antes do rollback:

- verificar dependências
- validar perda de dados
- executar backup

---

# Produção

Fluxo obrigatório.

```
Backup

↓

Migration

↓

Validação

↓

Monitoramento
```

Nunca aplicar migrações diretamente sem backup.

---

# Ambientes

Cada ambiente deverá possuir banco próprio.

```
Development

Testing

Staging

Production
```

Nunca compartilhar banco entre ambientes.

---

# Integridade

Após cada migração verificar.

- Foreign Keys
- Índices
- Constraints
- Relacionamentos
- Dados

---

# Performance

Após alterações estruturais.

Executar.

- EXPLAIN
- análise de índices
- testes de consulta

---

# Documentação

Toda migração deverá registrar.

- objetivo
- autor
- data
- impacto
- rollback
- módulos afetados

---

# Auditoria

Registrar.

- revisão
- aprovação
- execução
- ambiente
- versão

---

# Integração

```
Model

↓

Migration

↓

Alembic

↓

SQLAlchemy

↓

MySQL
```

---

# Casos de Uso

Exemplos.

- criação de módulos
- novos relacionamentos
- novos índices
- evolução da arquitetura
- otimização de tabelas
- auditoria

---

# Boas Práticas

- Nunca alterar produção manualmente.
- Nunca editar migrações antigas.
- Criar migrações pequenas.
- Revisar SQL gerado.
- Executar testes.
- Criar backups.
- Documentar alterações.

---

# Padrão Oficial

Toda evolução estrutural da Workstation IA deverá ocorrer exclusivamente através de migrações versionadas.

Qualquer alteração manual será considerada uma violação da arquitetura oficial do Cortex.

---

# Referências Oficiais

- Alembic Documentation
- Flask-Migrate Documentation
- SQLAlchemy Documentation
- MySQL Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Estratégia oficial de migrações definida.
- Processo de versionamento homologado.
- Política de rollback documentada.