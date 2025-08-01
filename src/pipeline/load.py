
# Módulo responsável por carregar dados processados para o destino final (banco, arquivo, etc).
# =============================================================================================
# Exemplo de uso:
#     from pipeline.load import example_load
#     df = ... # dataframe transformado
#     example_load(df)
# =============================================================================================

from utils.logger import logger
from utils.connection import connect_postgres  # Exemplo: ajuste conforme o destino

def example_load(df):
    try:
        logger.info("Iniciando carga de dados...")
        # Exemplo: conectar e simular carga
        # conn = connect_postgres(host, database, user, password)
        # df.to_sql('tabela_destino', conn, if_exists='replace', index=False)
        logger.info(f"Carga concluída. {len(df)} registros carregados.")
    except Exception as e:
        logger.error(f"Erro na carga: {e}")
        raise
