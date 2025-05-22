class Item:    #insere um item em uma "lista"
    def __init__(self, valor = None, anterior = None):
        self.valor = valor
        self.anterior = anterior
    def __repr__(self):
        return "%s\n%s"% (self.valor, self.anterior)
class Pilha:
    def __init__(self):
        self.topo = None
    def __repr__(self):
        return "TOPO\n%s\nRODAPÉ" % (self.topo)
    def push(self, valor):
        item_novo = Item(valor)    #cria um novo objeto Item
        item_novo.anterior = self.topo  #o anterior passa a ser o antigo topo
        self.topo = item_novo   #o topo da pilha sempre passa a ser o item novo
    def pop(self):
        assert self.topo, "Erro: pilha vazia."  #verifica se o topo da pilha está vazio
        self.topo = self.topo.anterior   #modifica o valor do topo
    
def main():
    pilha = Pilha()    #cria novo objeto do tipo pilha
    pilha.push('a')    #adc itens
    pilha.push('b')
    pilha.push('c')
    pilha.push('d')
    print(pilha)
    print('\n')

    pilha.pop()
    pilha.pop()
    print(pilha)

if __name__ == "__main__":
    main()