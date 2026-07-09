"""
=====================================================
Workstation Tasks
Configurações da Aplicação
Versão: 0.4.0
=====================================================
"""

import os

from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()


class Config:
    """
    Configurações base da aplicação.
    """

    # =====================================================
    # Segurança
    # =====================================================

    SECRET_KEY = os.getenv("SECRET_KEY")

    if not SECRET_KEY:
        raise RuntimeError(
            "SECRET_KEY não encontrada. Configure o arquivo .env."
        )

    # =====================================================
    # Banco de Dados
    # =====================================================

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    # Validação das variáveis obrigatórias
    required = {
        "DB_HOST": DB_HOST,
        "DB_PORT": DB_PORT,
        "DB_NAME": DB_NAME,
        "DB_USER": DB_USER,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise RuntimeError(
            f"Variáveis obrigatórias não configuradas: {', '.join(missing)}"
        )

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        "?charset=utf8mb4"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =====================================================
    # Pool de Conexões MySQL
    # =====================================================

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 280,
    }

    # =====================================================
    # Aplicação
    # =====================================================

    APP_NAME = os.getenv(
        "APP_NAME",
        "Workstation Tasks"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "0.4.0"
    )

    TIMEZONE = os.getenv(
        "TZ",
        "America/Belem"
    )