import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn import preprocessing
import math
from pickle import dump


# -----------------------------------------------------------------------------
# Carregar a base
# -----------------------------------------------------------------------------
dados = pd.read_csv('HousingData.csv', sep=',')

# Tratar valores ausentes (KMeans não aceita NaN): preenche com a mediana
medianas = dados.median()
dados = dados.fillna(medianas)


# -----------------------------------------------------------------------------
# REQUISITO 1: Normalizar a base com cuidado entre dados categóricos e
# quantitativos
#   - Quantitativos -> MinMaxScaler
#   - Categóricos   -> get_dummies (se existirem)
# Obs.: a HousingData não possui colunas categóricas, então todos os
# atributos são tratados como quantitativos.
# -----------------------------------------------------------------------------
dados_num = dados.select_dtypes(include='number')
dados_cat = dados.select_dtypes(exclude='number')

# Normalização dos dados quantitativos
normalizador = preprocessing.MinMaxScaler()
dados_num_normalizados = pd.DataFrame(
    normalizador.fit_transform(dados_num), columns=dados_num.columns
)

# Codificação dos dados categóricos (só se houver)
if dados_cat.empty:
    dados_normalizador = dados_num_normalizados
else:
    dados_cat_codificados = pd.get_dummies(dados_cat, dtype=int)
    dados_normalizador = dados_num_normalizados.join(dados_cat_codificados)

# Salvar o normalizador (já treinado) para uso no módulo de inferência
dump(normalizador, open('modelo_normalizador.pkl', 'wb'))


# -----------------------------------------------------------------------------
# REQUISITO 2: Não há necessidade de balancear a base
# (nenhuma etapa de balanceamento, como SMOTE, é aplicada)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# REQUISITO 3: Determinar o número ótimo de grupos com o método do cotovelo
# (distâncias)
#   - Distorção: distância média de cada ponto ao centróide mais próximo
#   - K ótimo: ponto da curva mais distante da reta que liga o primeiro
#     ao último ponto
# -----------------------------------------------------------------------------
distorcoes = []
K = range(1, 100)
for i in K:
    cluster_model = KMeans(n_clusters=i, random_state=42).fit(dados_normalizador)
    distorcoes.append(
        sum(
            np.min(
                cdist(dados_normalizador, cluster_model.cluster_centers_, 'euclidean'), axis=1
            ) / dados_normalizador.shape[0]
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
    numerador = abs((yn - y0) * x - (xn - x0) * y + xn * y0 - yn * x0)
    denominador = math.sqrt((yn - y0) ** 2 + (xn - x0) ** 2)
    distancias.append(numerador / denominador)

n_cluster_otimo = K[distancias.index(max(distancias))]
print("Número ótimo de clusters:", n_cluster_otimo)


# -----------------------------------------------------------------------------
# REQUISITO 4: Treinar e salvar o modelo
# -----------------------------------------------------------------------------
modelo_cluster = KMeans(n_clusters=n_cluster_otimo, random_state=42, n_init=10).fit(dados_normalizador)

dump(modelo_cluster, open('modeloHousing_cluster.pkl', 'wb'))
