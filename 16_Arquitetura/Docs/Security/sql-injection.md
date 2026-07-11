---
id: CKB-SEC-0014
title: SQL Injection
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - xss.md
  - api-security.md
  - ../database/readme.md
related:
  - logging.md
  - audit.md
  - vulnerability-management.md
last_update: 2026-07
---

# SQL Injection

## Objetivo

Definir oficialmente a arquitetura de proteção contra ataques de SQL Injection da Workstation IA.

Este documento estabelece políticas obrigatórias para impedir que comandos SQL maliciosos sejam executados através de entradas fornecidas por usuários, aplicações externas, APIs, Cortex, Agentes Inteligentes ou servidores MCP.

---

# Filosofia

Toda entrada é potencialmente maliciosa.

Nenhum dado recebido poderá ser utilizado diretamente em consultas SQL.

A segurança deverá ser garantida pela arquitetura.

---

# Missão

Garantir.

- Integridade dos dados
- Confidencialidade
- Disponibilidade
- Consultas seguras
- Auditoria completa

---

# Arquitetura

```
Cliente

↓

Input

↓

Validation

↓

Prepared Statement

↓

ORM

↓

Database

↓

Response
```

---

# Escopo

Aplica-se a.

- APIs REST
- GraphQL
- Painéis Administrativos
- Dashboards
- Cortex
- Agentes Inteligentes
- MCP
- Scripts internos
- ETL
- Jobs

---

# Tipos de SQL Injection

Proteger contra.

```
Classic SQL Injection

Blind SQL Injection

Boolean-Based

Time-Based

Union Injection

Second-Order SQL Injection

Stacked Queries
```

---

# Regra Principal

Nunca concatenar SQL utilizando dados externos.

Proibido.

```sql
SELECT * FROM users
WHERE email = '" + email + "'";
```

---

# Obrigatório

Utilizar.

```
Prepared Statements
```

ou.

```
Queries Parametrizadas
```

---

# Exemplo Seguro

```sql
SELECT *
FROM users
WHERE email = ?
```

---

# ORM

Todos os acessos ao banco deverão utilizar ORM quando possível.

Exemplos.

```
SQLAlchemy

Entity Framework

Hibernate

Prisma
```

---

# Consultas Nativas

Quando inevitáveis.

Obrigatório.

- parâmetros
- validação
- revisão
- auditoria

---

# Stored Procedures

Permitidas.

Desde que.

- parametrizadas
- revisadas
- documentadas

---

# Entrada

Toda entrada deverá passar por.

- validação
- normalização
- tipagem
- sanitização

Antes da camada de persistência.

---

# Lista de Campos

Ordenação.

```
ORDER BY
```

Filtros.

```
WHERE
```

Colunas dinâmicas deverão utilizar listas explícitas de campos permitidos.

Nunca aceitar nomes de tabelas ou colunas diretamente do usuário.

---

# Paginação

```
LIMIT

OFFSET
```

deverão utilizar valores validados.

---

# Banco de Dados

Compatível com.

```
PostgreSQL

MySQL

MariaDB

SQL Server

Oracle
```

---

# Permissões

A conta utilizada pela aplicação deverá possuir.

Somente.

- SELECT
- INSERT
- UPDATE
- DELETE

quando necessários.

Nunca utilizar contas administrativas na aplicação.

---

# Menor Privilégio

Cada serviço possuirá.

- usuário próprio
- permissões mínimas
- isolamento

---

# Logs

Nunca registrar.

- consultas contendo credenciais
- dados pessoais completos
- segredos
- tokens

---

# Tratamento de Erros

Nunca retornar.

- SQL
- Stack Trace
- Nome de tabelas
- Nome de colunas
- Mensagens do banco

Ao cliente.

---

# Cortex

O Cortex nunca construirá consultas SQL por concatenação.

Toda consulta deverá utilizar.

- ORM
- parâmetros
- camada Repository

---

# Agentes Inteligentes

Os agentes nunca acessarão diretamente o banco.

Fluxo.

```
Agente

↓

Repository

↓

ORM

↓

Database
```

---

# MCP

Ferramentas MCP seguirão exatamente a mesma política.

Nenhum comando SQL será executado sem parametrização.

---

# Auditoria

Registrar.

- consultas críticas
- tentativas bloqueadas
- erros
- origem
- usuário
- horário

---

# Monitoramento

Monitorar.

- payloads suspeitos
- UNION SELECT
- SLEEP()
- BENCHMARK()
- OR 1=1
- comentários SQL
- tentativas repetidas

---

# Segurança

Proibido.

- concatenação SQL
- EXEC dinâmico sem validação
- contas DBA
- SQL construído manualmente
- exposição de mensagens do banco

---

# Testes

Obrigatórios.

- testes automatizados
- SAST
- DAST
- testes de penetração
- fuzzing

---

# Conformidade

Compatível com.

- OWASP Top 10
- OWASP ASVS
- NIST SP 800-53
- ISO 27001
- CIS Controls

---

# Fluxo Oficial

```
Input

↓

Validation

↓

Prepared Statement

↓

ORM

↓

Database

↓

Audit

↓

Response
```

---

# Checklist

Antes da implantação.

- Prepared Statements implementados.

- ORM configurado.

- Conta de banco com menor privilégio.

- Logs protegidos.

- Auditoria ativa.

- Testes SAST executados.

- Testes DAST executados.

---

# Boas Práticas

- Utilizar sempre consultas parametrizadas.
- Evitar SQL dinâmico.
- Validar todas as entradas.
- Utilizar ORM sempre que possível.
- Isolar permissões do banco.
- Auditar consultas críticas.
- Automatizar testes de segurança.

---

# Padrão Oficial

Toda interação com bancos de dados da Workstation IA deverá seguir este documento.

Consultas parametrizadas, ORM seguro e validação rigorosa serão obrigatórios para APIs, Cortex, Agentes Inteligentes, Workflows, Jobs, SDKs e servidores MCP.

---

# Referências Oficiais

- OWASP SQL Injection Prevention Cheat Sheet
- OWASP Top 10
- OWASP ASVS
- NIST SP 800-53
- PostgreSQL Security Documentation
- MySQL Security Guide
- Microsoft SQL Server Security Documentation
- ISO/IEC 27001

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de proteção contra SQL Injection definida.
- Uso obrigatório de Prepared Statements e ORM documentado.
- Integração com Cortex, Agentes Inteligentes e servidores MCP homologada.
- Estratégias de auditoria, monitoramento e testes de segurança estabelecidas.