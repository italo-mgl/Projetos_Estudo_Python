nome_arquivo = "Python_TeoMeWhy/historia_02.txt"

txt = " Esqueci o nome do arquivo de texto "

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)

######
arquivos = "Python_TeoMeWhy/dados.csv"

with open(arquivos) as open_file:
    lines = open_file.readlines()


######
for l in lines:
    print(l)

####

dados = dict()

chaves = lines[0].strip("\n").split(";")

for c in chaves:
    dados[c] = []

print(dados)

####

for l in lines [1:]:
    valores = l.strip("\n").split(";")
    print(valores)
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

print(dados)