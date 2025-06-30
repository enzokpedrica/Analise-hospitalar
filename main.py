import pandas as pd
import os

pasta = r"C:\git\analise-hospitalar\Datasets"

# Dicionário com nomes personalizados para os arquivos
arquivos = {
    'pacientes': 'patients.csv',
    'medicos': 'doctors.csv',
    'consultas': 'appointments.csv',
    'tratamentos': 'treatments.csv',
    'faturamento': 'billing.csv'
}

# Leitura dos arquivos CSV
for nome, nome_arquivo in arquivos.items():
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    globals()[nome] = pd.read_csv(caminho_arquivo)

# Teste: mostrar as 5 primeiras linhas de cada DataFrame
print(pacientes.head())
print(medicos.head())
print(consultas.head())
print(tratamentos.head())
print(faturamento.head())