import pandas as pd


def check_nulls():

    print("Iniciando validação de valores nulos...")

    # Exemplo: leitura de dados (ajuste para seu caso real)
    df = pd.read_csv("data/sample_data.csv")

    # Verifica valores nulos
    null_count = df.isnull().sum()

    print("Resultado da validação:")

    for column, count in null_count.items():
        print(f"Coluna: {column} | Nulos: {count}")

        if count > 0:
            print(f"Atenção: Existem valores nulos em {column}")

    print("Validação finalizada com sucesso.")
