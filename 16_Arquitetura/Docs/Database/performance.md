---
id: CKB-DB-0007
title: Database Indexing
module: Database
version: 1.0.0
status: Official
owner: Cortex
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: database/
dependencies:
  - mysql.md
  - normalization.md
  - migrations.md
related:
  - performance.md
  - security.md
  - ../backend/sqlalchemy.md
last_update: 2026-07
---

# Indexação

## Objetivo

Definir o padrão oficial para utilização de índices na Workstation IA.

Toda estratégia de indexação deverá priorizar desempenho sem comprometer a integridade dos dados.

---

# Definição

Índices são estruturas auxiliares utilizadas pelo banco para localizar registros com maior eficiência.

Eles reduzem drasticamente o tempo de leitura.

Em contrapartida, aumentam o custo de escrita.

---

# Filosofia

Criar apenas índices necessários.

Cada índice deverá possuir justificativa técnica.

Nunca indexar indiscriminadamente.

---

# Fluxo Oficial

```
Modelagem

↓

Relacionamentos

↓

Consultas

↓

Índices

↓

EXPLAIN

↓

Validação

↓

Produção
```

---

# Tipos Homologados

## PRIMARY KEY

Obrigatório.

Um por tabela.

---

## FOREIGN KEY

Obrigatório.

Toda chave estrangeira deverá possuir índice.

---

## UNIQUE

Utilizar quando o domínio exigir unicidade.

Exemplos.

```
email

cpf

cnpj

api_key
```

---

## INDEX

Índice convencional.

Utilizado para consultas frequentes.

---

## COMPOSITE INDEX

Índice composto.

Utilizar quando consultas utilizarem mais de uma coluna.

Exemplo.

```
(status_id, created_at)
```

---

## FULLTEXT

Utilizar apenas para pesquisas textuais.

Exemplos.

- documentação
- artigos
- comentários
- prompts

---

## BTREE

Estrutura padrão do MySQL.

Será utilizada por padrão.

---

## HASH

Utilizar somente quando suportado e houver justificativa.

---

# Campos Prioritários

Criar índices em.

- Foreign Keys
- Email
- Login
- Username
- Datas
- Status
- Categoria
- Projeto
- Usuário
- Campos utilizados em filtros

---

# Índices Compostos

Criar quando houver consultas recorrentes.

Exemplo.

```
project_id

status_id

created_at
```

---

# Não Indexar

Evitar índices em.

- TEXT muito grandes
- BOOLEAN isolado
- colunas pouco utilizadas
- campos com baixa seletividade

---

# EXPLAIN

Toda consulta importante deverá ser analisada.

Utilizar.

```sql
EXPLAIN
```

Objetivos.

- verificar índices
- identificar scans
- analisar joins
- medir custo

---

# Performance

Priorizar.

- índices pequenos
- consultas específicas
- joins eficientes
- paginação

Evitar.

- SELECT *
- ORDER BY sem índice
- LIKE iniciando com %
- consultas sem filtros

---

# Paginação

Obrigatória para grandes volumes.

Preferência.

```
LIMIT

OFFSET
```

ou Cursor Pagination quando necessário.

---

# ORDER BY

Sempre verificar se existe índice.

---

# JOIN

Toda tabela utilizada em JOIN deverá possuir índices apropriados.

---

# Monitoramento

Revisar periodicamente.

- índices não utilizados
- índices duplicados
- consultas lentas

---

# Atualizações

Índices impactam operações.

- INSERT
- UPDATE
- DELETE

Criar apenas quando houver benefício comprovado.

---

# SQLAlchemy

Declarar índices diretamente nos Models quando apropriado.

Exemplo.

```python
Index(
    "idx_user_email",
    User.email
)
```

---

# Migrações

Todo novo índice deverá ser criado através de migração.

Nunca criar índices manualmente em produção.

---

# Auditoria

Registrar.

- criação
- remoção
- alteração
- impacto esperado

---

# Casos de Uso

Índices homologados.

- Login
- Dashboard
- Projetos
- Tarefas
- Auditoria
- IA
- Relatórios
- APIs
- Pesquisa

---

# Checklist

Antes de criar um índice.

- A consulta é frequente?

- Existe ganho real?

- Há impacto de escrita?

- Existe índice semelhante?

- Foi executado EXPLAIN?

---

# Boas Práticas

- Indexar Foreign Keys.
- Utilizar índices compostos quando necessário.
- Monitorar consultas lentas.
- Evitar índices redundantes.
- Validar desempenho após cada migração.
- Documentar todos os índices críticos.

---

# Padrão Oficial

Toda estratégia de indexação da Workstation IA deverá seguir este documento.

Nenhum índice deverá ser criado sem análise técnica e validação de desempenho.

---

# Referências Oficiais

- MySQL Documentation
- MySQL Performance Schema
- SQLAlchemy Documentation
- High Performance MySQL
- Use The Index, Luke!

---

# Changelog

## 1.0.0

- Documento criado.
- Estratégia oficial de indexação definida.
- Padrões de desempenho registrados.
- Processo de validação documentado.