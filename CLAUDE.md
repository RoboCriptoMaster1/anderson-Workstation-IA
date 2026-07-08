# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`Workstation-IA` is a personal AI/automation workspace, not a single application. As of this writing it is an **empty scaffold**: 15 numbered top-level folders (Portuguese names) plus `99_Backup`, all currently empty. There is no source code, README, build system, dependency manifest, or tests yet. It is **not** a git repository.

Because there is no code, there are no build/lint/test commands to document. As real projects land in these folders, add project-specific commands and architecture notes here (or in a nested `CLAUDE.md` inside the relevant folder).

## Folder taxonomy

Work is filed by category. When creating or placing files, respect this convention:

| Folder | Purpose |
|---|---|
| `01_Projetos` | Projects (end-to-end work; the primary home for real deliverables) |
| `02_Agentes` | AI agents / agent definitions |
| `03_APIs` | API integrations and clients |
| `04_Banco_Dados` | Databases, schemas, queries |
| `05_Excel` | Spreadsheets and Excel-based work |
| `06_Python` | Python scripts and projects |
| `07_NodesJS` | Node.js scripts and projects (note the folder is literally named `07_NodesJS`) |
| `08_Markdown` | Markdown documents |
| `09_Documentos` | General documents |
| `10_Templates` | Reusable templates |
| `11_Prompts` | Saved prompts |
| `12_Automacoes` | Automation scripts / workflows |
| `13_MCP` | Model Context Protocol servers and configs |
| `14_Modelos` | Models (AI models or document "modelos") |
| `99_Backup` | Backups |

## Conventions

- **Language:** Folder and file names are in Portuguese (pt-BR). Match the existing language when naming things.
- **Platform:** Windows 11. The shell is PowerShell (Windows PowerShell 5.1); a POSIX Bash tool is also available. Use PowerShell syntax by default for terminal work.
- **Permissions:** `.claude/settings.local.json` holds the local permission allowlist for this workspace.
