import pandas as pd
import joblib
import os
import sys

# =====================================
# CONFIGURAÇÃO DE PATH
# =====================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from feature_engineering import preparar_features_inferencia

# =====================================
# CAMINHOS
# =====================================

CAMINHO_MODELO = os.path.join(BASE_DIR, "models", "best_random_forest.pkl")
CAMINHO_ENTRADA = os.path.join(BASE_DIR, "data", "clientes_ativos.csv")
CAMINHO_SAIDA = os.path.join(BASE_DIR, "predictions", "churn_predicoes.csv")

# =====================================
# FAIXA DE RISCO
# =====================================

def definir_faixa_risco(prob):
    if prob >= 0.60:
        return "Risco Muito Alto"
    elif prob >= 0.30:
        return "Risco Alto"
    elif prob >= 0.20:
        return "Risco Médio"
    else:
        return "Risco Baixo"

# =====================================
# EXECUÇÃO
# =====================================

print("🔄 Carregando modelo...")
modelo = joblib.load(CAMINHO_MODELO)

print("📥 Lendo dados de entrada...")
df_raw = pd.read_csv(CAMINHO_ENTRADA)

print("🧼 Aplicando feature engineering (inferência)...")
X = preparar_features_inferencia(df_raw)

print("🧠 Gerando probabilidades de churn...")
probas = modelo.predict_proba(X)[:, 1]

print("📊 Montando DataFrame de saída...")
df_filtrado = df_raw.loc[X.index].copy()

df_filtrado["probabilidade_churn"] = probas
df_filtrado["faixa_risco"] = df_filtrado["probabilidade_churn"].apply(definir_faixa_risco)

print("💾 Salvando arquivo de saída...")
os.makedirs(os.path.dirname(CAMINHO_SAIDA), exist_ok=True)
df_filtrado.to_csv(CAMINHO_SAIDA, index=False)

print("✅ Batch executado com sucesso!")
print(f"📄 Arquivo gerado em: {CAMINHO_SAIDA}")
