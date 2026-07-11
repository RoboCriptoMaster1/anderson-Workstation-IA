---
id: CKB-SEC-0021
title: DevSecOps
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - cloud-security.md
  - container-security.md
  - vulnerability-management.md
related:
  - logging.md
  - audit.md
  - compliance.md
  - infrastructure-security.md
last_update: 2026-07
---

# DevSecOps

## Objetivo

Definir oficialmente a arquitetura DevSecOps da Workstation IA.

Este documento estabelece como a segurança será integrada continuamente durante todo o ciclo de desenvolvimento de software, desde o planejamento até a operação em produção.

A segurança deixa de ser uma etapa isolada e passa a fazer parte de todas as fases do desenvolvimento.

---

# Filosofia

Desenvolver rápido.

Implantar com segurança.

Automatizar sempre.

Corrigir cedo.

---

# Missão

Garantir.

- Desenvolvimento Seguro
- Entrega Contínua
- Segurança Contínua
- Automação
- Auditoria
- Conformidade

---

# Arquitetura

```
Planejamento

↓

Desenvolvimento

↓

Commit

↓

CI

↓

Testes

↓

Análise de Segurança

↓

Build

↓

Deploy

↓

Produção

↓

Monitoramento
```

---

# Escopo

Aplica-se a.

- Frontend
- Backend
- APIs
- Banco de Dados
- Containers
- Kubernetes
- Cloud
- Cortex
- Agentes IA
- Servidores MCP

---

# Secure SDLC

Toda aplicação deverá seguir.

```
Requirements

↓

Threat Modeling

↓

Secure Coding

↓

Code Review

↓

Testing

↓

Deployment

↓

Operations

↓

Continuous Improvement
```

---

# Controle de Código

Todo código deverá utilizar.

- Git
- Branch Protection
- Pull Requests
- Revisão obrigatória
- Assinatura de commits (quando aplicável)

---

# Revisão de Código

Obrigatório.

Toda alteração deverá possuir.

- revisão técnica
- revisão de segurança
- aprovação antes do merge

---

# CI/CD

Todo pipeline deverá executar.

- testes unitários
- testes de integração
- testes de segurança
- build automatizado
- validação de políticas

---

# SAST

Static Application Security Testing.

Executar a cada commit.

Ferramentas recomendadas.

```
Semgrep

SonarQube

CodeQL

Snyk Code
```

---

# DAST

Dynamic Application Security Testing.

Executar antes da produção.

Ferramentas.

```
OWASP ZAP

Burp Suite Enterprise
```

---

# SCA

Software Composition Analysis.

Verificar continuamente.

- bibliotecas
- dependências
- CVEs
- licenças

Ferramentas.

```
Dependabot

Renovate

Snyk

Trivy
```

---

# IaC Scanning

Infraestrutura como Código deverá ser analisada.

Ferramentas.

```
Checkov

tfsec

Terrascan
```

---

# Containers

Todo container deverá.

- ser escaneado
- ser assinado
- possuir SBOM
- possuir proveniência

---

# SBOM

Obrigatório.

Formatos.

```
CycloneDX

SPDX
```

---

# Supply Chain Security

Seguir.

```
SLSA

Sigstore

Cosign
```

Toda imagem deverá possuir assinatura válida.

---

# Policy as Code

Políticas automatizadas.

Ferramentas.

```
OPA

Gatekeeper

Kyverno
```

---

# GitOps

Quando aplicável.

Utilizar.

```
ArgoCD

FluxCD
```

Toda alteração deverá ser rastreável.

---

# Segredos

Pipelines nunca deverão armazenar.

- senhas
- tokens
- certificados
- API Keys

Utilizar.

```
Vault

Secrets Manager

KMS
```

---

# Vulnerabilidades

Falhas classificadas como críticas bloquearão automaticamente a implantação.

Classificação.

- Crítica
- Alta
- Média
- Baixa

---

# Ambientes

Separar.

```
Desenvolvimento

↓

Homologação

↓

Produção
```

---

# Rollback

Toda implantação deverá permitir.

- rollback automático
- rollback manual
- auditoria completa

---

# Observabilidade

Integrar.

```
OpenTelemetry

Prometheus

Grafana

Loki
```

---

# Cortex

O Cortex poderá auxiliar.

- revisão de código
- geração de testes
- análise de segurança
- documentação
- detecção de padrões inseguros

Toda sugestão deverá ser validada por revisão humana.

---

# Agentes Inteligentes

Os agentes poderão.

- analisar Pull Requests
- detectar vulnerabilidades
- revisar dependências
- gerar correções propostas

Sem executar alterações diretamente em produção.

---

# MCP

Servidores MCP deverão.

- seguir pipelines oficiais
- validar políticas
- registrar auditoria
- utilizar credenciais temporárias

---

# Auditoria

Registrar.

- commits
- builds
- deploys
- falhas
- aprovações
- rollbacks
- vulnerabilidades

---

# Monitoramento

Monitorar.

- pipelines
- tempo de build
- falhas
- cobertura de testes
- vulnerabilidades
- implantações

---

# Segurança

Obrigatório.

- MFA
- Assinatura de artefatos
- SBOM
- SAST
- DAST
- SCA
- IaC Scanning
- Policy as Code

---

# Conformidade

Compatível com.

- NIST SSDF
- OWASP SAMM
- OWASP ASVS
- SLSA Framework
- ISO/IEC 27001
- ISO/IEC 42001
- CIS Controls

---

# Fluxo Oficial

```
Code

↓

Review

↓

CI

↓

Security Tests

↓

Build

↓

Sign

↓

Deploy

↓

Monitor

↓

Improve
```

---

# Checklist

Antes da implantação.

- Code Review aprovado.

- SAST executado.

- DAST executado.

- SCA executado.

- IaC validada.

- SBOM gerado.

- Artefatos assinados.

- Auditoria ativa.

---

# Boas Práticas

- Automatizar verificações.
- Corrigir vulnerabilidades cedo.
- Assinar artefatos.
- Versionar infraestrutura.
- Monitorar continuamente.
- Revisar dependências regularmente.
- Aplicar Security by Design.

---

# Padrão Oficial

Todo desenvolvimento da Workstation IA deverá seguir este documento.

As práticas de DevSecOps serão obrigatórias para Frontend, Backend, APIs, Banco de Dados, Containers, Cloud, Cortex, Agentes Inteligentes e servidores MCP, garantindo uma cadeia de desenvolvimento segura, auditável e alinhada aos padrões internacionais.

---

# Referências Oficiais

- NIST Secure Software Development Framework (SSDF)
- OWASP SAMM
- OWASP ASVS
- SLSA Framework
- Sigstore Documentation
- Cosign Documentation
- SPDX Specification
- CycloneDX
- ISO/IEC 27001
- ISO/IEC 42001

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de DevSecOps definida.
- Secure SDLC, CI/CD seguro, SAST, DAST, SCA e IaC Scanning documentados.
- Integração com Supply Chain Security, GitOps, Policy as Code, Cortex, Agentes Inteligentes e servidores MCP homologada.
- Controles de auditoria, monitoramento e conformidade estabelecidos.