'''o que devo fazer: 
- lista de alunos que faltaram a primeira metade das aulas
- nome e matrícula de cada aluno na lista:
    se primeira metade == true e falta ==true exibir id_aluno
- lista de alunos que faltaram na segunda metade da aula
- nome e matrícula de cada aluno na lista:
    se primeira metade == false e falta == true exibir id_aluno
adc data em cada falta
'''

import pandas as pd #importando a biblioteca

planilhaProd = pd.read_csv('Planilha prod.csv') #atribuindo a planilha à variável

faltas_coluna = planilhaProd.iloc[:,2].astype(str) #atribuindo a coluna de faltas à variável e fazendo com que os dados sejam transformados em str

print(faltas_coluna) #EXIBINDO A COLUNA DE FALTAS

string_filtro = "True" #criando uma varável para filtrar a coluna

faltas_filtradas = faltas_coluna[faltas_coluna.str.contains(string_filtro)] #atribuindo À variável faltas_filtradas todos os valores que correspondem à variável string_filtro

print(faltas_filtradas) #exibindo as faltas