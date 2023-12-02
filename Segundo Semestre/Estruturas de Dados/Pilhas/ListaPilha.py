class Pilha:
    def __init__(self):     #permite criar uma pilha
        self.itens = []
    def __repr__(self):
        return str(self.itens)
    
    def empilha(self, valor):
        self.itens.append(valor)    #adciona itens na pilha
    def desempilha(self):
        assert self.itens, "Erro: Pilha vazia"
        return self.itens.pop()     #modifica o valor do topo
    def busca(self, alvo):  #busca por um alvo na pilha
        while self.itens:   #enquanto houver itens na pilha
            atual =self.desempilha()    #desempilhe o ultimo item
            if atual == alvo:
                return True     #se sim, retorne verdade
            else:
                continue    #se não, reinicie o laço while
        return False    #caso os itens da pilha acabem, retorne falso

def main():
    familia = Pilha()   #cria um novo objeto do tipo pilha
    familia.empilha("Miguel Silva de Castro")
    familia.empilha("José de Castro")
    familia.empilha("Eugênio de Castro")
    familia.empilha("Pedro Paulo de Castro")

    alvo = "Miguel Silva de Castro"
    parentes = familia.busca(alvo)

    if parentes:
        print("São parentes")
    else:
        print("Não são parentes")
    
if __name__ == "__main__":
    main()