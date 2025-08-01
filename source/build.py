# Script de build para geração de executável do projeto.
#
# Instruções de uso:
# ======================================================
# 1. Caso queira gerar arquivos executáveis para o seu projeto:
#    - Faça o update da versão do projeto executando:
#      'build upgrade -- (MINOR, MAJOR ou PATCH)'
#      (Ajuste a versão no pyproject.toml conforme a necessidade)
#    - Execute este script para gerar o executável.
#    - O executável será disponibilizado na pasta 'builds/dist'.

# 2. O build inclui as seguintes pastas e arquivos no executável:
#    - utils/.env (arquivo de variáveis de ambiente)
#    - logs (pasta de logs)
#    - pipeline (pasta de pipelines)
#    - utils (pasta de utilitários)
#    - Outras pastas podem ser adicionadas conforme necessário.

# 3. Requisitos:
#    - Python instalado
#    - pyinstaller instalado (pip install pyinstaller 
#       -- ou 'uv pip install pyinstaller' caso utilize uv)

# 4. Exemplo de execução:
#    python build.py
# ======================================================

import os
import re

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Buscar versão do projeto no pyproject.toml
version = "1.0.0"
pyproject_path = os.path.join(BASE_DIR, "pyproject.toml")
if os.path.exists(pyproject_path):
    with open(pyproject_path, "r", encoding="utf-8") as f:
        content = f.read()
        match = re.search(r'^version\s*=\s*"([\d\.]+)"', content, re.MULTILINE)
        if match:
            version = match.group(1)

os.system(
    f"pyinstaller --onefile {BASE_DIR}/main.py "
    f"--name meta_vendedor_remoto_v{version.replace('.', '_')} "
    f"--distpath {BASE_DIR}/../builds/dist "
    f"--workpath {BASE_DIR}/../builds/build "
    f"--specpath {BASE_DIR}/../builds/spec "
    f'--add-data "{BASE_DIR}/utils/.env;." '
    f'--add-data "{BASE_DIR}/logs;logs" '
    f'--add-data "{BASE_DIR}/pipeline;pipeline" '
    f'--add-data "{BASE_DIR}/utils;utils" '
    # Adicione pastas extras aqui
)