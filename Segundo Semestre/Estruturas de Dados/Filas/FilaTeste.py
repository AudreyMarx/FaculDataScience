from collections import deque

fila = deque(["abacate", "bola", "cachorro"])
print(fila)
fila.append("dado")
print(fila)
fila.popleft()
print(fila)