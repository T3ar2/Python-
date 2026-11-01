import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn import preprocessing
import math
from pickle import dump

from collections import Counter
from imblearn.over_sampling import SMOTE

dados = pd.read_csv('iris.csv', sep=';')

# 1. Balancear a base 
resampler = SMOTE()

dados_atributos = dados.drop(columns=['class'])
dados_classes = dados['class'] 

dados_atributos_b, dados_classes_b = resampler.fit_resample(dados_atributos, dados_classes)

dados = dados_atributos_b.join(dados_classes_b)
# print("Dados balanceados:", Counter(dados['class']))

# 2. Normalizar a base 
# 2.a Separar os dados numéricos dos dados categóricos
dados_num = dados.drop(columns=['class'])
dados_cat = dados['class']
dados_cat_rotulos = 'class'

# 2.b MinMax para os numéricos e get_dummies para os categóricos
normalizador = preprocessing.MinMaxScaler()

# normalizando dados numéricos 
modelo_normalizador = normalizador.fit(dados_num)
dump(modelo_normalizador, open('modelo_normalizador.pkl', 'wb'))

dados_num_normalizados = modelo_normalizador.fit_transform(dados_num)
dados_num_normalizados = pd.DataFrame(dados_num_normalizados, columns=dados_num.columns)
# print(dados_num_normalizados)

# normalizando dados categóricos
# print(dados_cat)
dados_cat_normalizados = pd.get_dummies(dados_cat, prefix=dados_cat_rotulos, dummy_na=False, dtype=int)
# print(dados_cat_normalizados)

# 2.d Juntar os dados normalizados em um dataframe único (usar o método join do pandas)
dados_finais = dados_num_normalizados.join(dados_cat_normalizados)
# print(dados_finais)

# 3. Determinar o número ótimo de clusters (aula do dia 21/10)
distorcoes = []
K = range(1, 100)
for i in K:
    cluster_model = KMeans(n_clusters=i, random_state=42).fit(dados_atributos_b)
    distorcoes.append(
        sum(
            np.min(
                cdist(dados_atributos_b, cluster_model.cluster_centers_, 'euclidean'), axis=1
            )/ dados_atributos_b.shape[0]
        )    
    )

x0 = K[0]
y0 = distorcoes[0]
xn = K[-1]
yn = distorcoes[-1]
distancias = []

for i in range(len(distorcoes)):
    x = K[i]
    y = distorcoes[i]
    # Fórmula corrigida
    numerador = abs((yn - y0) * x - (xn - x0) * y + xn * y0 - yn * x0)
    denominador = math.sqrt((yn - y0)**2 + (xn - x0)**2)
    distancias.append(numerador / denominador)

n_cluster_otimo = K[distancias.index(max(distancias))]
print("Número ótimo de clusters:", n_cluster_otimo)

# 4. Treinar o modelo de clusters com o Kmeans e salvar em disco com o pickle.dump (aula de 21/10)
fertility_cluster = KMeans(n_clusters=n_cluster_otimo, random_state=42).fit(dados_atributos_b)
dump(fertility_cluster, open('modelo_cluster.model.pkl', 'wb'))