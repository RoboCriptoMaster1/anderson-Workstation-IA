# ⚙️ 15_Config

# Centro de Configuração da Workstation IA

Versão: 1.0

Última atualização: Julho de 2026

---

# Objetivo

A pasta **15_Config** centraliza todas as configurações utilizadas pela Workstation IA.

Seu principal objetivo é organizar arquivos de configuração, documentação técnica e parâmetros utilizados pelas ferramentas que compõem a plataforma.

Toda configuração permanente deverá ser armazenada nesta pasta.

---

# Estrutura Atual

```text
15_Config
│
├── Claude
├── Config
├── Excel
├── Git
├── MCP
├── MySQL
├── NodeJS
├── PowerShell
├── Python
├── VSCode
├── Windows
├── README.md
└── .gitkeep
```

---

# Finalidade de Cada Pasta

| Pasta | Finalidade |
|--------|------------|
| Claude | Configurações do Claude Code, Claude API e documentação relacionada. |
| Config | Arquivos globais da Workstation IA, como estrutura, versões e configurações gerais. |
| Excel | Configurações de Excel, VBA, Office Scripts e Power Query. |
| Git | Configurações do Git, GitHub e versionamento. |
| MCP | Configurações de servidores Model Context Protocol. |
| MySQL | Configurações do MySQL e ferramentas de banco de dados. |
| NodeJS | Configurações do Node.js, npm e ambiente JavaScript. |
| PowerShell | Configurações do terminal PowerShell e scripts administrativos. |
| Python | Configurações do ambiente Python, pacotes e ambientes virtuais. |
| VSCode | Configurações do Visual Studio Code e extensões. |
| Windows | Configurações específicas do sistema operacional Windows. |

---

# Configurações Globais

A subpasta **Config** concentra os arquivos utilizados por toda a plataforma.

Exemplo:

```text
Config
│
├── estrutura.json
├── versao.json
├── workstation.json
├── paths.json
└── configuracoes.json
```

Atualmente já faz parte da plataforma:

- estrutura.json

---

# Regras

Toda configuração deve:

- possuir documentação;
- utilizar nomes claros;
- evitar duplicação;
- permanecer organizada;
- seguir os padrões definidos no CLAUDE.md.

---

# Segurança

Esta pasta não deve armazenar:

- senhas;
- tokens;
- API Keys;
- certificados privados;
- arquivos .env.

Esses arquivos permanecem protegidos pelo `.gitignore`.

---

# Evolução

Conforme a Workstation IA evoluir, novas configurações poderão ser adicionadas.

Exemplos:

- Docker
- Kubernetes
- Terraform
- PostgreSQL
- SQLite
- Redis
- Nginx
- Linux
- Cloud
- Azure
- AWS
- Google Cloud

A estrutura deverá crescer sem comprometer a organização da plataforma.

---

# Integração com a Plataforma

A pasta **15_Config** é utilizada por diversos componentes da Workstation IA, incluindo:

- Scripts Python
- Claude Code
- Claude API
- Git
- VS Code
- Node.js
- Banco de Dados
- Automações
- Agentes de IA

Sempre que possível, os projetos devem consultar as configurações centralizadas antes de utilizar valores fixos no código.

---

# Boas Práticas

Sempre:

- documentar novas configurações;
- reutilizar arquivos existentes;
- evitar configurações duplicadas;
- manter compatibilidade entre projetos;
- registrar alterações relevantes no CHANGELOG.md.

---

# Próximas Evoluções

Nas próximas versões da Workstation IA poderão ser adicionados:

- versionamento automático das configurações;
- validação de arquivos JSON;
- backup automático das configurações;
- sincronização entre máquinas;
- gerenciamento centralizado de caminhos;
- configuração automática de ambientes.

---

# Governança

Toda alteração realizada nesta pasta deverá respeitar:

- README.md
- CLAUDE.md
- ROADMAP.md
- CHANGELOG.md

Antes de remover, renomear ou sobrescrever arquivos de configuração, recomenda-se registrar a alteração e realizar backup quando necessário.

---

# Responsável

Anderson dos Santos Damasceno

Workstation IA

Oiapoque • Amapá • Brasil

2026