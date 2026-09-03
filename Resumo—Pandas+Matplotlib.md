# 📊 Resumo rápido — Pandas + Matplotlib

## Importações

```python
import pandas as pd
import matplotlib.pyplot as plt
```
## Ler um arquivo CSV

```python
dados = pd.read_csv("arquivo.csv")
```
## Selecionar apenas colunas numéricas

```python
numericas = dados.select_dtypes(include="number")
```

# 1. Média
média geral

```python
print(numericas.mean())
```

média por coluna

```python
print(dados["CRIM"].mean())
```

# 2. Mediana

```python
print(numericas.median())
````
# 3. Desvio padrão


```python
print(numericas.std())
```


# 4. Quartis

Os principais quartis são:

Q1 = 25%
Q2 = 50% = mediana
Q3 = 75%

```python
print(numericas.quantile(0.25))
print(numericas.quantile(0.50))
print(numericas.quantile(0.75))
```

# 5. Mínimo e máximo

Mínimo

```python
print(numericas.min())
```
Máximo

```python
print(numericas.max())
```

# Atalho: describe()
O `describe()` calcula várias dessas informações de uma vez:

```python
print(numericas.describe())
```

# 📈 Matplotlib

### Histograma

Mostra a distribuição dos valores.

```python
plt.hist(dados["CRIM"], bins=20)
plt.show()
```
Com título e nomes nos eixos:
```python

plt.hist(dados["CRIM"].dropna(), bins=20)

plt.title("Distribuição de CRIM")
plt.xlabel("Valores")
plt.ylabel("Frequência")

plt.show()
```

`bins=20` significa que os dados serão separados em aproximadamente 20 intervalos.

## Gráfico de barras

Usado principalmente para comparar categorias.

```python
dados["CHAS"].value_counts().plot(kind="bar")

plt.title("Quantidade por categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")

plt.show()
```
