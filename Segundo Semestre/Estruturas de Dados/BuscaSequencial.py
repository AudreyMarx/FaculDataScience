x = [3, 2, 4, 5, 9]
def buscaSeq(x, elem):
    n = len(x)
    for i in range(0,n):
        if x[i] == elem:
            return 1
        return 0

buscaSeq()