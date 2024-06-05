import pandas as pd #importando a biblioteca

planilhaProd = pd.read_csv('Planilha prod.csv') #atribuindo a planilha à variável

faltas_coluna = planilhaProd.iloc[:,2].astype(str) #atribuindo a coluna de faltas à variável e fazendo com que os dados sejam transformados em str

# id_alunos_coluna = planilhaProd.iloc[:, 1].astype(str) #atribuindo a coluna de faltas à variável e fazendo com que os dados sejam transformados em str

#print("Aqui coluna de faltas:\n", faltas_coluna) #EXIBINDO A COLUNA DE FALTAS

string_filtro = "True" #criando uma varável para filtrar a coluna

linhas_filtradas = planilhaProd.loc[faltas_coluna.str.contains(string_filtro)].astype(str) #nesta variável estou armazenando todas as colunas de cada linha em que a terceira célula seja igual a "True"
linhas_filtradas.columns =['Situação', 'Identificação do aluno', 'Faltou?', "Data", 'Turno'] #alterando os títulos das colunas
#print(linhas_filtradas) #exibindo a variável supracitada

id_alunos_filtradas = linhas_filtradas.iloc[:,1] #aqui armazeno todas as matrículas dos faltantes

#print(id_alunos_filtradas) #exibindo a matrícula dos faltantes

if not linhas_filtradas.empty: #verificando que não tenha posições vazias
    for index, row in linhas_filtradas.iterrows(): #laço for que pega o índice e dados de cada linha percorrida 
        if row["Situação"] == "atrasado":
            linhas_filtradas.at[index, "Situação"] = "Atrasado" 

if not linhas_filtradas.empty: #verificando que não tenha posições vazias
    for index, row in linhas_filtradas.iterrows():#laço for que pega o índice e dados de cada linha percorrida 
        if row["Faltou?"] == "True":
            linhas_filtradas.at[index, "Faltou?"] = "Sim" 
  

if not linhas_filtradas.empty: #verificando que não tenha posições vazias
    for index, row in linhas_filtradas.iterrows():#laço for que pega o índice e dados de cada linha percorrida 
        if row["Turno"] == "True":
            linhas_filtradas.at[index, "Turno"] = "17:45 - 20:00" 
        else: linhas_filtradas.at[index, "Turno"] = "20:15 - 22:00" 

#print(linhas_filtradas)

planilhaAlunos = pd.read_csv('ID Alunos.csv').astype(str)
#print(planilhaAlunos)

id_to_name = pd.Series(planilhaAlunos['nome'].values, index=planilhaAlunos["id"]).to_dict() #Criar um dicionário onde as chaves são os IDs dos alunos e os valores são os nomes dos alunos:
linhas_filtradas['Nome do Aluno'] = linhas_filtradas['Identificação do aluno'].map(id_to_name) 
print(linhas_filtradas)

linhas_filtradas['Frequência'] = 'teste'

colunas_ordenadas = ['Data', 'Identificação do aluno', 'Frequência', 'Nome do Aluno', 'Situação', 'Faltou?', 'Turno'] #criando uma variável com os valores dos títulos de linhas_filtradas
linhas_filtradas = linhas_filtradas[colunas_ordenadas] #trocando os valores das linhas de acordo com as posições colunas_ordenadas  

linhas_filtradas['Data'] = pd.to_datetime(linhas_filtradas['Data']) #convertendo os valores da coluna data para o formato de data +horário
linhas_filtradas['Data'] = linhas_filtradas['Data'].dt.strftime('%d - %m - %Y %H:%M:%S')#formatando as ordens e quantidade de valores que aparecem

print(linhas_filtradas)

linhas_filtradas.to_csv('Planilha-linhas-filtradas.csv',sep=';', index=False, encoding='utf-8-sig')