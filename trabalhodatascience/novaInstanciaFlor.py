from pickle import load

modelo_normalizador = load(open('modelo_normalizador.pkl', 'rb'))
novaInstanciaFlor = load(open('modelo_cluster.model.pkl', 'rb'))

nova_flor = [[5.2, 3.4, 1.6, 0.2]] 

# 5.e Normalizar a nova instância
nova_flor_normalizada = modelo_normalizador.transform(nova_flor)

# 5.f Usar o método predict 
numero_do_cluster = novaInstanciaFlor.predict(nova_flor_normalizada)

# 5.g Desnormalizar o centroide
centroide_normalizado = [novaInstanciaFlor.cluster_centers_[numero_do_cluster[0]]]

# Desnormalizar usando inverse_transform
centroide_desnormalizado = modelo_normalizador.inverse_transform(centroide_normalizado)
print("As medidas reais do centroide deste grupo são:", centroide_desnormalizado[0])