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

# Código main do programa, fazer os teste das funções aqui
if __name__ == '__main__':
    pasta_argumento = 'data'
    data_frame = extrair_dados(pasta=pasta_argumento)
    print(calcular_kpi_total(data_frame))

    