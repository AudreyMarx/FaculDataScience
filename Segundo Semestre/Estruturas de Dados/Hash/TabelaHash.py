hashtable = {}
m = 10    #numero de indices da tabela

def hashfunct(v, mh):     #função hash usando metodo da divisão
    return v % mh
for i in range (m):     #preenchendo indices da tabela
    hashtable[i] = ''
#inserindo numeros
hashtable[hashfunct(235,m)] = '235'
hashtable[hashfunct(578,m)] = '578'
hashtable[hashfunct(1024,m)] = '1024'
hashtable[hashfunct(96,m)] = '96'
hashtable[hashfunct(32,m)] = '32'
print(hashtable)
hashtable[hashfunct(18,m)] = '18'   #inserção sem tratamento de colisão
print(hashtable)

def insereTC(valor):
    if(hashtable[hashfunct(valor,m)] == ''):
        hashtable[hashfunct(valor,m)] = valor
    else:
        print("Colisão detectada, tratar colisão...")
for i in range (m):    #preenchendo indices da tabela
    hashtable[i] = ''
#inserindo numeros
insereTC(235)
insereTC(578)
insereTC(1024)
insereTC(96)
insereTC(32)
print(hashtable)
insereTC(18)    #inserção com tratamento de colisão
print(hashtable)
