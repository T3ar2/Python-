# =============================================================================
# MÓDULO DE INFERÊNCIA
# Usa os modelos gerados pelo módulo de treinamento:
#   - modelo_normalizador.pkl    (MinMaxScaler já treinado)
#   - modeloHousing_cluster.pkl  (KMeans já treinado)
# =============================================================================
from pickle import load

# Carregar os modelos salvos no treinamento
modelo_normalizador = load(open('modelo_normalizador.pkl', 'rb'))
novaInstancia = load(open('modeloHousing_cluster.pkl', 'rb'))  # modelo de cluster


# -----------------------------------------------------------------------------
# REQUISITO 1: Receber dados de uma nova residência
# Ordem dos atributos: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,
#                      PTRATIO, B, LSTAT, MEDV
# -----------------------------------------------------------------------------
nova_residencia = [[1.31842,0,8.14,0,0.538,5.63,96.4,3.8512,4,307,21,379.21,20.47,14.2]]


# -----------------------------------------------------------------------------
# REQUISITO 2: Normalizar os dados da nova residência
# Usa apenas transform, com o normalizador treinado (sem novo fit)
# -----------------------------------------------------------------------------
nova_residencia_normalizada = modelo_normalizador.transform(nova_residencia)


# -----------------------------------------------------------------------------
# REQUISITO 3: Inferir a qual grupo a nova residência pertence
# -----------------------------------------------------------------------------
numero_do_cluster = novaInstancia.predict(nova_residencia_normalizada)
print("A nova residência pertence ao grupo:", numero_do_cluster[0])


# -----------------------------------------------------------------------------
# REQUISITO 4: Exibir os dados desnormalizados do centroide inferido
# -----------------------------------------------------------------------------
centroide_normalizado = [novaInstancia.cluster_centers_[numero_do_cluster[0]]]

centroide_desnormalizado = modelo_normalizador.inverse_transform(centroide_normalizado)
print("As medidas reais do centroide deste grupo são:", centroide_desnormalizado[0])
