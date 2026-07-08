# Workstation-IA

Ambiente de trabalho pessoal para projetos de **Inteligência Artificial e automação**. Este repositório organiza projetos, agentes, integrações, scripts e documentos em uma estrutura de pastas numeradas por categoria, facilitando encontrar e reaproveitar o que já foi feito.

## Estrutura de pastas

O trabalho é arquivado por categoria. Ao criar ou mover arquivos, respeite esta convenção:

| Pasta | Finalidade |
|---|---|
| `01_Projetos` | Projetos completos (ponta a ponta); local principal das entregas reais |
| `02_Agentes` | Agentes de IA e suas definições |
| `03_APIs` | Integrações e clientes de API |
| `04_Banco_Dados` | Bancos de dados, schemas e consultas |
| `05_Excel` | Planilhas e trabalhos baseados em Excel |
| `06_Python` | Scripts e projetos em Python |
| `07_NodesJS` | Scripts e projetos em Node.js |
| `08_Markdown` | Documentos em Markdown |
| `09_Documentos` | Documentos gerais |
| `10_Templates` | Modelos reutilizáveis |
| `11_Prompts` | Prompts salvos |
| `12_Automacoes` | Scripts e fluxos de automação |
| `13_MCP` | Servidores e configurações de MCP (Model Context Protocol) |
| `14_Modelos` | Modelos (modelos de IA ou modelos de documentos) |
| `99_Backup` | Backups |

> As pastas vazias são mantidas no Git através de arquivos `.gitkeep`.

## Convenções

- **Idioma:** nomes de pastas e arquivos em português (pt-BR). Mantenha o mesmo idioma ao nomear coisas.
- **Plataforma:** Windows 11, terminal PowerShell.
- **Segredos:** nunca versione credenciais. O arquivo `.gitignore` já bloqueia chaves de API, arquivos `.env` e afins.

## Fluxo de trabalho com Git

Ciclo básico para salvar e enviar alterações:

```bash
git add .
git commit -m "sua mensagem"
git push
```

## Repositório

- **Remoto:** https://github.com/RoboCriptoMaster1/anderson-Workstation-IA
- **Branch principal:** `main`
