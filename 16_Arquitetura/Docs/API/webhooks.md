---
id: CKB-API-0011
title: Webhooks
module: API
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: api/
dependencies:
  - sdk.md
  - openapi.md
  - authentication.md
related:
  - websocket.md
  - rate-limit.md
  - documentation.md
last_update: 2026-07
---

# Webhooks

## Objetivo

Definir oficialmente a arquitetura de Webhooks da Workstation IA.

Os Webhooks representam o mecanismo oficial de comunicação assíncrona da plataforma com aplicações externas, parceiros, integrações corporativas, agentes inteligentes e servidores MCP.

---

# Filosofia

Nem toda informação precisa ser consultada.

Eventos importantes deverão ser enviados automaticamente.

A plataforma informa.

O consumidor reage.

---

# Missão

Disponibilizar um mecanismo confiável, seguro e auditável para entrega de eventos em tempo real.

---

# Arquitetura

```
Evento

↓

Event Bus

↓

Webhook Queue

↓

Dispatcher

↓

HTTPS

↓

Cliente

↓

ACK

↓

Auditoria
```

---

# Estrutura

```
webhooks/

events/

deliveries/

subscriptions/

security/

logs/

retries/
```

---

# Fluxo Oficial

```
Evento

↓

Fila

↓

Dispatcher

↓

Assinatura

↓

Entrega

↓

Validação

↓

ACK

↓

Auditoria
```

---

# Eventos

Todos os Webhooks serão baseados em eventos.

Exemplos.

```
user.created

user.updated

user.deleted

project.created

project.updated

project.archived

task.created

task.updated

task.completed

report.generated

file.uploaded

file.deleted

notification.sent

dashboard.updated

agent.executed

cortex.learning

mcp.connected

mcp.disconnected
```

---

# Assinaturas

Cada consumidor deverá registrar.

- URL
- eventos
- autenticação
- versão
- status
- owner

---

# Endpoint

Formato.

```
HTTPS
```

Obrigatório.

Nunca utilizar HTTP simples.

---

# Payload

Formato oficial.

```json
{
  "event": "",
  "version": "1.0",
  "timestamp": "",
  "request_id": "",
  "data": {}
}
```

---

# Timestamp

Formato.

```
ISO 8601 UTC
```

---

# Identificador

Todo evento deverá possuir.

```
event_id
```

Único.

---

# Versionamento

Cada evento possuirá.

```
version
```

Mudanças incompatíveis gerarão nova versão.

---

# Assinatura

Método oficial.

```
HMAC SHA-256
```

Header.

```
X-Workstation-Signature
```

---

# Headers

Obrigatórios.

```
Content-Type

X-Request-ID

X-Event-ID

X-Event-Type

X-Timestamp

X-Workstation-Signature
```

---

# Segurança

Obrigatório.

- HTTPS
- HMAC
- Secret por assinatura
- Replay Protection
- Timestamp Validation

---

# Replay Attack

Toda entrega deverá validar.

- assinatura
- timestamp
- event_id

Eventos repetidos deverão ser descartados.

---

# ACK

Sucesso.

```
HTTP 200

HTTP 202

HTTP 204
```

---

# Retry

Caso a entrega falhe.

Estratégia.

```
1 minuto

↓

5 minutos

↓

15 minutos

↓

30 minutos

↓

1 hora

↓

6 horas

↓

24 horas
```

Após o limite.

Evento movido para Dead Letter Queue.

---

# Dead Letter Queue

Eventos não entregues serão armazenados para investigação.

Nunca descartar silenciosamente.

---

# Timeout

Padrão.

```
10 segundos
```

Configurável.

---

# Idempotência

Consumidores deverão tratar.

```
event_id
```

como identificador único.

O mesmo evento poderá ser reenviado.

---

# Filtros

Cada assinatura poderá selecionar eventos específicos.

Exemplo.

```
projects.*

tasks.completed

dashboard.updated
```

---

# Observabilidade

Registrar.

- tempo de entrega
- tentativas
- status
- destino
- latência
- resposta

---

# Auditoria

Registrar.

- evento
- assinatura
- destino
- horário
- sucesso
- falha
- retries

---

# Integração com Cortex

Eventos poderão ser enviados pelo Cortex.

Exemplos.

```
knowledge.updated

memory.changed

workflow.finished

agent.completed
```

---

# Integração com MCP

Servidores MCP poderão.

- publicar eventos
- consumir eventos
- reagir automaticamente

---

# Integração com Filas

Compatível com.

```
RabbitMQ

Redis Streams

Apache Kafka

AWS SQS
```

---

# Monitoramento

Monitorar.

- taxa de sucesso
- tempo médio
- falhas
- retries
- DLQ
- disponibilidade

---

# Cancelamento

Uma assinatura poderá ser.

- pausada
- reativada
- removida

Sem perda do histórico.

---

# Checklist

Antes da publicação.

- HTTPS ativo.

- Assinatura HMAC.

- Retry configurado.

- DLQ configurada.

- Auditoria ativa.

- Timeout definido.

- Eventos documentados.

---

# Boas Práticas

- Utilizar HTTPS.
- Validar assinatura.
- Implementar idempotência.
- Responder rapidamente.
- Processar assincronamente.
- Registrar auditoria.
- Nunca perder eventos.

---

# Padrão Oficial

Toda comunicação assíncrona da Workstation IA deverá utilizar Webhooks conforme este documento.

Os Webhooks serão o mecanismo oficial para notificação de eventos entre a plataforma, Cortex, agentes inteligentes, servidores MCP e sistemas externos.

---

# Referências Oficiais

- Webhooks RFC
- OpenAPI Webhooks
- HMAC RFC 2104
- OWASP Webhook Security Guidelines
- Stripe Webhook Best Practices
- GitHub Webhooks Documentation
- CloudEvents Specification

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de Webhooks definida.
- Modelo de eventos padronizado.
- Estratégia de retries, DLQ e auditoria documentada.
- Integração com Cortex, MCP e sistemas externos homologada.