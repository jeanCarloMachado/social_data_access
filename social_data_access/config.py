

BASE_DATA_PATH = "/Users/jean.machado/projects/social_data_access/local_data"

DATA_METADATA = {
    'world_bank.gdp_percentage': {
        'path': BASE_DATA_PATH + "/world_bank/gdp_percentage/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_401130.csv",
    },
    'world_bank.expenditure_on_education': {
        'path': BASE_DATA_PATH + "/world_bank/gdp_percentage/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_401130.csv",
        'source': 'https://data.worldbank.org/indicator/SE.XPD.TOTL.GB.ZS?locations=BR-DE'
    },
    'world_bank.poverty': {
        'path': BASE_DATA_PATH + "/world_bank/poverty/API_11_DS2_en_csv_v2_512996.csv",
    },
    'world_bank.gdp_absolute': {
        'path': BASE_DATA_PATH + "/world_bank/gdp_absolute/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_401322.csv",
    },
    'world_bank.people_living_in_slums': {
        'path': BASE_DATA_PATH + "/world_bank/people_living_in_slums/API_EN.POP.SLUM.UR.ZS_DS2_en_csv_v2_443669.csv",
        'source': 'https://data.worldbank.org/indicator/EN.POP.SLUM.UR.ZS?locations=BR'
    },
    'ibge.cities_with_favela_2010': {
        'path': BASE_DATA_PATH + '/ibge/tab1_2010.xls',
        'source': 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html',
        'read_parameters': {'usecols': "A:G", 'skiprows': 4, 'index_col': 0},
        'description': """Path: Censo_Demografico_2010/Aglomerados_subnormais/Aglomerados_subnormais_informacoes_territoriais/tabelas_xls/UFs_Municípios.zip
    """
    },
    'ibge.cities_with_favela_2020': {
        'path': BASE_DATA_PATH + '/ibge/tab1_2020.xlsx',
        'source': 'https://sidra.ibge.gov.br/Tabela/8440#resultado',
        'description': "From all cities in brazil which ones have a favela?",
        'read_parameters': {'skiprows': 4, 'index_col': 0}
    }
}
