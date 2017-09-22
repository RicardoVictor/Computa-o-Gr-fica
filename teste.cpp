#include "Objeto.hpp"
#include "Cubo.hpp"

using namespace std;

int main(){
 
    Objeto *o1 = new Objeto();

//    o1->imprimeMatrizBase();
//    o1->espelhoXY();
//    o1->imprimeMatrizBase();
//    o1->espelhoYZ();
//    o1->imprimeMatrizBase();

//    o1->calculaNormal(0, 0, 4, 6, 0, 0, 0, 10, 0);
//    o1->imprimeNormal();
//    o1->normaliza();
//    o1->imprimeNormal();

    o1->espelhoQualquer(0, 0, 4, 6, 0, 0, 0, 10, 0);

    return 0;
}