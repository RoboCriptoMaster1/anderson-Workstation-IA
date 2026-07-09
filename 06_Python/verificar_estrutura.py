"""
verificar_estrutura.py

Objetivo:
    Verificar se a estrutura oficial de pastas da Workstation IA
    está criada corretamente no diretório raiz.

Autor: Anderson - Workstation IA
Versão: 1.0
"""

from pathlib import Path
import json



# -----------------------------------------------------------------------------
# Configurações
# -----------------------------------------------------------------------------

ARQUIVO_ESTRUTURA = (
    Path(__file__).resolve().parent.parent
    / "15_Config"
    / "Config"
    / "estrutura.json"
)


def carregar_pastas_oficiais() -> list[str]:
    """
    Lê a estrutura oficial da Workstation IA a partir do arquivo estrutura.json.
    """

    with open(ARQUIVO_ESTRUTURA, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["pastas"]


PASTAS_OFICIAIS = carregar_pastas_oficiais()
# -----------------------------------------------------------------------------
# Funções
# -----------------------------------------------------------------------------

def obter_raiz() -> Path:
    """
    Retorna o diretório raiz da Workstation IA.

    Como este script fica em '06_Python', a raiz é o diretório-pai (parent)
    da pasta onde o arquivo está localizado.
    """
    return Path(__file__).resolve().parent.parent


def verificar_estrutura(raiz: Path) -> tuple[list[str], list[str]]:
    """
    Compara as pastas existentes na raiz com a estrutura oficial.

    Parâmetros:
        raiz (Path): diretório raiz da Workstation IA.

    Retorna:
        tuple: (pastas_ok, pastas_faltando)
            - pastas_ok: pastas oficiais encontradas.
            - pastas_faltando: pastas oficiais que não existem.
    """
    pastas_ok = []
    pastas_faltando = []

    for pasta in PASTAS_OFICIAIS:
        caminho = raiz / pasta
        # is_dir() confirma que existe E que é realmente um diretório.
        if caminho.is_dir():
            pastas_ok.append(pasta)
        else:
            pastas_faltando.append(pasta)

    return pastas_ok, pastas_faltando


def exibir_relatorio(pastas_ok: list[str], pastas_faltando: list[str]) -> None:
    """
    Exibe no terminal um relatório simples da verificação.
    """
    print("=" * 50)
    print(" VERIFICACAO DA ESTRUTURA - WORKSTATION IA")
    print("=" * 50)

    for pasta in PASTAS_OFICIAIS:
        status = "[OK]" if pasta in pastas_ok else "[FALTANDO]"
        print(f" {status:<12} {pasta}")

    print("-" * 50)
    print(f" Total oficial : {len(PASTAS_OFICIAIS)}")
    print(f" Encontradas   : {len(pastas_ok)}")
    print(f" Faltando      : {len(pastas_faltando)}")
    print("=" * 50)

    # Mensagem final resumindo o resultado geral.
    if not pastas_faltando:
        print(" Resultado: estrutura 100% correta!")
    else:
        print(" Resultado: existem pastas faltando. Verifique acima.")


# -----------------------------------------------------------------------------
# Execução principal
# -----------------------------------------------------------------------------

def main() -> None:
    """
    Função principal: orquestra a verificação da estrutura.
    """
    raiz = obter_raiz()
    pastas_ok, pastas_faltando = verificar_estrutura(raiz)
    exibir_relatorio(pastas_ok, pastas_faltando)


# Garante que o main() só roda quando o arquivo for executado diretamente,
# e não quando for importado por outro script.
if __name__ == "__main__":
    main()
