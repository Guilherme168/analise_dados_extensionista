import pandas as pd

#trazer os dados brutos obtidos através da pesquisa
dados = [
    ["Maria dos Santos Alves", 42, "Feminino", "Estudante", "Fundamental Incompleto", "Sim", "Celular", "Diária", "Básico"],
    ["João Pereira Alvares", 58, "Masculino", "Estudante", "Médio Incompleto", "Não", "Nenhum", "Nunca", "Nenhum"],
    ["Ana Lima Sousa", 41, "Feminino", "Professora", "Superior", "Sim", "Computador", "Diária", "Intermediário"],
    ["Pedro Souza", 45, "Masculino", "Estudante", "Médio Completo", "Sim", "Celular", "Semanal", "Básico"],
    ["Fátima da Silva Santos ", 61, "Feminino", "Estudante", "Fundamental Completo", "Não", "Nenhum", "Nunca", "Nenhum"],
    ["Rafael Rocha", 39, "Masculino", "Técnico", "Técnico Completo", "Sim", "Computador", "Diária", "Avançado"],
    ["Lucimara Alves", 49, "Feminino", "Diarista", "Médio Incompleto", "Sim", "Computador", "Diária", "Básico"],
    ["Vicente Silva", 52, "Masculino", "Estudante", "Médio Completo", "Sim", "Celular", "Semanal", "Básico"],
    ["José Antônio", 66, "Masculino", "Estudante", "Fundamental Incompleto", "Não", "Nenhum", "Nunca", "Nenhum"],
    ["Helena Costa", 48, "Feminino", "Estudante", "Médio Incompleto", "Sim", "Celular", "Diária", "Intermediário"],
    ["Tiago Nunes Pereira", 40, "Masculino", "Professor", "Superior", "Sim", "Computador", "Diária", "Intermediário"],
    ["Joselma Ramos da Costa", 59, "Feminino", "Estudante", "Médio Completo", "Sim", "Celular", "Semanal", "Básico"],
    ["Roberto Lima", 41, "Masculino", "Estudante", "Médio Incompleto", "Sim", "Celular", "Diária", "Básico"],
    ["Sandra Ferreira", 65, "Feminino", "Estudante", "Fundamental Completo", "Não", "Nenhum", "Nunca", "Nenhum"],
    ["Cícero Martins Santos", 38, "Masculino", "Promotor", "Superior", "Sim", "Computador", "Diária", "Avançado"],
    ["Sônia Rodrigues dos Santos", 48, "Feminino", "Estudante", "Médio Incompleto", "Sim", "Celular", "Diária", "Básico"],
    ["Dália Machado de Oliveira", 37, "Feminino", "Repositor", "Superior", "Sim", "Computador", "Diária", "Avançado"],
    ["Ernesto Monteiro ", 53, "Masculino", "Motorista", "Médio Incompleto", "Sim", "Celular", "Diária", "Intermediário"],
    ["Eliza Muniz", 45, "Feminino", "Promotora", "Médio Incompleto", "Sim", "Celular", "Diária", "Básico"],
    ["Pedro Luiz Viana da Silva ", 49, "Masculino", "Empreendedor", "Médio incompleto", "Sim", "Computador", "Diária", "Básico"],
    ["Jorge Cruz", 62, "Masculino", "Estudante", "Fundamental Completo", "Sim", "Celular", "Diária", "Básico"],
    ["Mirna Amaral ", 54, "Feminino", "Autônoma", "Médio Incompleto", "Sim", "Celular", "Diária", "Básico"],
    ["Samara Agostinho ", 60, "Feminino", "Estudante", "Fundamental Incompleto", "Não", "Nenhum", "Nunca", "Básico"]
]

#trazer as respectivas colunas
colunas = [
    "Nome", "Idade", "Gênero", "Cargo", "Escolaridade", "Acesso à Internet",
    "Dispositivo Principal", "Frequência de Uso", "Nível de Conhecimento"
]
#organizar tudo em um data frame
df = pd.DataFrame(dados, columns=colunas)

#organizar homens e mulheres em data frames diferentes
df_feminino = df.loc[df["Gênero"]== "Feminino"]
df_masculino = df.loc[df["Gênero"]== "Masculino"]

#salvar data frames em csv ou excel

#df.to_csv("pesquisa_tecnologia_comunidade_iso.csv", encoding= "ISO-8859-1", sep= ";")
df.to_excel("pesquisa_tecnologia_comunidade.xlsx", sheet_name= 'PESQUISA COMUNIDADE')
#df_feminino.to_csv("pesquisa_comunidade_mulheres.csv", index=False)
df_feminino.to_excel("pesquisa_comunidade_mulheres.xlsx", sheet_name= 'MULHERES')
#df_masculino.to_csv("pesquisa_comunidade_homens.csv", index=False)
df_masculino.to_excel("pesquisa_comunidade_homens.xlsx", sheet_name= 'HOMENS')



#algumas pesquisas com filtros

#saber a quantidade de pessoas que não tem acesso a internet apenas pelo nome
colunas_filter = [
    "Nome", "Acesso à Internet"
]

df_acesso = df.filter(items= colunas_filter)
df_acesso = df_acesso.rename(columns= {"Acesso à Internet" : "Internet"})
df_sem_internet = df_acesso.loc[df_acesso["Internet"]== "Não"]
#print(df_sem_internet)

#saber a quantidade de pessoas que tem acesso a internet apenas pelo nome
df_com_internet = df_acesso.loc[df_acesso["Internet"]== "Sim"]
#print(df_com_internet)

#saber a quantidade de homens com acesso a internet
colunas_filter_genero = colunas_filter.copy()
colunas_filter_genero.append("Gênero")
df_internet_genero = df.filter(items= colunas_filter_genero)
df_internet_genero = df_internet_genero.rename(columns= {"Acesso à Internet" : "Internet"})
df_homens = df_internet_genero.loc[df_internet_genero["Gênero"] == "Masculino"]
df_internet_homens = df_homens.loc[df_homens["Internet"]== "Sim"]
#print(df_internet_homens)

#saber a quantidade de mulheres com acesso a internet
df_mulheres = df_internet_genero.loc[df_internet_genero["Gênero"] == "Feminino"]
df_internet_mulheres = df_mulheres.loc[df_mulheres["Internet"]== "Sim"]

#descobrir a maior idade
colunas_filter.append("Idade")
df_idade_internet = df.filter(items= colunas_filter)
#print(df_idade_internet["Idade"].max())

#descobrir a menor idade
colunas_filter.append("Idade")
df_idade_internet = df.filter(items= colunas_filter)
#print(df_idade_internet["Idade"].min())

#descobrir a idade da pessoa mais velha que não tem acesso à internet
df_sem_internet = df.filter(items=colunas_filter)
df_sem_internet = df_sem_internet.loc[df_sem_internet["Acesso à Internet"] == "Não"]
#print(df_sem_internet["Idade"].max())


#media das idades geral
#print((df["Idade"].sum()) // len(df["Idade"]))

#media das idades dos homens
colunas_filter_genero.append("Idade")
df_homens = df.filter(items= colunas_filter_genero)
df_homens = df_homens.loc[df_homens["Gênero"] == "Masculino"]
#print((df_homens["Idade"].sum()) // len(df_homens["Idade"]))

#media das idades das mulheres
df_mulheres = df.filter(items=colunas_filter_genero)
df_mulheres = df_mulheres.loc[df_mulheres["Gênero"] == "Feminino"]
#print((df_mulheres["Idade"].sum()) // len(df_mulheres["Idade"]))