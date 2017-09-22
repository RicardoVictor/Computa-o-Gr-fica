#include "Objeto.hpp"
#include "Cubo.hpp"

using namespace std;

int main(){
 
    Objeto *o1 = new Objeto();

    o1->imprimeMatrizBase();
    o1->espelhoXY();
	o1->imprimeMatrizBase();
	o1->espelhoYZ();
	o1->imprimeMatrizBase();


    return 0;
}