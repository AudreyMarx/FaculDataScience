import ListaEncadeada as le

lista = le.ListaEncadeadaC() #Cria o objeto

le.ListaEncadeadaC.insere(lista, "abacate")
le.ListaEncadeadaC.insere(lista, "biscoito")
le.ListaEncadeadaC.insere(lista, "cenoura")
le.ListaEncadeadaC.insere(lista, "desodorante")
le.ListaEncadeadaC.insere(lista, "espinafre")
print(lista)

query = "cenoura"
item_buscado = le.ListaEncadeadaC.busca(lista, query)
if item_buscado:
    print("Elemento encontrado")
else:
    print("Elemento NÃO encontrado")

le.ListaEncadeadaC.remove(lista, "cenoura")
print(lista)