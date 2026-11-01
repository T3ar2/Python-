import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pickle import dump 
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from collections import Counter
from imblearn.over_sampling import SMOTE

# 1. Carregar os dados
dados = pd.read_csv('fertility_Diagnosis.csv', sep=',')

# 2. Balancear os dados
Counter(dados['Diagnostico'])

# Instanciar o objeto balanceador
resampler = SMOTE()

# Separar os dados em atributos e classes 
dados_atributos = dados.drop(columns=['Diagnostico'])
dados_classes = dados['Diagnostico']

# Aplicar o balanceamento
dados_atribuidos_b, dados_classes_b = resampler.fit_resample(dados_atributos, dados_classes)

# Juntar os objetos de dados pós-balanceamento
dados = dados_atribuidos_b.join(dados_classes_b)

# 3. Descobrir o numero ideal de clusters (Grupos)
# HIPERPARAMETRIZAÇÃO
distorcoes = [] # matriz para conter as distorções calculadas 
k = range(1, 100) # intervalo de clusters a serem testados

for i in k:
    cluster_model = KMeans(n_clusters=i, random_state=42).fit(dados_atribuidos_b)
    distorcoes.append(
        sum(
            np.min(
                cdist(dados_atribuidos_b, cluster_model.cluster_centers_, 'euclidean'), 
                axis=1
            )
        ) / dados_atribuidos_b.shape[0]
    )

# 4. Determinar o número ideal de clusters (Método do cotovelo/elbow)
x0 = k[0] 
y0 = distorcoes[0]
xn = k[-1]
yn = distorcoes[-1]
distancias = []

for i in range(len(distorcoes)):
    x = k[i]
    y = distorcoes[i]
    numerador = abs((yn - y0) * x - (xn - x0) * y + xn * y0 - yn * x0)
    denominador = math.sqrt((yn - y0)**2 + (xn - x0)**2)
    distancias.append(numerador / denominador)

n_clusters_otimo = k[distancias.index(max(distancias))]

# 5. Treinamento definitivo
fertility_cluster = KMeans(n_clusters=n_clusters_otimo, random_state=42).fit(dados_atribuidos_b)

# 6. Salvar o modelo para uso futuro
dump(fertility_cluster, open('fertility_cluster.model', 'wb'))