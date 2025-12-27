import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def grafico_barras(df, coluna, titulo, rotacao=0):
    verde_pastel = '#dbead5'  
    vermelho_pastel = '#ff0000'
    cores_churn = [verde_pastel, vermelho_pastel]
    
    plt.figure(figsize=(10, 5))
    order = df[coluna].value_counts().index
    ax = sns.countplot(data=df, x=coluna, hue='Churn', palette=cores_churn, order=order)
    
    plt.title(titulo, fontsize=14, pad=30)
    plt.xlabel(f'\n{coluna}')
    ax.set_yticks([])
    ax.set_ylabel('')
    plt.legend(title='Churn')
    plt.xticks(rotation=rotacao)
    plt.grid(False)
    
    for container in ax.containers:
        ax.bar_label(container, fontsize=9)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    plt.show()

def grafico_boxplot(df, coluna, titulo):
    verde_pastel = '#dbead5'  
    vermelho_pastel = '#ff0000'
    cores_churn = [verde_pastel, vermelho_pastel]
    
    plt.figure(figsize=(10, 5))
    ax = sns.boxplot(data=df, x='Churn', y=coluna, palette=cores_churn)
    
    plt.title(titulo, fontsize=14, pad=30)
    plt.xlabel('Churn')
    plt.ylabel(coluna)
    plt.grid(False)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    plt.show()

def grafico_histograma(df, coluna, titulo, bins=30):
   
    verde_pastel = '#dbead5'  
    vermelho_pastel = '#ff0000'
    cores_churn = {'No': verde_pastel, 'Yes': vermelho_pastel}
    
    plt.figure(figsize=(12, 6))
    
    g = sns.FacetGrid(df, hue='Churn', palette=cores_churn, height=6, aspect=1.5)
    g.map(sns.histplot, coluna, bins=20, alpha=0.7)
    g.add_legend(title='Churn')
    
    plt.title(titulo, fontsize=14, pad=30)
    plt.grid(False)
    
    plt.tight_layout()
    plt.show()

def grafico_correlacao_numericas(df):

    df_corr = df.copy()

    df_corr['Churn'] = df_corr['Churn'].map({'Yes': 1, 'No': 0})
    df_corr['TotalCharges'] = pd.to_numeric(df_corr['TotalCharges'], errors='coerce')

    df_corr = df_corr.select_dtypes(include=['int64', 'float64'])

    plt.figure(figsize=(8, 5))
    sns.heatmap(
        df_corr.corr()[['Churn']].sort_values(by='Churn', ascending=False),
        annot=True,
        cmap='coolwarm',
        fmt='.2f'
    )
    plt.title("Correlação das Variáveis Numéricas com Churn")
    plt.tight_layout()
    plt.show()


