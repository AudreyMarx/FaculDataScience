class VerticeAVL:
    def __init__(self, chave, pai = None):
        self.chave = chave
        self.pai = pai
        self.esquerdo = None
        self.direito = None
        self._altura = 0
    def inserir(self, chave_nova):
        print("Inserir{} (atual={})".format(chave_nova, self.chave))
        if chave_nova == self.chave:
            return self       
        raiz_da_subarvore = self
        if chave_nova < self.chave:    #é menor, procura lado esquerdo
            if self.esquerdo:   #já tem filho no lado esquerdo, continua a procurar
                raiz_da_subarvore = self.esquerdo.inserir(chave_nova)
            else:   #não tem filho no lado esquerdo
                self.esquerdo = VerticeAVL(chave_nova, self)    #cria o vertice e o atribui como filho
        elif chave_nova > self.chave:   #é maior, procura na subarvore direita
            if self.direito:    #já tem filho na subarvore direita, continua a procurar
                raiz_da_subarvore = self.direito.inserir(chave_nova)
            else:   #não tem filho na subarvore direita
                self.direito = VerticeAVL(chave_nova, self)    #cria o vertice e o atribui como filho
        #depois de inserir o filho, seja na subarvore direita ou esquerda
        raiz_da_subarvore.atualizar_altura()    #atualizar a altura do vertice atual (raiz_da_subarvore)
        raiz_da_subarvore = raiz_da_subarvore.balancear()   #balancear
        return raiz_da_subarvore.pai or raiz_da_subarvore
    def remover(self, chave):
        print("Remover {} (chave atual: {})".format(chave, self.chave))
        if self.chave == chave:
            print()
    
    @property
    def altura(self):
        return self._altura
    @property   #permite chamar a função como um atributo
    def altura_esquerda(self):
        if self.esquerdo:
            return self.esquerdo.altura
        return -1
    @property
    def altura_direita(self):
        if self.direito:
            return self.direito.altura
        return -1
    def atualizar_altura(self):    #pega a maior altura entre duas subarvores e soma 1
        self._altura = 1 + max([self.altura_esquerda, self.altura_direita])
    def balancear(self):
        fb = self.fator_de_balanceamento
        print("fb({})={}".format(self.chave, fb))
        if fb == 2:
            return self._balancear_subarvore_direita()
        if fb == -2:
            return self._balancear_subarvore_esquerda()
        return self
    def _balancear_subarvore_direita(self):    #resolve os casos RR e RL
        print("Balançear subarvore direita de {}".format(self.chave))
        if self.direito.fator_de_balanceamento == 1:    #caso RL: aplicar rotação do filho direito para direita
            #para ficar com a configuração do Caso RR
            print("Caso RL: Rotação de {} à direita + Rotação de {} à esquerda".format(
                  str(self.direito), self.chave))
            self.direito._rotacao_para_direita()
        #caso RR: aplicar rotação para esquerda
        nova_raiz = self._rotacao_para_esquerda()
        return nova_raiz
    def balancear_subarvore_esquerda(self):    #resolve os casos LL e LR
        print("Balançear subarvore esquerda e {}".format(self.chave))
        if self.esquerdo.fator_de_balanceamento == 1:   #Caso LR: aplicar rotação do filho esquerdo para esquerda
            #para ficar com a configuração do caso LL
            print("Caso LR: Rotação de {} à esquerda + Rotação de {} à direita".format(
                str(self.esquerdo), self.chave))
            self.esquerdo._rotacao_para_esquerda()
        #caso LL: aplicar rotação direita
        nova_raiz = self._rotacao_para_direita()
        return nova_raiz
    def _rotacao_para_esquerda(self):
        """Caso RR (Right Right Case) - rotação unica
           Caso LR (Left Right Case) - primeira rotação"""
        self._rotacao_info("esquerda")
        #identifica os vertices envolvidos:
        #pai da subarvore, v1 (raiz da subarvore), v2 (nova raiz da subarvore) e s2
        raiz_da_subarvore = self
        pai_da_subarvore = raiz_da_subarvore.pai
        v1 = raiz_da_subarvore
        v2 = v1.direito
        s2 = v2.esquerdo
        #executa a rotação/atualiza os relacionamentos entre os vertices
        if pai_da_subarvore:
            if raiz_da_subarvore is pai_da_subarvore.direito:   #raiz da subarvore é filho direito
                pai_da_subarvore.direito = v2
            else:
                pai_da_subarvore.esquerdo = v2
        v1.pai = v2
        v1.direito = s2
        v2.pai = pai_da_subarvore
        v2.esquerdo = v1
        if s2:
            s2.pai = v1
        #atualizar alturas:
        v1.atualizar_altura()
        v2.atualizar_altura()
        self._rotacao_info("esquerda", v2)
        #retorna a nova raiz
        return v2
    def _rotacao_para_direita(self):
        """Caso LL (Left Left Case) - rotação unica
           Caso RL (Right Letf Case) - primeira rotação"""
        self._rotacao_info(sentido="direita")
        #identifica os vertices envolvidos
        raiz_da_subarvore = self
        v3 = raiz_da_subarvore
        pai_da_subarvore = raiz_da_subarvore.pai
        v2 = v3.esquerdo
        s3 = v2.direito
        #faz a rotação/atualiza os relacionamentos entre vertices
        if pai_da_subarvore:
            if raiz_da_subarvore is pai_da_subarvore.direito:
                pai_da_subarvore.direito = v2
            else:
                pai_da_subarvore.esquerdo = v2
        v2.pai = pai_da_subarvore
        v2.direito = v3
        v3.pai = v2
        v3.esquerdo = s3
        if s3:
            s3.pai = v3
        #atualizar alturas:
        v3.atualizar_altura()
        v2.atualizar_altura()
        self._rotacao_info("direita", v2)
        #retorna a nova raiz
        return v2
    



class ArvoreAVL:
    def __init__(self):
        self.raiz = None
    def inserir(self, chave):
        if self.raiz is None:  #arvore está vazia, cria primeiro vertice
            self.raiz = VerticeAVL(chave)
        else:   #arvore já tem vertices
            self.raiz = self.raiz.inserir(chave)    #executa 'self._raiz.inserir(chave)'
        self.raiz.imprimir()
    def remover(self, chave):
        if self._raiz is not None:
            #arvore não está vazia, então executa:
            self._raiz = self._raiz.remover(chave)
            self._raiz.imprimir()


arvore_avl = ArvoreAVL()
arvore_avl.inserir(50)
arvore_avl.inserir(60)
arvore_avl.inserir(70)