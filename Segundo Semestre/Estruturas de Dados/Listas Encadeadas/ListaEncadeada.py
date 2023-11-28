#Código XX: Classe ItemLista

class ItemLista: #Representa cada item de uma lista encadeada
    def __init__(self, data = 0, nextItem = None):
        self.data = data
        self.nextItem = nextItem

    def __repr__(self):
        return '%s => %s' % (self.data, self.nextItem)

class ListaEncadeadaC: #Cria uma lista encadeada
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "%s" % (self.head)
    
    def insere(lista, data): 
        item = ItemLista(data) #Cria um objeto para armazenar um novo item da lista
        item.nextItem = lista.head #O head é apontado como proximo item
        lista.head = item #O item atual se torna o head