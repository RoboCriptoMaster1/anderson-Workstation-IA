---
id: CKB-API-0012
title: WebSocket
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - webhooks.md
  - authentication.md
  - authorization.md
related:
  - graphql.md
  - sdk.md
  - rate-limit.md
last_update: 2026-07
---

# WebSocket

## Objetivo

Definir oficialmente a arquitetura de comunicação em tempo real da Workstation IA.

Este documento estabelece como usuários, agentes inteligentes, Cortex e servidores MCP compartilharão informações em tempo real.

Toda comunicação persistente deverá seguir este padrão.

---

# Filosofia

Nem toda comunicação deve esperar uma nova requisição.

Quando a informação muda.

Ela deve chegar imediatamente.

Tempo real representa sincronização contínua.

---

# Missão

Disponibilizar uma infraestrutura confiável para comunicação bidirecional entre clientes e a plataforma.

---

# Arquitetura

```
Cliente

↓

HTTPS

↓

Upgrade

↓

WebSocket

↓

Gateway

↓

Event Bus

↓

Cortex

↓

Agentes

↓

Database

↓

Resposta
```

---

# Estrutura

```
websocket/

gateway/

channels/

events/

presence/

rooms/

security/

monitoring/
```

---

# Fluxo Oficial

```
Cliente

↓

Handshake

↓

Authentication

↓

Authorization

↓

Connection

↓

Subscription

↓

Events

↓

Disconnect
```

---

# Handshake

Toda conexão deverá iniciar via HTTPS.

Após validação.

```
HTTP

↓

Upgrade

↓

WebSocket
```

---

# Autenticação

Obrigatória.

Métodos.

```
JWT

OAuth

Service Token

MCP Identity
```

Nenhuma conexão anônima será aceita.

---

# Autorização

Após autenticação verificar.

- permissões
- workspace
- organização
- papéis
- canais permitidos

---

# Identificação

Cada conexão possuirá.

```
connection_id

user_id

workspace_id

request_id
```

Todos únicos.

---

# Canais

Exemplos.

```
notifications

dashboard

projects

tasks

analytics

agents

cortex

system

chat
```

---

# Rooms

Utilizadas para agrupamento lógico.

Exemplos.

```
workspace

team

project

department

organization
```

---

# Presença

Cada conexão manterá.

```
online

away

busy

offline
```

---

# Eventos

Formato.

```json
{
  "event": "",
  "channel": "",
  "timestamp": "",
  "data": {}
}
```

---

# Eventos Oficiais

```
connected

disconnected

authenticated

notification.created

dashboard.updated

task.updated

project.updated

report.generated

agent.started

agent.finished

cortex.updated

system.alert
```

---

# Broadcast

Permitido.

Tipos.

```
Global

Workspace

Room

User

Agent
```

---

# Mensagens Privadas

Formato.

```
Servidor

↓

Usuário

ou

Agente
```

---

# Heartbeat

Obrigatório.

```
PING

↓

PONG
```

Objetivo.

- detectar conexões perdidas
- liberar recursos
- manter sessão ativa

---

# Reconexão

Estratégia.

```
Exponential Backoff
```

Tentativas.

```
1

2

4

8

16 segundos
```

---

# Escalabilidade

Compatível com.

```
Redis Pub/Sub

Redis Streams

RabbitMQ

Apache Kafka
```

---

# Balanceamento

Suporte para.

```
Load Balancer

Sticky Sessions

Redis Adapter
```

---

# Segurança

Obrigatório.

- TLS
- JWT
- Rate Limit
- Timeout
- Auditoria
- Validação de eventos

---

# Timeout

Conexões inativas.

```
30 minutos
```

Configurável.

---

# Limites

Cada usuário poderá possuir.

- número máximo de conexões
- número máximo de canais
- limite de mensagens

---

# Rate Limit

Aplicado em.

- conexões
- mensagens
- subscriptions

---

# Integração com Cortex

O Cortex poderá publicar.

```
knowledge.updated

memory.updated

workflow.finished

reasoning.completed

agent.created
```

---

# Integração com Agentes

Cada agente poderá.

- publicar eventos
- consumir eventos
- responder automaticamente

---

# Integração com MCP

Servidores MCP poderão.

- abrir canais
- consumir eventos
- publicar resultados

---

# Monitoramento

Registrar.

- conexões ativas
- latência
- mensagens
- falhas
- reconnects
- throughput

---

# Auditoria

Registrar.

- usuário
- conexão
- canal
- evento
- horário
- duração

---

# Logs

Registrar.

```
Connection

Authentication

Subscriptions

Broadcasts

Errors

Disconnect
```

---

# Observabilidade

Integrar com.

- Prometheus
- Grafana
- Loki
- OpenTelemetry

---

# Fluxo Geral

```
Cliente

↓

WebSocket

↓

Gateway

↓

Event Bus

↓

Cortex

↓

Agentes

↓

Broadcast

↓

Clientes
```

---

# Checklist

Antes da publicação.

- JWT ativo.

- TLS configurado.

- Heartbeat implementado.

- Reconexão validada.

- Auditoria ativa.

- Monitoramento ativo.

- Escalabilidade configurada.

---

# Boas Práticas

- Utilizar canais.
- Evitar broadcasts desnecessários.
- Implementar Heartbeat.
- Registrar auditoria.
- Validar autenticação continuamente.
- Utilizar filas para eventos.
- Fechar conexões inativas.

---

# Padrão Oficial

Toda comunicação em tempo real da Workstation IA deverá utilizar WebSockets conforme este documento.

Os WebSockets serão utilizados para sincronização entre usuários, dashboards, Cortex, agentes inteligentes, servidores MCP e módulos internos da plataforma.

---

# Referências Oficiais

- RFC 6455 WebSocket Protocol
- MDN WebSocket API
- Socket.IO Documentation
- OpenTelemetry Specification
- Redis Pub/Sub Documentation
- Apache Kafka Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de WebSockets definida.
- Modelo de canais, eventos e presença documentado.
- Integração com Cortex, Agentes e MCP homologada.
- Estratégias de segurança, escalabilidade e monitoramento estabelecidas.