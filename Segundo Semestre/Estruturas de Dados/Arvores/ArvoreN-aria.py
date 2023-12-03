class NoNArio:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []
def imprimir_arvore_naria(no, prefixo="", direcao=""):
    if no is not None:        
        print(f"{prefixo}({direcao}) {no.valor}")   # Imprime o valor do nó com a direção da aresta        
        for i, filho in enumerate(no.filhos):   # Chama recursivamente para cada filho
            is_ultimo_filho = i == len(no.filhos) - 1
            novo_prefixo = prefixo + ("└── " if is_ultimo_filho else "├── ")
            nova_direcao = f"{i + 1}/{len(no.filhos)}"
            imprimir_arvore_naria(filho, novo_prefixo, nova_direcao)
# Exemplo de uma árvore n-ária
raiz_naria = NoNArio('A')
raiz_naria.filhos.append(NoNArio('B'))
raiz_naria.filhos.append(NoNArio('C'))
raiz_naria.filhos[0].filhos.append(NoNArio('D'))
raiz_naria.filhos[0].filhos.append(NoNArio('E'))
raiz_naria.filhos[1].filhos.append(NoNArio('F'))

imprimir_arvore_naria(raiz_naria)