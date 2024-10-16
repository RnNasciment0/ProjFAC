from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

from sklearn import metrics

import pandas as pd

from sklearn import tree

import entrada_app as app

# Tratamento de dados

# nomes das colunas








col_names = ['febre alta', 'nauseas', 'vomitos', 'dor de cabeça', 'dor atrás dos olhos', 'manchas vermelhas na pele',
             'mau estar geral', 'cansaço excessivo', 'tem dengue']

# Entrada da base de dados, sem a base de dados o algoritmo é inútil

bd = pd.read_csv('dengue 2.0.csv', header=None, names=col_names)

# variáveis que representarão as entradas
colunas_ent = ['febre alta', 'nauseas', 'vomitos', 'dor de cabeça', 'dor atrás dos olhos', 'manchas vermelhas na pele',
               ' mau estar geral', 'cansaço excessivo']

# Substituindo, Sim, por 1 e Não por 0, pois o modelo não trabalha com ‘strings’ apenas com números (é um modelo matemático)
bd = bd.replace(['Sim', 'Nao'], [1, 0])

# valores das variáveis de entrada
X = bd[colunas_ent]

# valores das variáveis de saída
Y = bd['tem dengue']

# montagem do algoritmo é necessário haver uma base de treino e teste para o modelo funcionar
# 70% dos dados são utilizados para treinar o modelo (escolhidos aleatóriamente)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# biblioteca que faz a árvore de decisão
dec = DecisionTreeClassifier()
# treinamento do modelo
dec = dec.fit(X_train, y_train)
# resultado do treino, não precisa mostrar, mas sem ele o algoritmo também não aprende
y_train_pred = dec.predict(X_train)

# gera uma lista contendo as respostas do usuário Sim ou Não para cada pergunta

# App_test é a entrada dos dados do usuário
App_test = app.gera_vetor(8)

# formando um dataframe com a lista para fazer o tratamento dos dados
App_test = [App_test]
df = pd.DataFrame(App_test, columns=colunas_ent)

# tratamento dos dados gerados das respostas do usuário
df = df.replace(['Sim', 'Nao'], [1, 0])
# algoritmo definindo se a pessoa deve ou não ir ao hospital (saída)
y_pred = dec.predict(df)

# a pessoa deve ir ao médico?
if y_pred == 1:
    print('Procure um médico')
else:
    print('Não é necessário')
