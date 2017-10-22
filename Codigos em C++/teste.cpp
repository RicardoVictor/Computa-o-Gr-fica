#include <stdio.h> 
#include <cstdlib>
#include "Objeto.hpp"
#include "Cubo.hpp"

using namespace std;

int main(){
 
    Objeto *o1 = new Objeto();

    //o1->imprimeMatrizBase();
    //o1->espelhoXY();
    //o1->imprimeMatrizBase();
    //o1->espelhoYZ();
    //o1->imprimeMatrizBase();

    //o1->calculaNormal(0, 0, 4, 6, 0, 0, 0, 10, 0);
    //o1->imprimeNormal();
    //o1->normaliza();
    //o1->imprimeNormal();

    //o1->espelhoQualquer(0, 0, 4, 6, 0, 0, 0, 10, 0);

/*
    Teste 1
*/
/*
    //"criando" cubo
    o1->imprimeMatrizBase();
    o1->addVertice(1, 1, 0);
    //o1->addVertice(1, -1, 0);
    //o1->addVertice(-1, -1, 0);
    //o1->addVertice(-1, 1, 0);
    //o1->imprimeVertices();
    //rotacao de 45 graus
    o1->rotacaoZ(45);
    o1->imprimeMatrizBase();
    //o1->aplica();
    //o1->imprimeVertices();
    //translacao
    o1->translacao(6, 6, 0);
    //o1->translacao(-6, -6, 0);
    o1->imprimeMatrizBase();
    //espelho qualquer (30 graus quandrante 1)
    o1->espelhoQualquer(5, 2.886751, 0, 7, 4.041452, 0, 5, 2.886751, 2);
    o1->imprimeMatrizBase();
    //aplica em todos os pontos/vertices
    o1->aplica();
    o1->imprimeVertices();
*/

/*
    Teste 2
*/
/*
    //"criando" cubo
    o1->imprimeMatrizBase();
    o1->addVertice(1, 1, 0);
    o1->addVertice(1, -1, 0);
    o1->addVertice(-1, -1, 0);
    o1->addVertice(-1, 1, 0);
    //escala de 2 vezes
    o1->escala(2, 2, 1);
    o1->imprimeMatrizBase();
    //rotacao de 45
    o1->rotacaoZ(45);
    o1->imprimeMatrizBase();
    //escala 
    o1->escala(1, 0.5, 1);
    o1->imprimeMatrizBase();
    //rotacao 45
    o1->rotacaoZ(45);
    //translacao
    o1->translacao(8, 8, 0);
    o1->imprimeMatrizBase();
    //aplica em todos os pontos/vertices
    o1->aplica();
    o1->imprimeVertices();
*/

/*
    Teste 3
*/
    
    o1->addVertice(0, 0, 0);
    o1->addVertice(0, 0, 5);
    o1->addVertice(12, 0, 0);
    o1->addVertice(0, 8, 0);
    o1->imprimeVertices();
    //Questao 1
    //escala
    printf("\tQuestao 1\n");
    printf("matrizEscala\n");
    o1->escala(0.589256, 0.883883, 1.414213);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->inicializaMatrizBase();
    o1->imprimeVertices();
    //Questao 2
    printf("\tQuestao 2\n");
    printf("matrizTranslacao\n");
    o1->translacao(-7.071068, 0 , 0);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->inicializaMatrizBase();
    printf("matrizRotacaoY:135\n");
    o1->rotacaoY(135);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->inicializaMatrizBase();
    printf("matrizRotacaoX:-35.265\n");
    o1->rotacaoX(-35.265);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->inicializaMatrizBase();
    printf("matrizRotacaoZ:40\n");
    o1->rotacaoZ(40);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->inicializaMatrizBase();
    printf("matrizTranslacao\n");
    o1->translacao(60, 50, 0);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->imprimeVertices();
    o1->inicializaMatrizBase();
    //Questao 3
    printf("\tQuestao 3\n");
    printf("matrizTranslacao\n");
    o1->translacao(-67.660439, -56.427876, 0);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->imprimeVertices();
    o1->inicializaMatrizBase();
    o1->espelhoQualquer(-5.685814, -1.002525, 4.082452, 0, 0, 0, -9.396919, 3.420200, 0);
    o1->aplica();
    o1->imprimeVertices();
    o1->inicializaMatrizBase();
    printf("matrizTranslacao\n");
    o1->translacao(67.660439, 56.427876, 0);
    o1->aplica();
    o1->imprimeMatrizBase();
    o1->imprimeVertices();

    o1->rotacaoQualquer(30, 4, 8, 2, 5, 2, 3);

    system("pause");

    return 0;
}