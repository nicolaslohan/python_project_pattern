import os
import sys
from utils.logger import logger
from dotenv import load_dotenv

REQUIRED_ENV_VARS = [
    # Exemplo: 'API_KEY', 'DB_HOST', 'DB_USER', 'DB_PASS'
]


def check_env_vars(required_vars):
    """
    Verifica se as variáveis de ambiente necessárias estão definidas.

    Args:
        required_vars (list): Lista de nomes das variáveis de ambiente necessárias.

    Returns:
        list: Lista de nomes das variáveis de ambiente que estão ausentes.
    """
    missing = []
    for var in required_vars:
        if os.getenv(var) is None:
            missing.append(var)
    return missing


def load_env():
    """
    Carrega as variáveis de ambiente do arquivo .env.
    """
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    env_path = os.path.join(base_path, ".env")
    logger.info(f"Carregando variáveis de ambiente do arquivo: {env_path}")
    load_dotenv(env_path)

    missing_vars = check_env_vars(REQUIRED_ENV_VARS)
    if missing_vars:
        logger.error(
            f"Variáveis de ambiente obrigatórias ausentes: {', '.join(missing_vars)}"
        )
        exit(1)
    logger.info("Todas as variáveis de ambiente obrigatórias estão setadas.")


load_env()

# Defina aqui suas constantes do .env
API_KEY = os.getenv("API_KEY")
