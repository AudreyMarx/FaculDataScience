class NoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
def imprimir_arvore_binaria(no, prefixo="", direcao=""):
    if no is not None:
        # Imprime o valor do nó com a direção da aresta
        print(f"{prefixo}({direcao}) {no.valor}")

        # Chama recursivamente para a subárvore à esquerda
        imprimir_arvore_binaria(no.esquerda, prefixo + "│   ", "L")

        # Chama recursivamente para a subárvore à direita
        imprimir_arvore_binaria(no.direita, prefixo + "    ", "R")


# Exemplo de uma árvore binária
raiz = NoBinario(1)
raiz.esquerda = NoBinario(2)
raiz.direita = NoBinario(3)
raiz.esquerda.esquerda = NoBinario(4)
raiz.esquerda.direita = NoBinario(5)
raiz.direita.esquerda = NoBinario(6)
raiz.direita.direita = NoBinario(7)

imprimir_arvore_binaria(raiz)
