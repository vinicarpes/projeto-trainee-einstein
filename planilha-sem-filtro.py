import pandas as pd #importando a biblioteca
#esse código mostra a planilha completa, não apenas os faltantes
planilhaProd = pd.read_csv('Planilha prod.csv').astype(str) #atribuindo a planilha à variável

#faltas_coluna = planilhaProd.iloc[:,2].astype(str) #atribuindo a coluna de faltas à variável e fazendo com que os dados sejam transformados em str

# id_alunos_coluna = planilhaProd.iloc[:, 1].astype(str) #atribuindo a coluna de faltas à variável e fazendo com que os dados sejam transformados em str

#print("Aqui coluna de faltas:\n", faltas_coluna) #EXIBINDO A COLUNA DE FALTAS

'''string_filtro = "True" #criando uma varável para filtrar a coluna

linhas_filtradas = planilhaProd.loc[faltas_coluna.str.contains(string_filtro)].astype(str) #nesta variável estou armazenando todas as colunas de cada linha em que a terceira célula seja igual a "True"'''
planilhaProd.columns =['Situação', 'Identificação do aluno', 'Faltou?', "Data", 'Turno'] #alterando os títulos das colunas
#print(linhas_filtradas) #exibindo a variável supracitada

'''id_alunos_filtradas = linhas_filtradas.iloc[:,1] #aqui armazeno todas as matrículas dos faltantes'''

#print(id_alunos_filtradas) #exibindo a matrícula dos faltantes

if not planilhaProd.empty: #verificando que não tenha posições vazias
    for index, row in planilhaProd.iterrows(): #laço for que pega o índice e dados de cada linha percorrida 
        if row["Situação"] == "atrasado":
            planilhaProd.at[index, "Situação"] = "Atrasado" 
        else:
            planilhaProd.at[index, "Situação"] = "Sem atraso"

if not planilhaProd.empty: #verificando que não tenha posições vazias
    for index, row in planilhaProd.iterrows():#laço for que pega o índice e dados de cada linha percorrida 
        if row["Faltou?"] == "True":
            planilhaProd.at[index, "Faltou?"] = "Sim" 
        else:
            planilhaProd.at[index, "Faltou?"] = "Não"
  

if not planilhaProd.empty: #verificando que não tenha posições vazias
    for index, row in planilhaProd.iterrows():#laço for que pega o índice e dados de cada linha percorrida 
        if row["Turno"] == "True":
            planilhaProd.at[index, "Turno"] = "17:45 - 20:00" 
        else: planilhaProd.at[index, "Turno"] = "20:15 - 22:00" 

#print(linhas_filtradas)

planilhaAlunos = pd.read_csv('ID Alunos.csv').astype(str)
#print(planilhaAlunos)

id_to_name = pd.Series(planilhaAlunos['nome'].values, index=planilhaAlunos["id"]).to_dict() #Criar um dicionário onde as chaves são os IDs dos alunos e os valores são os nomes dos alunos:
planilhaProd['Nome do Aluno'] = planilhaProd['Identificação do aluno'].map(id_to_name) 
#print(planilhaProd)

colunas_ordenadas = ['Data', 'Identificação do aluno', 'Nome do Aluno', 'Situação', 'Faltou?', 'Turno'] #criando uma variável com os valores dos títulos de linhas_filtradas
planilhaProd = planilhaProd[colunas_ordenadas] #trocando os valores das linhas de acordo com as posições colunas_ordenadas  

planilhaProd['Data'] = pd.to_datetime(planilhaProd['Data']) #convertendo os valores da coluna data para o formato de data +horário
planilhaProd['Data'] = planilhaProd['Data'].dt.strftime('%d/%m/%Y %H:%M')#formatando as ordens e quantidade de valores que aparecem

'''for index, row in planilhaProd.iterrows():
    if index <=1200:
        print(row)
    else:
        break'''

planilhaProd.to_csv('Planilha-presenca-dados-com-if.csv', sep=';', index=False, encoding='utf-8-sig')
#print(planilhaProd)


planilhaAlunos.columns = ["ID", 'Nome'] #alterando os valores das colunas da variável
planilhaAlunos['Frequência'] = "" #criando uma coluna vazia
planilhaAlunos['Total de aulas'] = ""
planilhaAlunos['Total de faltas'] = ""
#agora, quero gerar uma porcentagem relativa faltas/dias letivos
#para cada planilhaProd[Faltou?] = "Sim" contar +1 para cada ID

faltas = planilhaProd[planilhaProd["Faltou?"]=="Sim"] #filtrando as faltas e atribuindo a uma variavel
cont_faltas = faltas["Identificação do aluno"].value_counts() #cont_faltas armazena a ocorrência de cada ID 
faltas_por_alunos = cont_faltas.to_dict() #dicionário em que a chave é o ID e o valor é a ocorrência de faltas

planilhaAlunos["Frequência"] = planilhaAlunos["ID"].map(faltas_por_alunos).fillna(0).astype(int) #atribuindo à coluna frequencia os valores usando o dicionario para mapear os dados; preenchendo as linhas em que frequencia =0
'''
cont_id1 = planilhaProd[planilhaProd["Identificação do aluno"]!= 0] #filtrando os ids e atribuindo a uma variavel
cont_id = cont_id1["Identificação do aluno"].value_counts() #cont_id armazena a ocorrência de cada ID 
id_por_dias = cont_id.to_dict() #dicionário em que a chave é o ID e o valor é a ocorrência 

planilhaTeste = planilhaAlunos
planilhaTeste ["Ocorrência"]= planilhaTeste["ID"].map(id_por_dias)'''

total_de_aulas = round(len(planilhaProd)/118)

frequencia_alunos = round((total_de_aulas-planilhaAlunos['Frequência'])/total_de_aulas, 3)

planilhaAlunos['Frequência'] = frequencia_alunos
planilhaAlunos['Total de aulas'] = total_de_aulas
planilhaAlunos['Total de faltas'] = planilhaAlunos["ID"].map(faltas_por_alunos).fillna(0).astype(int)
planilhaAlunos.to_csv('Frequência-dos-alunos.csv', sep =';', index=False, encoding='utf-8-sig')
#print(planilhaAlunos)