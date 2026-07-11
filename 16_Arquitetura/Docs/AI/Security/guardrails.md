---
id: CKB-AI-0036
title: Guardrails
module: AI
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: ai/
dependencies:
  - prompt-security.md
  - ai-risk-management.md
  - responsible-ai.md
related:
  - output-validation.md
  - human-in-the-loop.md
  - hallucination.md
  - ai-compliance.md
last_update: 2026-07
---

# Guardrails

## Objetivo

Definir oficialmente a arquitetura de Guardrails da Workstation IA.

Os Guardrails são responsáveis por impedir comportamentos inseguros, inadequados ou não autorizados durante toda a execução da Inteligência Artificial.

Eles atuam antes, durante e após a inferência.

---

# Filosofia

Toda IA precisa de limites.

Liberdade operacional não significa ausência de controle.

Proteção deve existir em todas as etapas da execução.

---

# Missão

Garantir.

- Segurança
- Confiabilidade
- Integridade
- Conformidade
- Controle
- Resiliência

---

# Arquitetura

```
Entrada

↓

Input Guardrails

↓

Policy Engine

↓

Reasoning

↓

Tool Calling

↓

Output Guardrails

↓

Resposta
```

---

# Escopo

Aplica-se a.

- Cortex
- Agentes Inteligentes
- Modelos
- Prompt Engineering
- MCP
- Tool Calling
- APIs
- Workflows

---

# Camadas

## Input Guardrails

Validar.

- prompts
- arquivos
- comandos
- parâmetros
- contexto

---

## Runtime Guardrails

Monitorar.

- decisões
- ferramentas
- memória
- workflows
- políticas

---

## Output Guardrails

Validar.

- respostas
- código
- documentos
- ações
- resultados

---

# Ameaças

Mitigar.

- Prompt Injection
- Jailbreak
- Data Leakage
- Tool Abuse
- Context Poisoning
- Model Manipulation
- Prompt Extraction
- Privilege Escalation

---

# Input Validation

Executar.

- sanitização
- validação de formato
- detecção de conteúdo malicioso
- classificação de risco

---

# Tool Validation

Antes da execução.

Verificar.

- permissões
- parâmetros
- escopo
- política
- organização

---

# Output Validation

Verificar.

- conformidade
- segurança
- privacidade
- consistência
- classificação
- evidências

---

# Policy Engine

Aplicar.

- políticas
- compliance
- privacidade
- classificação
- limites operacionais

---

# Runtime Protection

Bloquear.

- comandos proibidos
- acesso não autorizado
- uso indevido de ferramentas
- execução insegura

---

# RAG

Validar.

- origem
- classificação
- autorização
- relevância

---

# Memória

Permitir apenas.

- leitura autorizada
- gravação autorizada
- compartilhamento autorizado

---

# Cortex

Responsável por.

- aplicar Guardrails
- bloquear violações
- registrar incidentes
- acionar Human-in-the-Loop

---

# Classificação

As violações poderão ser classificadas.

```
Informativa

Baixa

Média

Alta

Crítica
```

---

# Ações

Quando detectar risco.

Executar.

- bloquear
- solicitar confirmação
- escalar
- registrar
- notificar

---

# Observabilidade

Monitorar.

- violações
- bloqueios
- tentativas
- exceções
- incidentes

---

# Auditoria

Registrar.

- regras aplicadas
- bloqueios
- aprovações
- exceções
- revisões

---

# Segurança

Integrar com.

- Zero Trust
- AI Privacy
- AI Compliance
- AI Risk Management
- Responsible AI

---

# Escalabilidade

Permitir.

- múltiplos modelos
- múltiplos agentes
- múltiplas organizações
- múltiplos ambientes

---

# Conformidade

Compatível com.

- ISO/IEC 42001
- ISO/IEC 23894
- ISO/IEC 27001
- NIST AI RMF
- OWASP LLM Top 10
- AI Act
- LGPD
- GDPR

---

# Fluxo Oficial

```
Entrada

↓

Input Guardrails

↓

Inferência

↓

Runtime Guardrails

↓

Output Guardrails

↓

Resposta
```

---

# Checklist

Antes da implantação.

- Input Guardrails ativos.

- Runtime Guardrails funcionando.

- Output Guardrails implementados.

- Policy Engine integrado.

- Auditoria habilitada.

- Observabilidade ativa.

- Segurança validada.

- Testes aprovados.

---

# Boas Práticas

- Validar toda entrada.
- Nunca executar comandos sem autorização.
- Aplicar menor privilégio.
- Bloquear ações críticas automaticamente.
- Registrar todas as violações.
- Revisar políticas periodicamente.
- Integrar Guardrails ao ciclo completo da IA.

---

# Padrão Oficial

Toda execução da Workstation IA deverá passar pelos Guardrails definidos neste documento.

Nenhum agente, modelo ou ferramenta poderá executar ações fora das políticas estabelecidas, garantindo proteção contínua durante todo o ciclo de vida da Inteligência Artificial.

---

# Referências Oficiais

- OWASP LLM Top 10
- NIST AI Risk Management Framework
- ISO/IEC 42001
- ISO/IEC 23894
- ISO/IEC 27001
- AI Act (União Europeia)
- OpenAI Safety Best Practices
- Anthropic Constitutional AI

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de Guardrails definida.
- Input, Runtime e Output Guardrails documentados.
- Integração com Cortex, AI Risk Management, Responsible AI e Human-in-the-Loop estabelecida.
- Controles de segurança, auditoria, observabilidade e conformidade implementados.