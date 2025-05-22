class Vertice:
    """Vertice de Arvore Binária de Busca"""
    def __init__(self, chave, pai=None):        
        self.chave = chave  # será usada na busca        
        self.pai = pai  # vértice pai        
        self.menor = None   # filho menor (à esquerda) 
        self.maior = None   #e maior (à direita)
    def __str__(self):
        return str(self.chave)
    def apresentar(self, num_espacos=0, sentido=""):
        espacos = " "*num_espacos
        if self.menor:
            self.menor.apresentar(num_espacos+10, sentido="/")
        print("{}{}----> [{}]".format(espacos, sentido, self.chave))
        if self.maior:
            self.maior.apresentar(num_espacos+10, sentido="\\")
    def representacao_com_parenteses(self):
        """Retorna a representação da árvore com aninhamento por parênteses
        :return: (str)"""
        dir = esq = ""
        if self.menor:           
            esq = self.menor.representacao_com_parenteses()    # recursividade
        if self.maior:            
            dir = self.maior.representacao_com_parenteses()    # recursividade
        return "({}{}{})".format(str(self), esq, dir)
    def representacao_com_recuo(self, numero_de_espacos=0):
        """Retorna a representação da árvore com recuo
        :return: (str)"""
        esq = dir = ""
        if self.menor:
            esq = self.menor.representacao_com_recuo(numero_de_espacos + 4)
        if self.maior:
            dir = self.maior.representacao_com_recuo(numero_de_espacos + 4)
        return "{esq}{espacos}{self}\n{dir}".format(espacos=' '*numero_de_espacos, self=str(self), esq=esq, dir=dir,)
    def inserir(self, chave_nova):
        """Executa a inserção
        :param chave_nova: chave da chave a ser inserido
        :return: vértice inserido"""
        print("Inserir {} (chave atual: {})".format(chave_nova, self.chave))
        if chave_nova < self.chave:    # é menor, procura no lado esquerdo            
            if self.menor:
                print("Inserir {} no lado menor".format(chave_nova))
                return self.menor.inserir(chave_nova)            
            self.menor = Vertice(chave_nova, self)   # cria Vertice no lado menor         
            return self.menor   # retorna vertice criado
        elif chave_nova > self.chave:   # é maior, procura no lado direito            
            if self.maior:
                print("Inserir {} no lado maior".format(chave_nova))
                return self.maior.inserir(chave_nova)
            self.maior = Vertice(chave_nova, self)  # cria Vertice no lado maior e o retorna           
            return self.maior   # retorna vertice criado
        else:            
            return self    # encontrou, retorna o próprio, não faz inserção
    def _remover_folha(self):
        """Remove o vértice folha
        :return: vértice removido"""        
        print("Remover FOLHA. Sou folha")
        if self.pai:    # tem pai, então não sou a raiz            
            if self.pai.menor is self:                
                self.pai.menor = None   # sou filho da esquerda, me desvincula da esquerda
            else:                
                self.pai.maior = None    # sou filho da direita, me desvincula da direita
            self.pai = None     # me desvinculo do meu pai 
        return self    # retorna o vértice removido
    def _remover_pai_de_um_filho(self): 
        """Remove o vértice que tem um filho seja à direita ou à esquerda
        :return: vértice removido"""       
        print("Remover PAI de 1 filho. Sou pai de 1 filho")
        meu_pai = self.pai  # identifico meu pai       
        meu_filho = self.menor or self.maior    # tenho só 1 filho, identifico meu filho (esquerdo ou direito)
        if meu_pai is None:    # sou raiz, a árvore está apontando para mim,            
            # não posso ser removido
            # então, vou trocar de lugar com meu filho
            meu_filho.chave, self.chave = self.chave, meu_filho.chave
            # agora estou no lugar do meu filho e posso ser removido            
            return meu_filho.remover(meu_filho.chave)   # a recursividade tratará a forma como serei removido
        meu_filho.pai = meu_pai  #meu pai, é pai do meu filho
        # meu filho, passa a ser filho do meu pai
        if meu_pai.menor is self:
            # sou filho da direita
            meu_pai.menor = meu_filho   # meu filho passa a ser seu filho da direita
        else:
            # sou filho da esquerda            
            meu_pai.maior = meu_filho     # meu filho passa a ser seu filho da esquerda
        self.pai = None    # me desvinculo do meu pai e do meu filho
        self.menor = None
        self.maior = None
        return self
    def _remover_pai_de_dois_filhos(self):        
        """Remove o vértice que tem 2 filhos
        :return: vértice removido"""        
        print("Remover PAI de 2 filhos. Sou pai de 2 filhos")
        # sou pai de dois filhos
        # o filho que assume o lugar do pai é definido pelo usuário
        # neste caso será o vertice de menor valor       
        menor = self.maior.buscar_menor()   # obter o menor do lado menor 
        self.chave, menor.chave = menor.chave, self.chave   # troca valor da chave entre o nó atual e o menor        
        return menor.remover(menor.chave)   # remover o menor / recursividade
    def remover(self, chave):
        print("Remover {} (chave atual: {})".format(chave, self.chave))
        if chave < self.chave:
            # se menor existe, continua a busca pelo menor
            # senão a busca encerra e None é retornado
            return self.menor and self.menor.remover(chave)
        elif chave > self.chave:
            # se maior existe, continua a busca pelo maior
            # senão a busca encerra e None é retornado
            return self.maior and self.maior.remover(chave)
        else:
            if self.menor and self.maior:   # tem ambos filhos                
                return self._remover_pai_de_dois_filhos()
            if self.menor or self.maior:    # tem ou filho menor ou filho maior                
                return self._remover_pai_de_um_filho()            
            return self._remover_folha()    # nao tem filhos
    def imprimir_percurso_em_ordem(self):
        """Percorre a árvore em ordem simétrica (esquerda, vértice, direita) e imprime a chave do vértice
        :return: None"""        
        if self.menor:           
            self.menor.imprimir_percurso_em_ordem()    # recursividade: executa o mesmo atributo para seu filho esquerdo
        print(self) # imprime a chave do vértice
        if self.maior:            
            self.maior.imprimir_percurso_em_ordem()    # recursividade: executa o mesmo atributo para seu filho direito
    def imprimir_percurso_pre_ordem(self):
        """Percorre a árvore em pré ordem (vértice, esquerda, direita)e imprime a chave do vértice
        :return: None"""               
        print(self) # imprime a chave do vértice
        if self.menor:            
            self.menor.imprimir_percurso_pre_ordem()    # recursividade: executa o mesmo atributo para seu filho esquerdo
        if self.maior:            
            self.maior.imprimir_percurso_pre_ordem()    # recursividade: executa o mesmo atributo para seu filho direito

    def imprimir_percurso_pos_ordem(self):        
        """Percorre a árvore em pré ordem (esquerda, direita, vértice) e imprime a chave do vértice
        :return: None"""       
        if self.menor:            
            self.menor.imprimir_percurso_pos_ordem()    # recursividade: executa o mesmo atributo para seu filho esquerdo
        if self.maior:           
            self.maior.imprimir_percurso_pos_ordem()    # recursividade: executa o mesmo atributo para seu filho direito        
        print(self) # imprime a chave do vértice
    def buscar(self, chave_nova):
        print("")
        print("Procurando {}. Chave atual: {}".format(chave_nova, self.chave))
        if chave_nova < self.chave:
            return self.menor and self.menor.buscar(chave_nova)
        elif chave_nova > self.chave:
            return self.maior and self.maior.buscar(chave_nova)
        else:   # encontrou, retorna o próprio           
            return self
    def buscar_menor(self): 
        """Procura o menor até que não encontra e retorna ele mesmo"""               
        print("Procurar menor {}".format(self))
        if self.menor:
            # recursividade
            return self.menor.buscar_menor()
        return self
    def imprimir(self):  # 3 formas de apresentar a árvore como está neste momento       
        print("_"*20)
        print(self.representacao_com_parenteses())
        print("_"*20)
        print(self.representacao_com_recuo())
        print("_"*20)
        self.apresentar()
        print("_"*20)

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Vertice(chave)
        else:
            self.raiz.inserir(chave)
        self.raiz.imprimir()   
    def remover(self, chave):
        if self.raiz is not None:
            removido = self.raiz.remover(chave)
            if removido is self.raiz:
                self.raiz = None
        self.raiz.imprimir()

# Criação da árvore
arvore = ArvoreBinariaBusca()
arvore.inserir(14)
arvore.inserir(4)   # Inserção de 4
arvore.inserir(18)  # Inserção de 18
arvore.inserir(0)   # Inserção de 0
arvore.inserir(21)  # Inserção de 21
arvore.inserir(17)  # Inserção de 17
arvore.inserir(1)   # Inserção de 1
arvore.inserir(8)   # Inserção de 8
arvore.inserir(13)  # Inserção de 13 
arvore.remover(21)  # Remoção de 21, vertice folha
arvore.remover(0)   # Remoção de zero, vertice pai de 1 filho
arvore.remover(14)  # Remoção de 14, vertice pai de 2 filhos e arvore
arvore.remover(99999)
