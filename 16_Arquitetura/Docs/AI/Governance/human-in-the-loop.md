---
id: CKB-AI-0035
title: Human-in-the-Loop (HITL)
module: AI
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: ai/
dependencies:
  - responsible-ai.md
  - ai-risk-management.md
  - ai-compliance.md
related:
  - output-validation.md
  - hallucination.md
  - conversation-management.md
  - ai-governance.md
last_update: 2026-07
---

# Human-in-the-Loop (HITL)

## Objetivo

Definir oficialmente a arquitetura de Human-in-the-Loop (HITL) da Workstation IA.

Este documento estabelece quando a participação humana é obrigatória, opcional ou dispensável durante a execução de agentes inteligentes, modelos de IA e workflows automatizados.

O objetivo é garantir que decisões críticas permaneçam sob supervisão humana adequada.

---

# Filosofia

A Inteligência Artificial auxilia.

A responsabilidade permanece humana.

Quanto maior o risco, maior deverá ser a supervisão.

---

# Missão

Garantir.

- Segurança
- Responsabilidade
- Transparência
- Confiabilidade
- Governança
- Controle

---

# Arquitetura

```
Solicitação

↓

Reasoning Engine

↓

Risk Assessment

↓

Decision Engine

↓

Human Review

↓

Approval Engine

↓

Execution

↓

Audit
```

---

# Escopo

Aplica-se a.

- Cortex
- Agentes Inteligentes
- Modelos
- Workflows
- MCP
- Tool Calling
- Automações
- Processos Corporativos

---

# Princípios

Aplicar.

- Supervisão Humana
- Accountability
- Aprovação Formal
- Rastreabilidade
- Transparência

---

# Classificação

As decisões poderão ser classificadas.

```
Automática

Assistida

Supervisionada

Obrigatoriamente Humana
```

---

# Critérios

A necessidade de revisão humana poderá considerar.

- risco
- impacto financeiro
- impacto jurídico
- impacto na saúde
- impacto operacional
- privacidade
- conformidade
- confiança do modelo

---

# Casos Obrigatórios

Exemplos.

- decisões médicas
- decisões jurídicas
- movimentações financeiras relevantes
- exclusão definitiva de dados
- alterações críticas em produção
- aprovações regulatórias

---

# Casos Assistidos

Exemplos.

- criação de documentos
- geração de relatórios
- classificação de informações
- análises técnicas

---

# Casos Automáticos

Permitidos quando.

- risco baixo
- políticas aprovadas
- confiança elevada
- auditoria disponível

---

# Human Review

O revisor poderá.

- aprovar
- reprovar
- solicitar revisão
- solicitar evidências
- encaminhar para especialista

---

# Approval Engine

Registrar.

- responsável
- decisão
- justificativa
- horário
- evidências
- assinatura

---

# Escalonamento

Fluxo.

```
IA

↓

Supervisor

↓

Especialista

↓

Gestor

↓

Comitê
```

---

# Feedback

Toda revisão poderá alimentar.

- treinamento
- avaliação
- melhoria dos agentes
- melhoria dos modelos

---

# Cortex

Responsável por.

- identificar necessidade de revisão
- bloquear execução quando necessário
- registrar aprovações
- manter histórico

---

# Indicadores

Monitorar.

- revisões humanas
- aprovações
- reprovações
- tempo médio
- retrabalho
- divergências

---

# Observabilidade

Registrar.

- solicitações
- decisões
- revisores
- justificativas
- exceções

---

# Auditoria

Registrar.

- aprovações
- recusas
- responsáveis
- comentários
- histórico
- alterações

---

# Segurança

Obrigatório.

- autenticação
- autorização
- assinatura digital
- trilha de auditoria

---

# Escalabilidade

Permitir.

- múltiplos revisores
- múltiplos níveis
- múltiplas organizações
- múltiplos fluxos

---

# Conformidade

Compatível com.

- ISO/IEC 42001
- ISO/IEC 23894
- ISO/IEC 27001
- NIST AI RMF
- AI Act
- LGPD
- GDPR

---

# Fluxo Oficial

```
Solicitação

↓

Risk Assessment

↓

Human Review

↓

Approval

↓

Execution

↓

Auditoria
```

---

# Checklist

Antes da implantação.

- Critérios de revisão definidos.

- Approval Engine ativo.

- Auditoria funcionando.

- Escalonamento configurado.

- Indicadores publicados.

- Segurança validada.

- Responsáveis definidos.

- Políticas aprovadas.

---

# Boas Práticas

- Automatizar apenas decisões de baixo risco.
- Manter supervisão humana em decisões críticas.
- Registrar todas as aprovações.
- Documentar justificativas.
- Revisar critérios periodicamente.
- Medir qualidade das revisões.
- Utilizar feedback para melhoria contínua.

---

# Padrão Oficial

Toda decisão classificada como crítica pela Workstation IA deverá passar obrigatoriamente pelo processo de Human-in-the-Loop definido neste documento.

A plataforma deverá assegurar que decisões de alto impacto sejam supervisionadas, justificadas, auditáveis e alinhadas às políticas organizacionais e regulatórias.

---

# Referências Oficiais

- ISO/IEC 42001
- ISO/IEC 23894
- NIST AI Risk Management Framework
- AI Act (União Europeia)
- OECD AI Principles
- UNESCO Recommendation on the Ethics of AI
- Microsoft Responsible AI Standard

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de Human-in-the-Loop definida.
- Critérios de revisão humana, aprovação, escalonamento e feedback documentados.
- Integração com Cortex, Responsible AI, AI Risk Management e AI Compliance estabelecida.
- Controles de auditoria, observabilidade, segurança e governança implementados.