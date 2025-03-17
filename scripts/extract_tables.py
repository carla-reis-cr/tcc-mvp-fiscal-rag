import os
import camelot
import pandas as pd

def processar_pdf(pdf_path, pasta_saida):

    all_tables = []
    """Processa um único PDF e salva as tabelas extraídas."""
    try:
        tables = camelot.read_pdf(
            pdf_path,
            flavor="lattice",
            pages="all",
            strip_text="\n",
            split_text=True
        )
        
        # Adicionando as tabelas extraídas à lista
        all_tables.extend(tables)
        
        # Lista para armazenar as tabelas processadas
        processed_tables = []
        
        # Processando as tabelas extraídas
        for idx, table in enumerate(tables):
            df = table.df
            
            # Verifica se a tabela tem pelo menos as três primeiras colunas: 'Nº', 'Campo' e 'Descrição'
            if df.shape[1] >= 3 and set(df.iloc[0, 0:6]) == {'Nº', 'Campo', 'Descrição', 'Tipo','Tam','Dec'}:
                # Se a tabela tem o cabeçalho esperado, adiciona ela como tabela válida
                df.columns = df.iloc[0]  # Definindo a primeira linha como os nomes das colunas
                df = df.drop(0)  # Remover a linha de cabeçalho original (primeira linha)
                
                if all(df.columns.astype(str).str.isalpha()):
                    previous_columns = df.columns
                
                print(f"Coluna Anterior:{previous_columns}" )
                processed_tables.append(df)
            elif processed_tables and df.shape[1] == processed_tables[-1].shape[1]:
                # Se a tabela não tem o cabeçalho esperado, mas tem o mesmo número de colunas que a anterior,
                # a junta com a tabela anterior
                df.columns = previous_columns
                processed_tables[-1] = pd.concat([processed_tables[-1], df], ignore_index=True)
            else:
                # Caso contrário, adiciona como uma nova tabela
                #processed_tables.append(df)
                print(f"Processado {pdf_path} - tabela desconsiderada")
        
            # Salvando as tabelas processadas como CSV
            for idx, table in enumerate(processed_tables):
                # Extrair código do registro
                if 'Descrição' in df.columns and 'Campo' in df.columns:
                        df_reg = df[df['Campo'].str.strip() == 'REG'].copy()
                        if not df_reg.empty:
                            registro =  df_reg['Descrição'].str.extract(r'contendo\s*["“]([^"”]+)["”]', expand=False)
                            if not registro.empty:
                                registro_valor = registro.iloc[0].strip()

                csv_path = os.path.join(pasta_saida, f'registro_{registro_valor}.csv')
                table.to_csv(csv_path, index=False)  # Salvando a tabela como CSV
            
        print(f"Processado {pdf_path} - {len(processed_tables)} tabela(s) processada(s).")
        return True
    
    except Exception as e:
        print(f"Erro ao processar {pdf_path}: {e}")

def processar_pasta(pasta_entrada, pasta_saida):
    """Processamento em lote com verificação de diretórios"""
    try:
        if not os.path.exists(pasta_entrada):
            raise FileNotFoundError(f"Diretório inexistente: {pasta_entrada}")
            
        os.makedirs(pasta_saida, exist_ok=True)
        
        resultados = []
        for pdf in [f for f in os.listdir(pasta_entrada) if f.lower().endswith(".pdf")]:
            pdf_path = os.path.join(pasta_entrada, pdf)
            status = processar_pdf(pdf_path, pasta_saida)
            resultados.append({"Arquivo": pdf, "Status": "✅ Sucesso" if status else "❌ Falha"})
            
        return pd.DataFrame(resultados)
    
    except Exception as e:
        print(f"Erro fatal: {str(e)}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Para execução via terminal - DEBUG
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/pdfs")
    parser.add_argument("--output", default="data/processed/registros")
    args = parser.parse_args()
    
    processar_pasta(args.input, args.output)