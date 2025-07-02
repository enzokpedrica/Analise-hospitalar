import pandas as pd
import pyodbc

# Colunas que existem na tabela SQL
colunas_patients = [
    'patient_id', 'first_name', 'last_name', 'gender', 'date_of_birth',
    'contact_number', 'registration_date', 'insurance_provider',
    'insurance_number', 'email', 'number_adress', 'type_adress',
    'street', 'age'
]

colunas_medicos = [
    'doctor_id', 'first_name', 'last_name', 'specialization',
    'phone_number', 'years_experience', 'hospital_branch', 'email'
]

colunas_consultas = [
    'appointment_id', 'patient_id', 'doctor_id', 'appointment_date',
    'appointment_time', 'reason_for_visit', 'status'
]

colunas_tratamentos = [
    'treatment_id', 'appointment_id', 'treatment_type', 'description',
    'cost', 'treatment_date'
]

colunas_faturamento = [
    'bill_id', 'patient_id', 'treatment_id', 'bill_date', 'amount',
    'payment_method', 'payment_status'
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
caminho_patients = "C:\\git\\analise-hospitalar\\Silver\\patients_silver.csv"
caminho_medicos = 'C:\\git\\analise-hospitalar\\Silver\\doctors_silver.csv'
caminho_consultas = 'C:\\git\\analise-hospitalar\\Silver\\appointments_silver.csv'
caminho_tratamentos = 'C:\\git\\analise-hospitalar\\Silver\\treatments_silver.csv'
caminho_faturamento = 'C:\\git\\analise-hospitalar\\Silver\\billing_silver.csv'

carregar_csv_para_sql(caminho_patients, 'patients', colunas_patients)
carregar_csv_para_sql(caminho_medicos, '', colunas_medicos)
carregar_csv_para_sql(caminho_consultas, '', colunas_consultas)
carregar_csv_para_sql(caminho_tratamentos, '', colunas_tratamentos)
carregar_csv_para_sql(caminho_faturamento, '', colunas_faturamento)

cursor.close()
conn.close()