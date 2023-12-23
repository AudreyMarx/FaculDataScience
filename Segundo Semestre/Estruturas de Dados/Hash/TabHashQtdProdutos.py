import array as arr    #Biblioteca para tratar arrays

m = 15     #numero de indices no hash
hashtable = arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])    #inicialização da tabela como array de inteiros de 15 posições com 0

def hashfunct(v, mh):   #função hash usando método da divisão
    return v % mh
def insereTC(valor):    #incremento do valor do vetor na chave
    hashtable[hashfunct(valor,m)] += 1
def retornaV(valor):    #retorna o numero de produtos para determinada chave
    return hashtable[hashfunct(valor,m)]

#testes
print(hashtable)
print()
print("Digite o numero da etiqueta com 10 algarismos")
x = int(input())
insereTC(x)
print()
print("Tabela atualizada")
print(hashtable)
print("Digite uma etiqueta para buscar quantidade")
x = int(input())
print()
print(retornaV(x))