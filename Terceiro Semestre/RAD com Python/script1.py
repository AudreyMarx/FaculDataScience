"""Neste script contém exemplos de como abrir e fechar um arquivo, como obter
    o caminho relativo e absoluto, modos de acesso"""

import os

#Para o arquivo dados1.txt
arquivo1 = open("Terceiro Semestre\\RAD com Python\\dados1.txt", encoding='utf-8')   #caminho relativo?
arquivo2 = open("C:\\Users\\audrey\\OneDrive\\Área de Trabalho\\Facul DataScience\\Terceiro Semestre\\RAD com Python\\dados1.txt")    #caminho absoluto

#para o arquivo dados2.txt
arquivo3 = open("Terceiro Semestre\\RAD com Python\\documentos\\dados2.txt", "w+", encoding="utf-8")
arquivo4 = open("C:\\Users\\audrey\\OneDrive\\Área de Trabalho\\Facul DataScience\\Terceiro Semestre\\RAD com Python\\documentos\\dados2.txt")

#Aqui obtemos o caminho relativo e absoluto
print(os.path.relpath(arquivo1.name))   #caminho relativo
print(os.path.abspath(arquivo1.name))   #caminho absoluto

print(arquivo1)
conteudo = arquivo1.read()
print("Arquivo1: ",conteudo)
#Aqui verificamos o nome, modo e se o arquivo está fechado
print("Nome do arquivo1: ",arquivo1.name) 
print("Modo do arquivo1: ",arquivo1.mode)
print("Arquivo1 fechado? ",arquivo1.closed)

arquivo3.write("Testando o Olá, mundo!")
arquivo3.seek(0)  #Move o cursor de leitura para o início
conteudo2 = arquivo3.read()
print("Arquivo3: ", conteudo2)
print("Nome do arquivo3: ",arquivo3.name)   #Verifica o nome
print("Modo do arquivo3: ",arquivo3.mode)   #Verifica o modo de acesso
print("Arquivo3 fechado? ",arquivo3.closed) #Verifica se está fechado retornando True or False

arquivo1.close()
arquivo2.close()
arquivo3.close()
arquivo4.close()

print("Todos os arquivos fechados? ",arquivo1.closed, arquivo3.closed)

#Outra forma de exibir o caminho relativo e absoluto de um arquivo
relpath = os.path.relpath('dados1.txt')
abspath = os.path.abspath('dados1.txt')
print("Caminho relativo: ", relpath)
print("Caminho absoluto: ", abspath)