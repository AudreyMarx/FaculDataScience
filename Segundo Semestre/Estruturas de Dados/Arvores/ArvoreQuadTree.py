class QuadTree:
    def __init__(self, altura = None):
        self.NO = None
        self.NE = None
        self.SO = None
        self.SE = None
        self._altura = altura or 0
    def inserir_vertice(self, img):
        self.imagem_com_cores_mescladas = obter_imagem_com_cores_mescladas(img)
        imagem_dividida = dividir_em_4(img)
        if imagens_diferentes(imagem_dividida):
            h = self._altura + 1
            self.NO = QuadTree(h)
            self.NE = QuadTree(h)
            self.SO = QuadTree(h)
            self.SE = QuadTree(h)

            self.NO.inserir_vertice(imagem_dividida[0])
            self.NE.inserir_vertice(imagem_dividida[1])
            self.SO.inserir_vertice(imagem_dividida[2])
            self.SE.inserir_vertice(imagem_dividida[3])
        return self
    def obter_vertice(self, altura):
        if self.folha or self._altura == altura:
            return self.imagem_com_cores_mescladas
        return concatenar(
            self.NO.obter_vertice(altura),
            self.NE.obter_vertice(altura),
            self.SO.obter_vertice(altura),
            self.SE.obter_vertice(altura))
