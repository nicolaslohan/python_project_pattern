# Script principal para execução da pipeline ETL.
# ==================================================================================
# Descrição:
#     Este script executa as etapas de extração, transformação e carga de dados 
#     (ETL), utilizando logging estruturado para rastreamento e tratamento de 
#     exceções em cada etapa.
# ==================================================================================
#     - A etapa de extração utiliza pandas para ler dados de uma fonte (exemplo: 
#       CSV, banco, etc).
#     - A etapa de transformação utiliza pandas para processar os dados extraídos.
#     - A etapa de carga utiliza funções de conexão do módulo utils.connection para 
#       inserir ou atualizar dados no destino.
# ==================================================================================
# Como usar:
#     python main.py
# ==================================================================================
# Requisitos:
#     - Python 3.x
#     - pandas instalado (pip install pandas)
#     - Dependências de conexão conforme o destino (psycopg2, fdb, pyodbc, etc)
# ==================================================================================

from pipeline.extract import example_extract
from pipeline.transform import example_transform
from pipeline.load import example_load

from utils.logger import logger
import traceback

if __name__ == '__main__':
    try:
        logger.info('Início da pipeline')

        # Extração
        try:
            df = example_extract()
        except Exception as e:
            logger.error('Falha na etapa de extração. Encerrando pipeline.')
            exit(1)

        # Transformação
        try:
            df_tr = example_transform(df)
        except Exception as e:
            logger.error('Falha na etapa de transformação. Encerrando pipeline.')
            exit(1)

        # Carga
        try:
            example_load(df_tr)
        except Exception as e:
            logger.error('Falha na etapa de carga. Encerrando pipeline.')
            exit(1)

        logger.info('Fim da pipeline')
        exit(0)
    except Exception as e:
        logger.error(f'Erro inesperado na pipeline: {e}')
        logger.error(traceback.format_exc())
        exit(1)