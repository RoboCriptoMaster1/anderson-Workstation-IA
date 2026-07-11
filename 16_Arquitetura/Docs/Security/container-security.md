---
id: CKB-SEC-0019
title: Container Security
module: Security
version: 1.0.0
status: Core
owner: Workstation IA
project: Workstation IA
author: Anderson dos Santos Damasceno
parent: security/
dependencies:
  - infrastructure-security.md
  - network-security.md
  - encryption.md
related:
  - cloud-security.md
  - devsecops.md
  - vulnerability-management.md
  - logging.md
last_update: 2026-07
---

# Container Security

## Objetivo

Definir oficialmente a arquitetura de segurança para containers da Workstation IA.

Este documento estabelece as políticas obrigatórias para desenvolvimento, construção, distribuição, implantação, execução e monitoramento de containers utilizados pela plataforma.

---

# Filosofia

Containers devem ser descartáveis.

Imagens devem ser imutáveis.

Cada container deve executar apenas uma responsabilidade.

Toda imagem deverá ser considerada não confiável até ser validada.

---

# Missão

Garantir.

- Integridade
- Isolamento
- Disponibilidade
- Rastreabilidade
- Segurança da Supply Chain

---

# Arquitetura

```
Source Code

↓

CI

↓

Build

↓

Scan

↓

Sign

↓

Registry

↓

Deploy

↓

Runtime

↓

Monitoring
```

---

# Escopo

Aplica-se a.

- Docker
- Kubernetes
- OCI Images
- Pods
- Containers do Cortex
- Agentes Inteligentes
- Servidores MCP

---

# Imagens Base

Utilizar somente imagens oficiais ou homologadas.

Preferir.

```
Alpine

Distroless

Ubuntu LTS

Debian Slim
```

Nunca utilizar imagens sem procedência conhecida.

---

# Imagens Imutáveis

Após publicadas.

Nunca deverão ser modificadas.

Toda alteração exigirá nova versão.

---

# Build

Todo build deverá ser reproduzível.

Utilizar.

- Dockerfile versionado
- Build automatizado
- Pipeline CI/CD

---

# Escaneamento

Toda imagem deverá passar por análise de vulnerabilidades.

Ferramentas homologadas.

```
Trivy

Grype

Clair

Docker Scout
```

Bloquear imagens com vulnerabilidades críticas não tratadas.

---

# Assinatura de Imagens

Obrigatória.

Tecnologias recomendadas.

```
Cosign

Sigstore

Notary v2
```

Toda imagem implantada deverá possuir assinatura válida.

---

# Registro de Imagens

Armazenar somente em registries autorizados.

Exemplos.

```
GitHub Container Registry

Azure Container Registry

Amazon ECR

Google Artifact Registry

Harbor
```

---

# Usuário

Containers nunca deverão executar como.

```
root
```

Obrigatório utilizar usuário não privilegiado.

---

# Sistema de Arquivos

Sempre que possível.

```
readOnlyRootFilesystem = true
```

---

# Capacidades

Remover capacidades desnecessárias.

Aplicar.

```
Least Privilege
```

---

# Secrets

Nunca armazenar.

- senhas
- tokens
- certificados
- API Keys

Dentro da imagem.

Utilizar.

```
Vault

Secrets Manager

Kubernetes Secrets
```

---

# Runtime Security

Monitorar containers em execução.

Ferramentas recomendadas.

```
Falco

Sysdig Secure

Aqua

Prisma Cloud
```

---

# Kubernetes

Obrigatório.

- Pod Security Standards
- RBAC
- Network Policies
- Resource Quotas
- LimitRanges
- Admission Controllers

---

# Recursos

Todo container deverá possuir.

```
CPU Limits

Memory Limits

Storage Limits
```

---

# Isolamento

Separar workloads por.

- namespace
- ambiente
- organização
- criticidade

---

# Comunicação

Toda comunicação entre containers deverá utilizar.

- mTLS
- autenticação
- autorização

Quando aplicável.

---

# Supply Chain Security

Seguir práticas.

```
SLSA

SBOM

Assinatura Digital

Verificação de Proveniência
```

---

# SBOM

Toda imagem deverá possuir.

```
Software Bill of Materials
```

Compatível com.

```
SPDX

CycloneDX
```

---

# Logs

Registrar.

- criação
- implantação
- atualização
- remoção
- falhas
- reinicializações

---

# Auditoria

Registrar.

- imagem utilizada
- assinatura
- versão
- usuário responsável
- ambiente
- horário

---

# Monitoramento

Monitorar.

- consumo de CPU
- memória
- disco
- reinícios
- falhas
- containers privilegiados
- alterações em runtime

---

# Cortex

Os componentes do Cortex deverão executar em containers isolados.

Cada serviço possuirá.

- identidade própria
- recursos limitados
- políticas independentes

---

# Agentes Inteligentes

Cada agente executará em ambiente isolado.

Nunca compartilhará filesystem ou credenciais com outros agentes.

---

# MCP

Servidores MCP deverão.

- utilizar imagens assinadas
- executar como usuário não privilegiado
- possuir auditoria
- respeitar políticas de runtime

---

# Segurança

Proibido.

- Containers privilegiados
- Docker Socket exposto
- Execução como root
- Imagens não assinadas
- Secrets embutidos
- Última versão sem versionamento ("latest")

---

# Conformidade

Compatível com.

- CIS Docker Benchmark
- CIS Kubernetes Benchmark
- NIST SP 800-190
- SLSA Framework
- ISO/IEC 27001
- OWASP Container Security

---

# Fluxo Oficial

```
Code

↓

Build

↓

Scan

↓

Sign

↓

Registry

↓

Deploy

↓

Runtime

↓

Audit

↓

Monitoring
```

---

# Checklist

Antes da implantação.

- Imagem escaneada.

- Vulnerabilidades críticas tratadas.

- Assinatura válida.

- Usuário não root.

- Secrets externos.

- Runtime monitorado.

- Recursos limitados.

- Auditoria ativa.

---

# Boas Práticas

- Utilizar imagens mínimas.
- Assinar todas as imagens.
- Escanear continuamente.
- Evitar containers privilegiados.
- Executar como usuário não root.
- Utilizar SBOM.
- Automatizar verificações no CI/CD.

---

# Padrão Oficial

Toda infraestrutura baseada em containers da Workstation IA deverá seguir este documento.

As políticas estabelecidas aplicam-se ao Docker, Kubernetes, Cortex, Agentes Inteligentes, servidores MCP e toda a cadeia de Supply Chain da plataforma, garantindo ambientes seguros, auditáveis e resilientes.

---

# Referências Oficiais

- NIST SP 800-190 (Application Container Security Guide)
- CIS Docker Benchmark
- CIS Kubernetes Benchmark
- Sigstore Documentation
- Cosign Documentation
- SLSA Framework
- SPDX Specification
- CycloneDX
- OWASP Container Security Cheat Sheet
- Kubernetes Security Documentation

---

# Changelog

## 1.0.0

- Documento criado.
- Arquitetura oficial de Container Security definida.
- Políticas para Docker, Kubernetes e OCI Images documentadas.
- Integração com Supply Chain Security, SBOM, Sigstore, Cosign, Cortex, Agentes Inteligentes e servidores MCP homologada.
- Controles de auditoria, monitoramento e runtime security estabelecidos.