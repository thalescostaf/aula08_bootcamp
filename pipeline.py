from etl import pipeline_vendas

pasta_argumento: str = 'data'
formato_de_saida: list = ['csv', 'parquet']

pipeline_vendas(pasta_argumento, formato_de_saida)
