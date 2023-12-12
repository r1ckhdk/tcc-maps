import pandas as pd


def unir_tabelas_por_semestre(sem1: pd.DataFrame, sem2: pd.DataFrame) -> pd.DataFrame:
    tabela_unida = pd.merge(sem1, sem2, on='district_id', suffixes=('_1', '_2'))
    return tabela_unida


anos = [
    '2020',
    '2021',
    '2022'
]

diretorio_fixa = 'dados/dados_fixa'
diretorio_movel = 'dados/dados_moveis'


for ano in anos:
    semestre_1 = pd.read_csv(f'{diretorio_fixa}/dados_fixa_{ano}_1.csv')
    semestre_2 = pd.read_csv(f'{diretorio_fixa}/dados_fixa_{ano}_2.csv')

    csv_output_fixa = f'{diretorio_fixa}/dados_consolidados_{ano}.csv'

    tabela_anual_fixa = unir_tabelas_por_semestre(semestre_1, semestre_2)
    tabela_anual_fixa.to_csv(csv_output_fixa)
    print(f'Tabela {csv_output_fixa} gerada.')

    semestre_1_movel = pd.read_csv(f'{diretorio_movel}/dados_movel_{ano}_1.csv')
    semestre_2_movel = pd.read_csv(f'{diretorio_movel}/dados_movel_{ano}_2.csv')

    csv_output_movel = f'{diretorio_movel}/dados_consolidados_{ano}.csv'

    tabela_anual_movel = unir_tabelas_por_semestre(semestre_1_movel, semestre_2_movel)
    tabela_anual_movel.to_csv(csv_output_movel)
    print(f'Tabela {csv_output_movel} gerada.')
