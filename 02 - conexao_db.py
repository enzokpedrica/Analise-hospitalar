import pandas as pd
import pyodbc

# Colunas que existem na tabela SQL
colunas_patients = [
    'patient_id', 'first_name', 'last_name', 'gender', 'date_of_birth',
    'contact_number', 'registration_date', 'insurance_provider',
    'insurance_number', 'email', 'number_adress', 'type_adress',
    'street', 'age'
]


conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'  # Ajuste para o seu
    'DATABASE=hospital_data;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Função para carregar CSV para SQL
def carregar_csv_para_sql(nome_arquivo, nome_tabela, colunas_ordenadas):
    df = pd.read_csv(nome_arquivo)


    # Reordenar colunas para garantir a ordem correta
    df = df[colunas_ordenadas]

    # Substituir NaN por None para evitar erros no SQL
    df = df.where(pd.notnull(df), None)

    colunas = ', '.join(colunas_ordenadas)
    placeholders = ', '.join(['?' for _ in colunas_ordenadas])
    query = f"INSERT INTO {nome_tabela} ({colunas}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        cursor.execute(query, tuple(row))

    conn.commit()
    print(f'{len(df)} registros inseridos em {nome_tabela}')


# Caminhos dos arquivos
caminho = "C:\\git\\analise-hospitalar\\Silver\\patients_silver.csv"
carregar_csv_para_sql(caminho, 'patients', colunas_patients)

cursor.close()
conn.close()