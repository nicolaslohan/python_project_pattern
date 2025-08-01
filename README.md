# Projeto Pipeline ETL Python

## Descrição Geral
Este projeto segue uma estrutura modular para construção de pipelines ETL (Extração, Transformação e Carga) em Python. O código está organizado em pastas para facilitar a manutenção, reutilização e escalabilidade:

- `source/` — Código-fonte principal
  - `main.py` — Script principal para execução da pipeline
  - `pipeline/` — Módulos de extração (`extract.py`), transformação (`transform.py`) e carga (`load.py`)
  - `utils/` — Utilitários como logger, conexão com bancos, variáveis de ambiente
  - `pyproject.toml` — Metadados do projeto
  - `build.py` — Script para empacotamento do projeto
- `requirements.txt` — Dependências do projeto

## Bibliotecas Disponíveis
- `pandas` — Manipulação e análise de dados
- `psycopg2` — Conexão com PostgreSQL
- `fdb` — Conexão com Firebird
- `pyodbc` — Conexão com SQL Server
- `pyinstaller` — Empacotamento do projeto em executável
- `logging` — Registro de logs customizados

> Instale as dependências com:
> ```bash
> pip install -r requirements.txt
> ```

## Sugestão: Utilize o [uv](https://github.com/astral-sh/uv)

O [uv](https://github.com/astral-sh/uv) é um gerenciador de dependências ultrarrápido, compatível com `pip` e `pip-tools`, que acelera a instalação de pacotes Python.

**Benefícios:**
- Instala dependências até 10x mais rápido que o pip
- Compatível com ambientes virtuais
- Substitui comandos pip tradicionais

**Como instalar:**
```bash
pip install uv
```

**Como usar:**
```bash
uv pip install -r requirements.txt
```

Mais detalhes e instruções: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

## Controle de Versão com bumpver

Este projeto recomenda o uso do [bumpver](https://github.com/mbarkhau/bumpver) para controle e atualização automática de versão.

### Instalação do bumpver
```bash
pip install bumpver
```

### Como usar
- Para atualizar a versão (patch, minor ou major):
  ```bash
  bumpver update --patch   # Para atualizar o patch (ex: 1.0.0 → 1.0.1)
  bumpver update --minor   # Para atualizar o minor (ex: 1.0.0 → 1.1.0)
  bumpver update --major   # Para atualizar o major (ex: 1.0.0 → 2.0.0)
  ```
- O bumpver atualiza automaticamente o campo de versão no `pyproject.toml` e outros arquivos configurados.

Mais detalhes e configurações avançadas: [https://github.com/mbarkhau/bumpver](https://github.com/mbarkhau/bumpver)

## Instruções de Instalação
1. Clone o repositório ou copie os arquivos para seu ambiente local.
2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   # ou, para maior velocidade:
   uv pip install -r requirements.txt
   ```
4. Configure o arquivo `.env` em `source/utils/` conforme necessário.
5. Execute a pipeline:
   ```bash
   python source/main.py
   ```

---

Para empacotar o projeto como executável, utilize o `build.py` conforme instruções no próprio arquivo.
