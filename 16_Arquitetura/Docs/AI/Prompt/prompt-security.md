---
id: CKB-AI-0016
title: Prompt Security
module: AI
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: ai/
dependencies:
  - prompt-engineering.md
  - agent-security.md
  - reasoning.md
related:
  - guardrails.md
  - tool-calling.md
  - mcp.md
  - ../security/security.md
last_update: 2026-07
---

# Prompt Security

## Objetivo

Definir oficialmente a arquitetura de segurança de prompts da Workstation IA.

Este documento estabelece os controles necessários para proteger o Cortex, os Agentes Inteligentes, os modelos de IA e o ecossistema MCP contra ataques direcionados aos prompts.

Prompt Security representa uma camada obrigatória de defesa da plataforma.

---

# Filosofia

Todo prompt é uma superfície de ataque.

Nenhuma entrada será considerada confiável.

Toda informação deverá ser validada antes de alcançar o modelo.

---

# Missão

Garantir.

- Integridade
- Confidencialidade
- Disponibilidade
- Rastreabilidade
- Resiliência
- Governança

---

# Arquitetura

```
Entrada

↓

Sanitização

↓

Validação

↓

Policy Engine

↓

Guardrails

↓

Prompt Builder

↓

Modelo

↓

Validation Engine

↓

Resposta
```

---

# Escopo

Aplica-se a.

- Cortex
- Planner
- Agentes
- MCP
- Tool Calling
- RAG
- Memory Manager
- Todos os Modelos

---

# Modelo de Segurança

A arquitetura seguirá.

```
Zero Trust

+

Least Privilege

+

Defense in Depth
```

---

# Ameaças

Proteção obrigatória contra.

- Prompt Injection
- Indirect Prompt Injection
- Jailbreak
- Prompt Leakage
- Data Exfiltration
- Tool Poisoning
- Agent Hijacking
- Context Poisoning
- Memory Poisoning
- Output Manipulation

---

# Prompt Injection

Antes da execução.

Validar.

- comandos ocultos
- instruções conflitantes
- alterações de identidade
- mudanças de políticas

---

# Indirect Prompt Injection

Documentos recuperados via.

- RAG
- PDFs
- HTML
- Markdown
- Websites
- APIs

Nunca serão considerados confiáveis.

---

# Jailbreak

Detectar tentativas de.

- ignorar políticas
- alterar instruções
- assumir privilégios
- executar ações proibidas

---

# Prompt Leakage

Nunca revelar.

- System Prompts
- Prompts internos
- Cadeias de Prompt
- Políticas
- Credenciais
- Tokens

Mesmo quando solicitado.

---

# Data Exfiltration

Bloquear tentativas de extração de.

- memória privada
- documentos restritos
- segredos
- credenciais
- contexto interno

---

# Context Poisoning

Validar.

- histórico
- memória
- documentos
- contexto recuperado

Antes da montagem do prompt.

---

# Memory Poisoning

Toda memória nova deverá passar por.

- validação
- classificação
- auditoria
- aprovação quando necessário

---

# Tool Poisoning

Ferramentas deverão possuir.

- assinatura
- identidade
- política
- auditoria
- validação de origem

---

# Sanitização

Toda entrada será submetida a.

- limpeza
- normalização
- remoção de caracteres maliciosos
- validação estrutural

---

# Policy Engine

Aplicar.

- políticas corporativas
- LGPD
- Compliance
- Segurança
- IA Responsável

Antes da execução.

---

# Guardrails

Executar.

- validação de entrada
- validação de contexto
- validação de ferramentas
- validação da resposta

---

# Tool Calling

Antes da execução.

Validar.

- permissões
- parâmetros
- identidade
- escopo

---

# MCP

O Gateway MCP deverá.

- validar ferramentas
- bloquear chamadas ilegítimas
- registrar auditoria
- limitar permissões

---

# Cortex

Responsável por.

- validar prompts
- remover conteúdo inseguro
- aplicar políticas
- interromper execuções suspeitas

---

# Agentes

Os agentes deverão.

- utilizar apenas prompts aprovados
- respeitar políticas
- validar entradas
- registrar auditoria

---

# Observabilidade

Monitorar.

- Prompt Injection
- Jailbreak
- tentativas bloqueadas
- prompts rejeitados
- risco
- anomalias

---

# Auditoria

Registrar.

- prompts
- alterações
- bloqueios
- incidentes
- ferramentas utilizadas
- políticas aplicadas

---

# Resposta

Antes da entrega.

Validar.

- vazamento de dados
- políticas
- classificação
- informações sensíveis

---

# Segurança

Obrigatório.

- Zero Trust
- autenticação
- autorização
- auditoria
- criptografia
- sandbox
- guardrails

---

# Conformidade

Compatível com.

- ISO/IEC 42001
- ISO/IEC 23894
- ISO/IEC 27001
- NIST AI RMF
- OWASP LLM Top 10
- Google Secure AI Framework

---

# Fluxo Oficial

```
Entrada

↓

Sanitização

↓

Policy Engine

↓

Guardrails

↓

Modelo

↓

Validação

↓

Resposta
```

---

# Checklist

Antes da implantação.

- Sanitização ativa.

- Guardrails implementados.

- Prompt Injection protegido.

- Jailbreak detectado.

- Tool Calling validado.

- Auditoria funcionando.

- Observabilidade ativa.

- Políticas aplicadas.

---

# Boas Práticas

- Nunca confiar na entrada do usuário.
- Separar instruções do sistema e do usuário.
- Validar documentos recuperados pelo RAG.
- Minimizar exposição de contexto.
- Revisar políticas regularmente.
- Auditar tentativas de ataque.
- Atualizar continuamente os mecanismos de proteção.

---

# Padrão Oficial

Todo prompt utilizado pela Workstation IA deverá seguir os controles definidos neste documento.

A segurança de prompts será obrigatória para Cortex, Agentes Inteligentes, RAG, Tool Calling, MCP e todos os modelos suportados pela plataforma, garantindo proteção contra ataques modernos direcionados a sistemas de IA.

---

# Referências Oficiais

- OWASP LLM Top 10
- NIST AI Risk Management Framework
- Google Secure AI Framework (SAIF)
- ISO/IEC 42001
- ISO/IEC 23894
- Microsoft AI Security Guidance
- Anthropic Responsible AI Research
- OpenAI Security Best Practices

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de Prompt Security definida.
- Proteções contra Prompt Injection, Jailbreak, Prompt Leakage, Data Exfiltration, Context Poisoning e Tool Poisoning documentadas.
- Integração com Cortex, MCP, Guardrails e módulo Security estabelecida.
- Controles de auditoria, observabilidade e governança implementados.