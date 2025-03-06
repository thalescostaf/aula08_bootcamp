import pandas as pd
import os
import glob


# Função que concatena os arquivos JSON e transforma em um dataframe
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    
    return df_total

def calcular_kpi_total(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['quantidade'] * df['venda']
    
    return df

def carregar_dados(df: pd.DataFrame, formato_saida: list):
    
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv("Dados_com_total.csv", index=False)
        if format == 'parquet':
            df.to_parquet("Dados_com_total_parquet.csv", index=False)

def pipeline_vendas(pasta:str, formato_de_saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_total(data_frame)
    print(carregar_dados(data_frame_calculado, formato_de_saida))

# Código main do programa, fazer os teste das funções aqui
if __name__ == '__main__':

    pipeline_vendas()