# Módulo responsável por extrair dados de fontes externas (bancos, arquivos, APIs, etc).
# =========================================================================================
# Exemplo de uso:
#     from pipeline.extract import example_extract
#     df = example_extract()
#     print(df.head())
# =========================================================================================
import pandas as pd
from utils.logger import logger

def example_extract():
    try:
        logger.info("Iniciando extração de dados...")
        # Exemplo: leitura de um arquivo CSV
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
        logger.info(f"Extração concluída. {len(df)} registros extraídos.")
        return df
    except Exception as e:
        logger.error(f"Erro na extração: {e}")
        raise
