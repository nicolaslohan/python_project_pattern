# Módulo responsável por transformar/processar dados extraídos.
# =================================================================
# Exemplo de uso:
#     from pipeline.transform import example_transform
#     df = ... # dataframe extraído
#     df_tr = example_transform(df)
#     print(df_tr.head())
# =================================================================

import pandas as pd
from utils.logger import logger

def example_transform(df):
    try:
        logger.info("Iniciando transformação de dados...")
        # Exemplo: adicionar uma coluna
        df["nova_coluna"] = df["col1"].apply(lambda x: x * 10)
        logger.info("Transformação concluída.")
        return df
    except Exception as e:
        logger.error(f"Erro na transformação: {e}")
        raise
