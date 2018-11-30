import pandas as pd

names = ['PERIODO', 'UF', 'MUNICIPIO', 'COD_MUNICIPIO_TSE', 'NR_ZONA', 'SEXO',
         'FAIXA_ETARIA', 'GRAU_ESCOLARIDADE', 'QTE_ELEITORES_PERFIL']

df2012 = pd.read_csv('perfil_eleitorado/perfil_eleitorado_2012.txt',
                  encoding='latin1', sep=';', names=names)

df2012 = df2012[df2012.UF == 'RN'][['MUNICIPIO', 'NR_ZONA', 'SEXO',
                                    'FAIXA_ETARIA', 'GRAU_ESCOLARIDADE',
                                    'QTE_ELEITORES_PERFIL']]

eleitores_df2012 = df2012.groupby('MUNICIPIO')['QTE_ELEITORES_PERFIL'].sum()
sexo_df2012 = df2012.groupby(['MUNICIPIO', 'SEXO'])['SEXO'].count()
faixa_etaria_df2012 = df2012.groupby(['MUNICIPIO', ''])['SEXO'].count()






