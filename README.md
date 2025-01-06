# Análise de Vendas em E-commerce

## Descrição

Este projeto tem como objetivo realizar uma análise exploratória dos dados de vendas de um e-commerce, buscando insights sobre o comportamento de compra dos usuários, a performance das categorias de produtos, e a contribuição dos diferentes métodos de pagamento para a receita total. A análise é feita utilizando a linguagem Python, com foco na exploração de dados, limpeza de dados, visualizações e geração de insights para um entendimento mais profundo das métricas de vendas.

## Objetivos do Projeto

- **Carregar e Limpar os Dados**: Importar o dataset, tratar valores ausentes, duplicados e garantir que os tipos de dados estejam corretos.
- **Análise Exploratória de Dados (EDA)**: Analisar as distribuições de preços, categorias e formas de pagamento, e entender como esses elementos influenciam as vendas.
- **Geração de Insights**: Fornecer insights sobre as categorias mais lucrativas, formas de pagamento mais comuns, e a receita mensal.
- **Visualizações**: Criar gráficos informativos para facilitar a interpretação dos dados e os resultados da análise.

## Bibliotecas Utilizadas

- **pandas**: Para manipulação e análise de dados.
- **matplotlib**: Para criação de gráficos e visualizações.

## Estrutura do Projeto

O projeto é estruturado em várias etapas, que são detalhadas abaixo:

### 1. Carregar as Bibliotecas e o Dataset

Inicializamos as bibliotecas necessárias e carregamos o dataset CSV.

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### 1. Carregar o dataset
```python
data = pd.read_csv('ecommerce_dataset_updated.csv')
```

### 2. Visualização Inicial do Dataset
Exibimos as primeiras linhas e as informações gerais do dataset para entender melhor sua estrutura.

```python
data.head()
data.info()
```

### 3. Limpeza de Dados
Verificamos e tratamos valores ausentes e duplicados. Também garantimos que os nomes das colunas estejam limpos, sem espaços adicionais.

```python
data.isnull().sum()  # Verificar valores ausentes
data.duplicated().sum()  # Verificar valores duplicados
data = data.drop_duplicates()  # Remover duplicados
data.columns = data.columns.str.strip()  # Remover espaços nas colunas
```

### 4. Ajuste de Formatos de Colunas
Convertimos as colunas de data para o formato datetime para garantir que possamos manipulá-las corretamente.

```python
data['Purchase_Date'] = pd.to_datetime(data['Purchase_Date'], format='%d-%m-%Y')
```

### 5. Análise de Receita por Categoria e Forma de Pagamento
Agrupamos os dados por categoria de produto e forma de pagamento para calcular a receita total.

```python
categoria_receita = data.groupby('Category')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
metodos_pagamento_receita = data.groupby('Payment_Method')['Final_Price(Rs.)'].sum().sort_values(ascending=False)
```


### 6. Visualizações
Criamos gráficos para visualização da receita por categoria e por método de pagamento, além da receita mensal.

```python
categoria_receita.plot(kind='bar', color='skyblue', figsize=(10, 6))
metodos_pagamento_receita.plot(kind='bar', color='lightgreen', figsize=(10, 6))
```


### 7. Cálculo da Receita Mensal
Calculamos a receita mensal, agrupando os dados por mês e somando as vendas.

```python
data['Month'] = data['Purchase_Date'].dt.to_period('M')
receita_mensal = data.groupby('Month')['Final_Price(Rs.)'].sum()
receita_mensal.plot(kind='line', color='orange', figsize=(10, 6))
```

## Resultados Obtidos
### Categorias Mais Lucrativas:
Identificação das categorias de produtos que mais geraram receita.
### Métodos de Pagamento: 
Análise dos métodos de pagamento mais utilizados e a contribuição de cada um para a receita total.
### Receita Mensal: 
Visualização da receita mensal, permitindo identificar picos de vendas ou períodos com menor performance.


## Considerações Finais
Este projeto demonstra o uso de análise exploratória de dados (EDA) para um conjunto de dados de vendas em e-commerce. Ele pode ser utilizado para melhorar a compreensão dos padrões de vendas, otimizar estratégias de marketing e pagamento, e fornecer insights para aumentar a rentabilidade de uma plataforma de e-commerce.
