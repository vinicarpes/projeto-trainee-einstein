import pandas as pd #importando a biblioteca

planilhaProd = pd.read_csv('Planilha prod.csv').astype(str) #atribuindo a planilha à variável

planilhaProd.columns =['Situação', 'Identificação do aluno', 'Faltou?', "Data", 'Turno'] #alterando os títulos das colunas

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
#print(id_to_name)

planilhaProd['Nome do Aluno'] = planilhaProd['Identificação do aluno'].map(id_to_name) 
#print(planilhaProd)

colunas_ordenadas = ['Data', 'Identificação do aluno', 'Nome do Aluno', 'Situação', 'Faltou?', 'Turno'] #criando uma variável com os valores dos títulos de linhas_filtradas
planilhaProd = planilhaProd[colunas_ordenadas] #trocando os valores das linhas de acordo com as posições colunas_ordenadas  

planilhaProd['Data'] = pd.to_datetime(planilhaProd['Data']) #convertendo os valores da coluna data para o formato de data +horário
planilhaProd['Data'] = planilhaProd['Data'].dt.strftime('%d/%m/%Y')#formatando as ordens e quantidade de valores que aparecem

planilhaProd.to_csv('Planilha-presenca-dados-com-if.csv', sep=';', index=False, encoding='utf-8-sig')
#print(planilhaProd)


planilhaAlunos.columns = ["ID", 'Nome'] #alterando os valores das colunas da variável
planilhaAlunos['Frequência (%)'] = "" #criando uma coluna vazia
planilhaAlunos['Total de aulas'] = ""
planilhaAlunos['Total de faltas'] = ""
#agora, quero gerar uma porcentagem relativa faltas/dias letivos
#para cada planilhaProd[Faltou?] = "Sim" contar +1 para cada ID


ocorrencia_data= set()
for i in range(planilhaProd.shape[0]): 
    ocorrencia_data.add(planilhaProd.iloc[i,0])
print(len(ocorrencia_data))

quantidade_aulas = len(ocorrencia_data)*2
print(quantidade_aulas)

faltas = planilhaProd[planilhaProd['Faltou?']=="Sim"]

# Criar um dicionário onde as chaves são os IDs dos alunos e os valores são as quantidades de faltas
quantidade_faltas = faltas['Identificação do aluno'].value_counts().to_dict()

planilhaAlunos['Total de aulas'] = quantidade_aulas
# Mapear o número de faltas para os alunos em planilhaAlunos
planilhaAlunos['Total de faltas'] = planilhaAlunos["ID"].map(quantidade_faltas).fillna(0).astype(int)

planilhaAlunos['Frequência (%)'] = (((planilhaAlunos['Total de aulas']-planilhaAlunos['Total de faltas'])/planilhaAlunos['Total de aulas'])* 100).round(2)

#Agrupa as faltas por "Identificação do aluno" e cria uma lista de datas para cada aluno, armazenando o resultado em um dicionário datas_faltas.
datas_faltas = faltas.groupby('Identificação do aluno')['Data'].apply(list).to_dict()
turnos_faltas = faltas.groupby("Identificação do aluno")['Turno'].apply(list).to_dict() 

colunas_ordenadas = [ "ID", 'Nome', 'Total de aulas', 'Total de faltas', 'Frequência (%)']
planilhaAlunos=planilhaAlunos[colunas_ordenadas]

max_faltas = max(map(len, datas_faltas.values())) if datas_faltas else 0
for i in range(max_faltas):
    planilhaAlunos[f'Falta {i + 1}'] = planilhaAlunos["ID"].map(lambda x: datas_faltas.get(x, [])[i] if len(datas_faltas.get(x, [])) > i else '') + " " + planilhaAlunos["ID"].map(lambda x: turnos_faltas.get(x, [])[i] if len(turnos_faltas.get(x, []))> i else "")
print(planilhaAlunos)

planilhaAlunos.to_csv('Frequência-dos-alunos.csv', sep =';', index=False, encoding='utf-8-sig')