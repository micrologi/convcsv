from sys import argv
import sys
import os
import pandas as pd

print("")
print("CONVCSV versão 0.1.01 - by Marlon Andrei (marlon@micrologi.com.br)")
print("")
print("Conversor de planilhas em Excel (XLSX) para formato de arquivo CSV (americano), para importação nos Bancos de Dados Relacionais e outros fins.")
print("")

if len(argv) != 2:
    print("Utilize: convcsv planilha.xlsx")
    print("")
    sys.exit()
    
    
arqxls = argv[1]
if not os.path.isfile(arqxls):
    print("A planilha informada não existe. Verifique!")
    print("")
    sys.exit()
    
arqxls_name = os.path.basename(arqxls)


arqcsv = arqxls_name[0:(arqxls_name.find("."))] + ".csv"

df = pd.read_excel(arqxls)
print(df.head())   
print("")

df.to_csv(arqcsv, index=False, encoding="utf-8")

print("Arquivo convertido!")
print("")
