class Item:    #insere um item em uma lista
    def __init__(self, valor = None, proximo = None):
        self.valor = valor
        self.proximo = proximo
    def __repr__(self):
        return "%s, %s" % (self.valor, self.proximo)
class Fila:    #constroi uma fila usando listas encadeadas
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def __repr__(self):
        return str(self.primeiro)
    def push(self, valor):  #adc itens na fila
        item = Item(valor)

        if self.primeiro:   #verifica se existe um item na fila
            #o valor proximo do ultimo item atual recebe o valor atual de
            self.ultimo.proximo = item
            self.ultimo = item #todo objeto item recebe o item a?
        else: #se a fila estiver vazia
            self.primeiro = item    #o item atual se torna o primeiro item
            self.ultimo = item      #o item atual tambem se torna o ultimo item
    def pop(self):  #remove itens da fila
        self.primeiro = self.primeiro.proximo
def main():
    fila = Fila()   #instancia uma nova fila

    fila.push(1) #adc itens
    fila.push(2)
    fila.push(3)
    print(fila)
    fila.pop()  #removendo itens
    print(fila)
    fila.pop()
    print(fila)
if __name__ == '__main__':
    main()