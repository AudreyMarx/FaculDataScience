setor = c('RH', 'Finanças', 'Serviços', 'Dados', "Outras")
total_funcionarios = c(6, 12, 20, 7, 6)
funcionarios_por_setor = data.frame(setor, total_funcionarios)
head(funcionarios_por_setor)

barplot(funcionarios_por_setor$total_funcionarios, main= "Gráfico de Barras do Número de Funcionários por Setor", ylab = "Frequência",
        names.arg = funcionarios_por_setor$setor, cex.axis = 0.6, cex.names = 0.7, cex.main=0.7, cexlab=0.8, las=2)
#dentro do comando barplot, temos alguns itens parametrizaveis, como o titulo do grafico (main), 
#o nome das variaveis no eixo x (names.arg), o nome dos eixos (ylab e xlab), e os tamanhos das fontes (cex)

hist(tempo_ate_trabalho, xlab = "Tempo em minutos", ylab = "Frequência", main ="Histograma do Tempo de Trajeto até o Trabalho",
    cex.axis=0.6, cex.main=0.4, cex.lab=0.8, las=2, col= "grey")    #da mesma forma que o biplot, o histograma permite parametrizar 
    #uma serie de componentes graficos