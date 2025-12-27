# 📊 Customer Churn Prediction — Telco Dataset (Kaggle)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-red)]()
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-End--to--End-orange)]()

---

## 🔗 Acessos Online

- 🌐 **API de Predição (FastAPI)**  
  👉 https://churn-api-vprr.onrender.com/docs

- 🖥️ **Demo Interativa (Streamlit Cloud)**  
  👉 https://churn-prediction-byvitoriagblima.streamlit.app/

> A API permite predição individual de churn.  
> A interface Streamlit funciona como uma demonstração interativa do modelo.

---

## 📌 Visão Geral

Este projeto utiliza o **dataset Telco Customer Churn**, disponibilizado no Kaggle, com o objetivo de **prever a probabilidade de churn (cancelamento de serviço)** de clientes de uma empresa de telecomunicações.

O projeto foi desenvolvido como um **caso completo de Data Science**, cobrindo todas as etapas do ciclo de vida de um modelo preditivo, desde a análise exploratória até a disponibilização em produção.

---

## 📂 Sobre o Dataset (Kaggle)

- **Fonte:** Kaggle — Telco Customer Churn
- **Tipo:** Dados tabulares
- **Tamanho:** ~7.000 clientes
- **Variável alvo:** `Churn` (Yes / No)

### Principais grupos de variáveis:
- **Perfil do cliente:** gênero, idade, dependentes
- **Serviços contratados:** internet, segurança, streaming, suporte
- **Contrato:** tipo, método de pagamento, fatura digital
- **Financeiro:** cobrança mensal e total
- **Relacionamento:** tempo de contrato (`tenure`)

---

## 🎯 Objetivo do Projeto

- Prever a **probabilidade de churn** de cada cliente
- Identificar clientes em **faixa de risco**
- Apoiar decisões de retenção com base em dados
- Gerar dados prontos para consumo analítico (Power BI)

---

## 🧠 Abordagem de Data Science

- **Tipo de problema:** Classificação binária
- **Modelos avaliados:**
  - Regressão Logística (baseline)
  - Random Forest (modelo final)
  - XGBoost (comparativo)
- **Métricas principais:**
  - ROC-AUC
  - Recall da classe churn
- **Decisão orientada a negócio:**
  - Ajuste de threshold com base em custo
  - Criação de faixas de risco operacionais

---

## 📁 Descrição dos Componentes

### 📊 Notebooks
Documentam todo o raciocínio analítico:
- **EDA:** identificação de padrões e fatores de churn  
- **Feature Engineering:** preparação das variáveis  
- **Modelagem:** comparação de modelos  
- **Threshold & Custo:** decisão orientada a impacto financeiro  
- **Validação:** coerência entre churn predito e comportamento esperado  

---

### 🔄 Inferência em Lote (Batch)
- `batch/predict_batch.py`  
Executa predições em massa sobre clientes ativos, gerando:
- Probabilidade de churn
- Faixa de risco
- CSV final para análise e dashboards

---

### 🌐 API de Predição
- `api/main.py`  
API desenvolvida com **FastAPI** para:
- Predição individual de churn
- Integração com sistemas externos
- Uso em tempo real

📌 Documentação interativa disponível em `/docs`.

---

### 🖥️ Interface Streamlit
- `frontend/app.py`  
Interface interativa para demonstração do modelo, permitindo simular cenários de clientes e visualizar o risco de churn.

---

## 📊 Saída para Power BI

O arquivo:

predictions/churn_predicoes.csv


está pronto para ser conectado diretamente ao **Power BI**, possibilitando análises como:
- Distribuição de clientes por faixa de risco
- Churn por tipo de contrato
- Churn por tempo de relacionamento
- Prioridade de retenção

---

## 🚀 Status do Projeto

✔️ Projeto finalizado  
✔️ Modelo validado  
✔️ Inferência em lote funcional  
✔️ API e interface disponíveis  

---

## 🧑‍💻 Autoria

Projeto desenvolvido como estudo prático de **Data Science aplicado a dados reais**, cobrindo o fluxo completo:
**dados → modelo → decisão → produção → visualização**.

---

### 🔧 Possíveis Evoluções
- Dashboard executivo no Power BI
- Monitoramento de performance e drift
- Automação de batch (MLOps básico)
