import streamlit as st
import pandas as pd
import joblib
import os

# ==========================
# CONFIG
# ==========================
st.set_page_config(
    page_title="Churn Prediction",
    page_icon="📉",
    layout="centered"
)

st.title("📉 Predição de Churn")
st.caption("Simulador de risco de cancelamento de clientes")

# ==========================
# LOAD MODEL
# ==========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_random_forest.pkl")

modelo = joblib.load(MODEL_PATH)
THRESHOLD = 0.40

# ==========================
# FORM
# ==========================
with st.form("form_churn"):

    st.subheader("👤 Perfil do Cliente")
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gênero", ["Female", "Male"])
        senior = st.selectbox("Cliente é idoso (65+)?", ["Não", "Sim"])
        partner = st.selectbox("Possui parceiro(a)?", ["Não", "Sim"])
        dependents = st.selectbox("Possui dependentes?", ["Não", "Sim"])

    with col2:
        tenure = st.slider("Tempo como cliente (meses)", 0, 72, 12)
        contract = st.selectbox(
            "Tipo de contrato",
            ["Month-to-month", "One year", "Two year"]
        )

    st.divider()

    st.subheader("🌐 Serviços")
    col3, col4 = st.columns(2)

    with col3:
        internet = st.selectbox(
            "Serviço de internet",
            ["DSL", "Fiber optic", "No"]
        )
        phone = st.selectbox("Possui telefone fixo?", ["Sim", "Não"])

    with col4:
        security = st.selectbox("Segurança online", ["Sim", "Não"])
        tech = st.selectbox("Suporte técnico", ["Sim", "Não"])

    st.divider()

    st.subheader("💳 Financeiro")
    col5, col6 = st.columns(2)

    with col5:
        monthly = st.number_input(
            "Valor mensal (R$)",
            min_value=0.0,
            max_value=500.0,
            value=70.0
        )

    with col6:
        payment = st.selectbox(
            "Forma de pagamento",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    submit = st.form_submit_button("🔍 Calcular risco de churn")

# ==========================
# PROCESS INPUT
# ==========================
if submit:

    dados = {
        "gender": gender,
        "seniorcitizen": 1 if senior == "Sim" else 0,
        "partner": "Yes" if partner == "Sim" else "No",
        "dependents": "Yes" if dependents == "Sim" else "No",
        "tenure": tenure,
        "phoneservice": "Yes" if phone == "Sim" else "No",
        "multiplelines": "No",
        "internetservice": internet,
        "onlinesecurity": "Yes" if security == "Sim" else "No",
        "onlinebackup": "No",
        "deviceprotection": "No",
        "techsupport": "Yes" if tech == "Sim" else "No",
        "streamingtv": "No",
        "streamingmovies": "No",
        "contract": contract,
        "paperlessbilling": "Yes",
        "paymentmethod": payment,
        "monthlycharges": monthly,
        "totalcharges": monthly * max(tenure, 1)
    }

    input_df = pd.DataFrame([dados])

    proba = modelo.predict_proba(input_df)[:, 1][0]
    churn = int(proba >= THRESHOLD)

    st.divider()
    st.subheader("📊 Resultado")

    st.metric("Probabilidade de churn", f"{proba:.2%}")

    if churn == 1:
        st.error("⚠️ Cliente com ALTO risco de churn")
        st.caption("Ação recomendada: retenção imediata (desconto / contato ativo)")
    else:
        st.success("✅ Cliente com BAIXO risco de churn")
