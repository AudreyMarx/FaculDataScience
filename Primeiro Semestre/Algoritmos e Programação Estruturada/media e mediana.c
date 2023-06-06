#include <stdio.h>
#define VET_TAM 6

float calcularMedia(float conjunto[], int tam) {
    float soma = 0.0, resultado = 0.0;
    for(int i = 0; i < tam; i++) {
        soma += conjunto[i];
    }
    resultado = soma / (float) tam;
    return resultado;
}

float calcularMediana(float conjunto[], int tam) {
    float resultado = 0.0;
    if (tam % 2 != 0) { // tam é impar
        resultado = conjunto[tam / 2];     
    } else {
        resultado = (conjunto[tam / 2] + conjunto[(tam / 2) - 1]) / 2;
    }
    return resultado;
}

int main(void){
    float vet[VET_TAM] = {1, 2, 3, 4, 5, 6};
    float media = calcularMedia(vet, VET_TAM);
    float mediana = calcularMediana(vet, VET_TAM);
    printf("\nMédia = %.2f", media);
    printf("\nMediana = %.2f", mediana);
}
