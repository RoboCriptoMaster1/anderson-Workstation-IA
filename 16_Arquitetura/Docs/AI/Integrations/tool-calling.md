---
id: CKB-AI-0017
title: Tool Calling
module: AI
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: ai/
dependencies:
  - cortex.md
  - planner.md
  - reasoning.md
  - prompt-security.md
related:
  - mcp.md
  - guardrails.md
  - agent-security.md
  - model-routing.md
last_update: 2026-07
---

# Tool Calling

## Objetivo

Definir oficialmente a arquitetura de Tool Calling da Workstation IA.

Este documento estabelece como o Cortex e os Agentes Inteligentes descobrem, selecionam, autorizam, executam e monitoram ferramentas durante a resolução de tarefas.

Toda interação com recursos externos deverá ocorrer através da arquitetura oficial de Tool Calling.

---

# Filosofia

Modelos raciocinam.

Ferramentas executam.

O Cortex decide quando uma ferramenta será utilizada.

Nenhum modelo deverá executar ações diretamente.

---

# Missão

Garantir.

- Execução Segura
- Padronização
- Auditoria
- Escalabilidade
- Governança
- Reutilização

---

# Arquitetura

```
Usuário

↓

Cortex

↓

Planner

↓

Reasoning Engine

↓

Tool Manager

↓

MCP Gateway

↓

Ferramenta

↓

Resultado

↓

Validation

↓

Resposta
```

---

# Escopo

Aplica-se a.

- Cortex
- Agentes
- MCP
- APIs
- Banco de Dados
- Arquivos
- Serviços Cloud
- Scripts
- Automações

---

# Definição

Uma ferramenta representa qualquer recurso externo capaz de executar ações ou recuperar informações para o Cortex.

Exemplos.

- API REST
- Banco de Dados
- Planilhas
- Sistema ERP
- Sistema CRM
- Power BI
- Docker
- Git
- Python
- PowerShell
- Web Search

---

# Registro

Toda ferramenta deverá possuir.

```
tool_id

name

description

version

owner

provider

permissions

status

risk_level
```

---

# Classificação

Ferramentas poderão ser.

```
Read Only

Write

Execute

Administrative

Critical
```

---

# Descoberta

O Tool Manager deverá descobrir ferramentas utilizando.

- MCP
- Catálogo Oficial
- Registro Corporativo
- Plugins Homologados

---

# Seleção

O Cortex deverá considerar.

- contexto
- permissões
- custo
- latência
- disponibilidade
- risco
- especialização

---

# Autorização

Antes da execução.

Validar.

- identidade
- permissões
- organização
- workspace
- política
- classificação

---

# Fluxo Oficial

```
Objetivo

↓

Planner

↓

Reasoning

↓

Selecionar Ferramenta

↓

Autorização

↓

Execução

↓

Validação

↓

Resposta
```

---

# Execução

Cada chamada deverá registrar.

```
execution_id

tool_id

agent_id

model

user

started_at

finished_at

status
```

---

# Entrada

Toda entrada deverá ser validada.

Executar.

- sanitização
- validação de tipos
- validação de tamanho
- validação estrutural

---

# Saída

Toda saída deverá passar por.

- validação
- classificação
- mascaramento
- auditoria

Antes de retornar ao modelo.

---

# Timeout

Toda ferramenta deverá possuir.

- timeout
- retry
- fallback

Configuráveis.

---

# Retry

Estratégias.

```
Linear

Exponencial

Adaptativa
```

---

# Fallback

Quando uma ferramenta falhar.

O Cortex poderá.

- utilizar outra ferramenta
- utilizar outro agente
- utilizar outro modelo
- solicitar intervenção humana

---

# Paralelismo

Ferramentas poderão executar.

- paralelo
- sequencial
- dependente

Conforme plano do Planner.

---

# Idempotência

Ferramentas críticas deverão suportar.

- execução segura
- prevenção de duplicidade
- rollback quando aplicável

---

# Segurança

Obrigatório.

- autenticação
- autorização
- criptografia
- auditoria
- sandbox
- Zero Trust

---

# Guardrails

Antes da execução.

Validar.

- parâmetros
- risco
- políticas
- permissões

---

# MCP

Toda ferramenta oficial deverá ser registrada através do Gateway MCP.

O MCP será responsável por.

- descoberta
- autenticação
- autorização
- execução
- auditoria

---

# Cortex

Responsável por.

- selecionar ferramentas
- autorizar chamadas
- validar resultados
- monitorar execução

---

# Agentes

Os agentes poderão.

- solicitar ferramentas
- interpretar resultados

Nunca executar ferramentas diretamente sem autorização do Cortex.

---

# Observabilidade

Monitorar.

- tempo de execução
- erros
- disponibilidade
- custo
- throughput
- retries
- falhas

---

# Auditoria

Registrar.

- ferramenta utilizada
- agente
- parâmetros
- resultado
- tempo
- usuário
- políticas aplicadas

---

# Escalabilidade

Permitir.

- milhares de ferramentas
- múltiplos provedores
- múltiplos ambientes
- execução distribuída

---

# Conformidade

Compatível com.

- Model Context Protocol (MCP)
- ISO/IEC 42001
- ISO/IEC 23894
- ISO/IEC 27001
- NIST AI RMF
- OWASP LLM Top 10

---

# Fluxo Completo

```
Usuário

↓

Cortex

↓

Planner

↓

Reasoning

↓

Tool Manager

↓

MCP

↓

Ferramenta

↓

Validation

↓

Resposta
```

---

# Checklist

Antes da implantação.

- Ferramenta registrada.

- Permissões configuradas.

- Timeout definido.

- Retry configurado.

- Auditoria ativa.

- Observabilidade funcionando.

- Guardrails habilitados.

- Segurança validada.

---

# Boas Práticas

- Registrar todas as ferramentas.
- Aplicar menor privilégio.
- Validar entradas e saídas.
- Monitorar disponibilidade continuamente.
- Utilizar fallback para operações críticas.
- Automatizar auditorias.
- Revisar permissões periodicamente.

---

# Padrão Oficial

Toda execução de ações externas da Workstation IA deverá utilizar a arquitetura oficial de Tool Calling.

Nenhum modelo ou agente poderá acessar diretamente APIs, bancos de dados ou serviços externos sem passar pelo Cortex, pelo Tool Manager e pelo Gateway MCP, garantindo segurança, rastreabilidade e governança.

---

# Referências Oficiais

- Model Context Protocol (MCP)
- OpenAI Function Calling
- Anthropic Tool Use
- Google Gemini Function Calling
- LangChain Tools
- LangGraph
- ISO/IEC 42001
- NIST AI RMF
- OWASP LLM Top 10

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de Tool Calling definida.
- Registro, descoberta, autorização, execução e monitoramento de ferramentas documentados.
- Integração com Cortex, Planner, Agentes e Gateway MCP estabelecida.
- Controles de segurança, auditoria, observabilidade e governança implementados.