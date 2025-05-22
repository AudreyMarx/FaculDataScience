set.seed(42)    #comendo utilizado para fixar uma semente, oq permitira criar um mesmo conjunto ao
# rodar um codigo de geração de amostra aleatoria, como rno, rm, runif, rpois, rbin.

tempo_ate_trabalho = sample(runif(100, 15, 110), 46, replace=F) #utilizamos o sample() para aleatorizar uma amostra populacinal.
#o runif foi utilizado para criar um conjunto de dados aleatorios, seguindo uma distribuição uniforme,
# com 100 observações e amplitude de 15 minutos a 110 minutos.
head(tempo_ate_trabalho)