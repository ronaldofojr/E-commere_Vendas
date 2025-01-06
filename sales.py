#%%
# Carregar as bibliotecas
import pandas as pd 
import matplotlib.pyplot as plt

#%%
# Carregar o dataset
data = pd.read_csv('ecommerce_dataset_updated.csv')
data

#%%
# Visualizar as primeiras linhas do dataset

data.head()

#%%
# Obter informações gerais do dataset, Detalha as colunas, tipos de dados e valores ausentes.

data.info()

#%%
# Agora vamos para limpeza de dados
# Verificando valores ausentes por coluna

data.isnull().sum()

#%%

# Verificar e remover valores duplicados
print(f"Linhas duplicadas: {data.duplicated().sum()}")
data = data.drop_duplicates()


#%%
# Remover os espaços no inicio e no final dos nomes das colunas
data.columns = data.columns.str.strip()

#%%
# Ajustar formatos de colunas, Se houver colunas de datas ou valores mal formatados, ajustamos:
data['Purchase_Date'] = pd.to_datetime(data['Purchase_Date'], format='%d-%m-%Y')

#%%
# Verificar os primeiros valores únicos da coluna
print(data['Purchase_Date'].unique())


#%%
# Conferir o resultado da conversão
print(data['Purchase_Date'].head())

#%%
# Converter a coluna 'Purchase_Date' para o formato datetime
data['Purchase_Date'] = pd.to_datetime(data['Purchase_Date'])
data['Purchase_Date'].head()


#%%
#Realizar a Análise Explorando as Colunas Existentes
# Confirmar que os valores necessários estão presentes
print(data[['Final_Price(Rs.)', 'Category']].head())


#%%
# Analisar receita por categoria
categoria_receita = data.groupby('Category')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
categoria_receita

#%%
# Analisar receita por forma de pagamento
# Agrupar por método de pagamento e calcular receita total
metodos_pagamento_receita = data.groupby('Payment_Method')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
metodos_pagamento_receita

#%%
# Vizualizações Atualizadas por categoria

# Gráfico de barras para categorias mais lucrativas
categoria_receita.plot(kind='bar', color='skyblue',edgecolor='black',figsize=(10,6))
plt.title('Receita por Categoria',fontsize=16)
plt.xlabel('Categoria',fontsize=12)
plt.ylabel('Receita Total (Rs.)', fontsize=12)
plt.xticks(rotation=45)
plt.show()

#%%
# Receita por método de pagamento

metodos_pagamento_receita.plot(kind='bar', color='lightgreen', edgecolor='black', figsize=(10, 6))
plt.title('Receita por Método de Pagamento', fontsize=16)
plt.xlabel('Método de Pagamento', fontsize=12)
plt.ylabel('Receita Total (Rs.)', fontsize=12)
plt.xticks(rotation=45)
plt.show()

#%%

# Receita Mensal
