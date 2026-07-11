---
id: CKB-API-0018
title: Rate Limit
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - authentication.md
  - authorization.md
  - endpoints.md
related:
  - websocket.md
  - webhooks.md
  - sdk.md
  - errors.md
last_update: 2026-07
---

# Rate Limit

## Objetivo

Definir oficialmente a política de Rate Limiting da Workstation IA.

Este documento estabelece mecanismos para controlar o volume de requisições realizadas por usuários, aplicações, agentes inteligentes, SDKs e servidores MCP.

O objetivo é proteger a infraestrutura contra abuso, ataques automatizados e consumo excessivo de recursos.

---

# Filosofia

Todo recurso possui limites.

Controlar o consumo garante estabilidade.

Rate Limiting protege a plataforma sem comprometer a experiência do usuário.

---

# Missão

Garantir disponibilidade, previsibilidade e equilíbrio no consumo das APIs.

---

# Arquitetura

```
Cliente

↓

Gateway

↓

Authentication

↓

Rate Limit

↓

Authorization

↓

API

↓

Response
```

---

# Fluxo Oficial

```
Request

↓

Identificação

↓

Política

↓

Contador

↓

Validação

↓

Permitir

ou

Bloquear
```

---

# Identificação

O Rate Limit poderá ser aplicado por.

- usuário
- IP
- API Key
- JWT
- Organização
- Workspace
- SDK
- Agente
- Servidor MCP

---

# Algoritmos Homologados

A plataforma suportará.

```
Token Bucket

Leaky Bucket

Sliding Window

Fixed Window
```

Padrão oficial.

```
Sliding Window
```

---

# Limites Padrão

Usuário autenticado.

```
1000 requisições

↓

60 minutos
```

Usuário anônimo.

```
100 requisições

↓

60 minutos
```

Os valores poderão ser configurados por ambiente.

---

# Limites por Endpoint

Cada endpoint poderá possuir política própria.

Exemplo.

```
Login

↓

10 requisições/minuto

Upload

↓

30 requisições/minuto

Consulta

↓

500 requisições/minuto
```

---

# Rate Limit por Organização

Cada organização poderá possuir limites personalizados.

---

# Rate Limit por Workspace

Cada Workspace poderá possuir cotas independentes.

---

# API Keys

Cada chave poderá definir.

- limite por minuto
- limite por hora
- limite por dia

---

# SDK

Os SDKs deverão respeitar automaticamente os limites retornados pela API.

---

# Cortex

O Cortex deverá identificar limites antes de executar chamadas em lote.

Quando possível.

- agrupar requisições
- utilizar cache
- aplicar backoff

---

# MCP

Servidores MCP deverão respeitar as políticas de Rate Limit definidas pela plataforma.

---

# WebSockets

Limitar.

- conexões simultâneas
- mensagens por segundo
- canais por usuário

---

# Webhooks

Limitar.

- entregas simultâneas
- retries
- eventos por assinatura

---

# Headers HTTP

Todas as respostas deverão informar.

```
X-RateLimit-Limit

X-RateLimit-Remaining

X-RateLimit-Reset
```

Quando o limite for excedido.

```
Retry-After
```

---

# Resposta

HTTP.

```
429 Too Many Requests
```

Exemplo.

```json
{
  "success": false,
  "message": "Limite de requisições excedido.",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED"
  }
}
```

---

# Backoff

Estratégia oficial.

```
Exponential Backoff
```

Aplicável para.

- SDK
- Cortex
- MCP
- Webhooks

---

# Lista de Exclusão

Poderão existir exceções para.

- monitoramento
- serviços internos
- infraestrutura crítica

Sempre mediante autorização.

---

# Segurança

Objetivos.

- impedir ataques DDoS
- reduzir abuso
- limitar força bruta
- proteger autenticação
- preservar disponibilidade

---

# Monitoramento

Registrar.

- usuário
- IP
- endpoint
- quantidade
- bloqueios
- tempo de espera

---

# Auditoria

Registrar.

- política aplicada
- motivo do bloqueio
- duração
- horário
- origem

---

# Integração com Cache

Compatível com.

- Redis
- Memcached
- Banco de Dados

Redis será o padrão recomendado.

---

# Observabilidade

Integrar com.

- Grafana
- Prometheus
- Loki
- OpenTelemetry

---

# Fluxo Geral

```
Cliente

↓

Gateway

↓

Rate Limit

↓

API

↓

Response
```

---

# Checklist

Antes da implantação.

- Limites definidos.

- Redis configurado.

- Headers implementados.

- Resposta 429 documentada.

- Auditoria ativa.

- Monitoramento ativo.

---

# Boas Práticas

- Definir limites por perfil.
- Utilizar Sliding Window.
- Aplicar Backoff.
- Monitorar abusos.
- Informar limites através dos Headers.
- Registrar auditoria.
- Revisar políticas periodicamente.

---

# Padrão Oficial

Toda API da Workstation IA deverá possuir políticas de Rate Limiting.

As regras deverão ser aplicadas de forma consistente para APIs REST, GraphQL, SDKs, WebSockets, Webhooks, Cortex e servidores MCP, garantindo proteção, estabilidade e escalabilidade da plataforma.

---

# Referências Oficiais

- RFC 6585 (HTTP 429 Too Many Requests)
- OWASP API Security Top 10
- NGINX Rate Limiting
- Envoy Proxy Rate Limiting
- Redis Documentation
- OpenTelemetry Specification

---

# Changelog

## 1.0.0

- Documento criado.
- Política oficial de Rate Limiting definida.
- Algoritmos homologados documentados.
- Integração com REST, GraphQL, SDKs, Cortex, MCP, WebSockets e Webhooks estabelecida.
- Estratégias de segurança, auditoria e monitoramento padronizadas.