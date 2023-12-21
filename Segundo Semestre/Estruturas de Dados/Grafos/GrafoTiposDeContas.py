import networkx as nx
import matplotlib.pyplot as plt

class visualizacaoGrafo:
    def __init__(self):
        self.visual = []
    def adcionaAresta(self, a, b):
        temp = [a, b] #armazena aresta temporária
        self.visual.append(temp) #insere na lista visual
    def desenhar(self):
        G = nx.Graph() #cria-se um grafo G
        G.add_edges_from(self.visual) #adiciona-se então a lista de arestas a G
        nx.draw_networkx(G, node_color='lightgrey') #executa-se a função de desenho
        plt.show() #o grafo é desenhado na tela

G = visualizacaoGrafo()
G.adcionaAresta('Pedro', 'CP')
G.adcionaAresta('Pedro', 'Carla')
G.adcionaAresta('Carla', 'CP')
G.adcionaAresta('João', 'CC')
G.adcionaAresta('Pedro', 'CC')
G.desenhar()