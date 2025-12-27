import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(os.path.join(BASE_DIR, "data", "raw", "telco_churn.csv"))

# Remove a variável alvo
df = df.drop(columns=["Churn"])

# Salva como clientes ativos
df.to_csv(os.path.join(BASE_DIR, "data", "clientes_ativos.csv"), index=False)

print("Arquivo clientes_ativos.csv criado com sucesso!")
