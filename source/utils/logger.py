# =============================================================================
# Exemplos de uso do logger:
# =============================================================================
# from utils.logger import logger
#
# logger.debug("Mensagem de debug")
# logger.info("Informação relevante")
# logger.warning("Atenção!")
# logger.error("Ocorreu um erro")
#
# try:
#     1 / 0
# except Exception as e:
#     logger.exception("Exceção capturada: {e}")
# =============================================================================

from loguru import logger
import sys
from pathlib import Path

# Criar diretório de logs se não existir
log_path = Path("logs")
log_path.mkdir(parents=False, exist_ok=True)

# Remove o handler default do logger
logger.remove()

# Configura a saída no console
logger.add(
    sys.stdout,
    colorize=True,
    format = "<green>{time:DD/MM/YYYY HH:mm:ss}</green> (<blue>{file}:{line}</blue>) [<level>{level}</level>] - <cyan>{message}</cyan>",
    level="DEBUG",
)

# Configura o arquivo de saída com rotação e retenção
logger.add(
    log_path / "app.log",
    rotation="1 MB",        # Rotaciona arquivos ao atingir 1 MB
    retention="7 days",     # Mantém o arquivo no sistema por 7 dias
    compression="zip",      # Comprime logs antigos
    encoding="utf-8",
    level="DEBUG",
    format="{time:DD/MM/YYYY HH:mm:ss} ({file}:{line}) [{level}] - {message}",
)

