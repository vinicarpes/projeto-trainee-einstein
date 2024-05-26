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

# id_alunos_coluna = planilhaProd.iloc[:, 1].astype(str) #atribuindo a coluna de faltas à variável e fazendo com que os dados sejam transformados em str

#print("Aqui coluna de faltas:\n", faltas_coluna) #EXIBINDO A COLUNA DE FALTAS

string_filtro = "True" #criando uma varável para filtrar a coluna

linhas_filtradas = planilhaProd.loc[faltas_coluna.str.contains(string_filtro)] #nesta variável estou armazenando todas as colunas de cada linha em que a terceira célula seja igual a "True"

print(linhas_filtradas) #exibindo a variável supracitada

id_alunos_filtradas = linhas_filtradas.iloc[:,1] #aqui armazeno todas as matrículas dos faltantes

print(id_alunos_filtradas) #exibindo a matrícula dos faltantes

