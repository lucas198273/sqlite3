
import pandas as pd


#Criando um DataFrame a partir de um dicionario
data = {
    'Nome1 ':"MATHEUS",
    'Nome2 ': "JOAO",
    'Nome3 ':"MARCOS",
    'Nome4 ':"MATIAS",
    'Nome5 ':"MARCIA",
}
serie = pd.Series(data)   #Cria serie com dicionario
# df = pd.DataFrame(data)
print("QUANTIDADE DE LINHAS: ",serie.shape)
print("TIPO DE DADOS : ",serie.dtypes)
print("VALORES SAO UNICOS ? : ",serie.is_unique)
print("EXISTEM VALORES NULOS? : ",serie.hasnans)
print("QUANTIDADE DE VALORES EXISTENTES?  : ", serie.count)

lista_nome = 'LUIZ CARLOS MAICON PEDRO ANTONIO METHEU LUIZ'.split()
lista_idade = 25,45,45,8,5,6,9,8

print(pd.DataFrame(lista_nome,columns=['NOME']))
pd.DataFrame(lista_nome,columns=['NOME']) 
#OPERAÇÃO MANUAL PARA IMPRIMIR DATAFRAME

# ABAIXO : OPERAÇÃO GUARDADA EM UMA VARIAVEL , PARA EXIBIR ->  print(VARIAVEL)
tabela_idade =  pd.DataFrame(lista_idade,columns=['IDADE'])
print(pd.DataFrame(lista_nome,columns=['NOME']))
print(tabela_idade)

# caminho_html = 'logo_barbearia'

# tabela = pd.read_html(caminho_html)
# response = requests.get(caminho_html)

# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
# else:
#     print("Erro ao obter o conteúdo HTML da página")
# for indice, valor in enumerate(tabela):
#     print(f"TABELA {indice + 1} : ")
#     print(valor)
#     print('============')

#   Exercicio com tabela EXCEL
nova_linha = {
    "Data": "2023-08-27",
    "ID Loja": "Iguatemi Campinas ",
    "Produto": "Bermuda Papai noel",
    "Quantidade": 111,
    "Valor Unitário": 11,
    "Valor Final": 1111
}
tabela = pd.read_excel("Vendas.xlsx")
print(tabela)

# FATURAMENTO  TOTAL
faturamento_total = tabela["Valor Final"].sum()
                        # ["Coluna"]. comar
print("FATURAMENTO ANUAL:\n ",faturamento_total)

# FATURAMENTO POR LOJA
faturamento_por_loja = tabela[["ID Loja","Valor Final"]].groupby("ID Loja").sum()
                    # Da tabela , trabalhandondo com ('Id loja' , e 'valor final')
                    # agrupa pelo 'Id loja' somando seus itens
print("\n\n",faturamento_por_loja)
# FATURAMENTO POR PRODUTO
faturamento_por_produto = tabela[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print(faturamento_por_produto)
#Inserindo linha na tabela 
tabela = tabela.append(nova_linha, ignore_index=True)
print(tabela)


#  AUTOMAÇÃO EM PLANILHA DE EXCEL


# VISUALIZAR PAGINAS EXISTENTES



# CRIAR  UMA PAGINA


# Selecionando uma pagina


# Adding data rows to the sheet
