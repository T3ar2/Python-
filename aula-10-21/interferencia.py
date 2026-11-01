# receber um novo paciente e determinar a qual cluster ele pertence

novo_paciente = [-1,0.53,1,1,1,0,0.8,1,0.5]


# carregar o modelo

from pickle import load
fertility_cluster = load(open('fertility_cluster.model', 'rb'))

cluster_do_paciente = fertility_cluster.predict([novo_paciente])
print(f'O paciente pertence ao cluster: {cluster_do_paciente[0]}')