# AuditaFiscal RAG 🧾🔍

**Sistema Inteligente de Validação Fiscal com RAG**  
*Combine regras tributárias com IA generativa para validação fiscal explicável*

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carla-reis-cr/tcc-mvp-fiscal-rag/blob/main/notebooks/fiscalrag_mvp.ipynb)

![Fluxo do FiscalRAG](https://via.placeholder.com/800x400.png?text=Fluxo+do+FiscalRAG+-+Extração+de+Regras+→+Validação+→+Explicação+com+RAG)

## Funcionalidades Principais

**📄 Extração Automática de Regras** de manuais técnicos da Receita Federal (SPED)

**🔎 Validação Inteligente** de registros fiscais com regex e lógica condicional

**🤖 Explicações Contextuais** usando RAG (Retrieval-Augmented Generation)

**📊 Suporte Multi-Formato** para PDFs, Excel e bancos de dados SQL

**⚙️ Configuração Modular** para diferentes regimes tributários


## **Tecnologias Utilizadas**

- **Linguagem**: `Python 3.9+`
- **Gerenciamento de Ambiente**: `conda`
- **Manipulação de Dados**: `pandas` 


## **Pré-requisitos**

- Python 3.8 ou superior
- Anaconda3
- 4GB de RAM livre (8GB recomendado)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/tcc-mvp-fiscal-rag.git
cd tcc-mvp-fiscal-rag
```

2. Crie e ative o ambiente Conda:
```bash
conda env create -f environment.yml
conda activate fiscalrag
```

3. Crie as pastas dos dados:
```bash
mkdir -p data/pdfs data/processed
```

## Estrutura do Projeto

```bash
fiscalrag/
├── data/               # Dados estruturados e brutos
├── notebooks/          # Jupyter notebooks de análise
├── scripts/            # Scripts de processamento
└── environment.yml     # Configuração do ambiente conda
```

## Usos Básicos

### **Extração das tabelas do(s) PDF(s)**:

Adicionar o(s) arquivo(s) que deseja que sejam extraídos as tabelas referente aos registros do SPED na pasta `data/pdfs`, rodar o código:
```bash
python scripts/extract_tables.py
```


