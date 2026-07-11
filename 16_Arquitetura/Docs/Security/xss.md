---
id: CKB-SEC-0013
title: Cross-Site Scripting (XSS)
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - secure-headers.md
  - csrf.md
  - cors.md
related:
  - api-security.md
  - file-security.md
  - logging.md
last_update: 2026-07
---

# Cross-Site Scripting (XSS)

## Objetivo

Definir oficialmente a arquitetura de proteção contra ataques de Cross-Site Scripting (XSS) da Workstation IA.

Este documento estabelece políticas para impedir execução de código JavaScript não autorizado, protegendo usuários, aplicações Web, APIs, Cortex, Agentes Inteligentes e interfaces administrativas.

---

# Filosofia

Todo dado recebido deve ser considerado não confiável.

Nenhum conteúdo poderá ser executado sem validação.

A saída deve ser protegida tanto quanto a entrada.

---

# Missão

Garantir que dados fornecidos por usuários nunca possam executar código malicioso dentro da plataforma.

---

# Arquitetura

```
Usuário

↓

Input

↓

Validation

↓

Sanitization

↓

Storage

↓

Output Encoding

↓

Browser
```

---

# Tipos de XSS

A plataforma deverá proteger contra.

```
Stored XSS

Reflected XSS

DOM Based XSS

Mutation XSS
```

---

# Stored XSS

Código malicioso armazenado.

Exemplos.

- comentários
- descrições
- mensagens
- perfis
- documentos
- dashboards

Toda informação persistida deverá ser sanitizada.

---

# Reflected XSS

Código refletido imediatamente na resposta.

Toda entrada deverá ser validada antes da renderização.

---

# DOM XSS

Alterações inseguras realizadas pelo JavaScript.

Nunca utilizar.

```
innerHTML
```

com dados não confiáveis.

Preferir.

```
textContent

createElement()

appendChild()
```

---

# Sanitização

Toda entrada HTML deverá passar por sanitização.

Remover.

- scripts
- eventos
- atributos perigosos
- URLs maliciosas

---

# HTML Permitido

Quando necessário.

Permitir somente.

```
b

strong

i

em

p

ul

ol

li

br

code

pre

blockquote
```

Qualquer outro elemento deverá ser removido ou tratado conforme a política do módulo.

---

# Markdown

Conteúdo Markdown deverá ser convertido utilizando bibliotecas seguras.

Após conversão.

Aplicar sanitização HTML.

---

# Output Encoding

Toda saída deverá utilizar codificação adequada ao contexto.

Contextos.

- HTML
- atributos HTML
- JavaScript
- CSS
- URL
- JSON

Nunca reutilizar a mesma estratégia para todos os contextos.

---

# JavaScript

Nunca construir código utilizando concatenação de strings.

Evitar.

```
eval()

new Function()

setTimeout(string)

setInterval(string)
```

---

# Templates

Utilizar mecanismos de escape automático.

Nunca desabilitar escaping sem justificativa técnica.

---

# Content Security Policy

Obrigatória.

Política mínima.

```
default-src 'self'

object-src 'none'

frame-ancestors 'none'

base-uri 'self'
```

Restringir scripts externos ao mínimo necessário.

---

# Trusted Types

Quando suportado.

Habilitar.

```
Trusted Types
```

para impedir injeção de DOM.

---

# Upload de Arquivos

Arquivos HTML enviados por usuários deverão.

- ser tratados como conteúdo ativo
- passar por validação
- ser isolados quando necessário

---

# APIs

As APIs deverão retornar.

```
Content-Type
```

correto.

Nunca permitir interpretação incorreta de conteúdo.

---

# Banco de Dados

Nunca confiar em dados recuperados do banco.

Todo conteúdo exibido deverá passar por codificação de saída.

---

# Cortex

O Cortex deverá tratar conteúdo gerado por IA como potencialmente não confiável.

Toda saída destinada ao navegador deverá ser sanitizada antes da renderização.

---

# Agentes Inteligentes

Os agentes nunca deverão gerar HTML executável diretamente para a interface.

Toda resposta deverá seguir o pipeline oficial de sanitização.

---

# MCP

Interfaces Web dos servidores MCP seguirão exatamente esta política.

---

# Auditoria

Registrar.

- tentativas bloqueadas
- payloads suspeitos
- origem
- usuário
- endpoint
- horário

---

# Monitoramento

Monitorar.

- padrões XSS
- violações CSP
- eventos bloqueados
- tentativas repetidas
- conteúdo removido

---

# Segurança

Proibido.

- inline scripts desnecessários
- eval()
- innerHTML com dados externos
- document.write()
- javascript: em links
- atributos HTML de eventos não controlados

---

# Fluxo Oficial

```
Input

↓

Validation

↓

Sanitization

↓

Storage

↓

Output Encoding

↓

Browser
```

---

# Checklist

Antes da implantação.

- Sanitização implementada.

- Output Encoding configurado.

- CSP ativa.

- Trusted Types avaliadas.

- HTML permitido documentado.

- Auditoria funcionando.

- Monitoramento ativo.

---

# Boas Práticas

- Validar toda entrada.
- Codificar toda saída.
- Utilizar CSP rigorosa.
- Preferir textContent em vez de innerHTML.
- Sanitizar HTML e Markdown.
- Revisar bibliotecas de terceiros.
- Automatizar testes de segurança.

---

# Padrão Oficial

Toda interface Web da Workstation IA deverá implementar proteção contra XSS conforme este documento.

Os controles definidos aplicam-se ao Frontend, APIs, Cortex, Agentes Inteligentes, dashboards administrativos e interfaces Web dos servidores MCP.

---

# Referências Oficiais

- OWASP Cross Site Scripting Prevention Cheat Sheet
- OWASP DOM Based XSS Prevention Cheat Sheet
- OWASP ASVS
- W3C Trusted Types
- Content Security Policy Level 3
- MDN Web Docs XSS
- NIST SP 800-53
- CIS Controls v8

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de proteção contra XSS definida.
- Stored, Reflected, DOM e Mutation XSS documentados.
- Políticas de sanitização, Output Encoding, CSP e Trusted Types estabelecidas.
- Integração com Cortex, Agentes Inteligentes e servidores MCP homologada.