import pandas as pd

def padronizar_colunas(df):
    """
    Padroniza nomes das colunas:
    - lowercase
    - remove espaços extras
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df

def preparar_variavel_alvo(df):
    """
    Converte a variável churn para binário.
    """
    df = df.copy()
    df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})
    return df

def tratar_variaveis_numericas(df):
    """
    Garante que variáveis numéricas estejam no tipo correto.
    """
    df = df.copy()

    if 'totalcharges' in df.columns:
        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')

    df = df.dropna(subset=['totalcharges'])

    return df

def separar_variaveis(df):
    """
    Separa variáveis numéricas e categóricas.
    """
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include='object').columns.tolist()

    # Remover colunas que não entram no modelo
    if 'customerid' in cat_cols:
        cat_cols.remove('customerid')

    if 'churn' in num_cols:
        num_cols.remove('churn')

    return num_cols, cat_cols

def preparar_features(df):
    """
    Executa todo o feature engineering e retorna X e y.
    """
    df = padronizar_colunas(df)
    df = preparar_variavel_alvo(df)
    df = tratar_variaveis_numericas(df)

    num_cols, cat_cols = separar_variaveis(df)

    X = df[num_cols + cat_cols]
    y = df['churn']

    return X, y, num_cols, cat_cols

def preparar_features_inferencia(df):
    """
    Prepara dados para inferência (batch / API).
    NÃO espera a coluna churn.
    """
    df = padronizar_colunas(df)
    df = tratar_variaveis_numericas(df)

    num_cols, cat_cols = separar_variaveis(df)

    X = df[num_cols + cat_cols]

    return X

