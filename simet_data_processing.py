from os import makedirs
import pandas as pd


def criar_diretorios(*diretorios: str) -> None:
    for d in diretorios:
        makedirs(d, exist_ok=True)


def limpar_distrito_id(df: pd.DataFrame) -> pd.DataFrame:
    # Retira o prefixo 3550308 para equiparar os códigos de distrito
    df['district_id'] = df['district_id'].astype(str).str.replace('3550308', '')
    return df


dados_simet = pd.read_csv('data/dados_para_tcc_rick_SIMET_18_10_23.csv')
dados_simet_clean = limpar_distrito_id(dados_simet)

dados_simet_clean.to_csv('dados/dados_simet_clean.csv')

diretorio_fixa = 'dados/dados_fixa'
diretorio_moveis = 'dados/dados_moveis'

criar_diretorios(diretorio_moveis, diretorio_fixa)

bandas = {'movel': diretorio_moveis, 'fixa': diretorio_fixa}

# Separa dados moveis por semestre
semestres = [
    '2020_1',
    '2020_2',
    '2021_1',
    '2021_2',
    '2022_1',
    '2022_2',
    '2023_1'
]

for banda, diretorio in bandas.items():
    dados_banda = dados_simet_clean[dados_simet_clean['banda_larga'] == banda]

    for semestre in semestres:
        dados_semestre = dados_banda[dados_banda['semestre'] == semestre]
        csv_output = f'{diretorio}/dados_{banda}_{semestre}.csv'
        dados_semestre.to_csv(csv_output, index=False)
        print(f'CSV salvo de dados {banda} para semestre {semestre}: {csv_output}')
