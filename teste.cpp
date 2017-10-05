#include <stdio.h> 
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
    o1->escala(0.589256, 0.883883, 1.414213);
    o1->aplica();
    o1->inicializaMatrizBase();
    o1->imprimeVertices();
    //Questao 2
    o1->translacao(-7.071068, 0 , 0);
    o1->aplica();
    o1->inicializaMatrizBase();
    o1->rotacaoY(135);
    o1->aplica();
    o1->inicializaMatrizBase();
    o1->rotacaoX(-35.265);
    o1->aplica();
    o1->inicializaMatrizBase();
    o1->rotacaoZ(40);
    o1->aplica();
    o1->inicializaMatrizBase();
    o1->translacao(60, 50, 0);
    o1->aplica();
    o1->imprimeVertices();
    o1->inicializaMatrizBase();
    //Questao 3
    o1->translacao(-62.961979, -58.137976, 0);
    o1->aplica();
    o1->imprimeVertices();
    o1->inicializaMatrizBase();
    o1->espelhoQualquer(-0.987354, -2.712627, 4.082452, 4.698460, -1.710102, 0, -4.698460, 1.710098, 0);
    o1->aplica();
    o1->imprimeVertices();
    o1->inicializaMatrizBase();
    o1->translacao(62.961979, 58.137976, 0);
    o1->aplica();
    o1->imprimeVertices();

    
    return 0;
}