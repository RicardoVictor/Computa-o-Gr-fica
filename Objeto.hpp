#ifndef OBJETO_H
#define OBJETO_H
#define PI 3.14159265

#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

struct vertice{
    float x;
    float y;
    float z;
};

struct aresta{
    vertice a;
    vertice b;
};

struct face{
    vertice a;
    vertice b;
    vertice c;
};

class Objeto{
    
    //atributos
    protected:
        float matrizBase[4][4];
        float normal[4];
        float qu[4];
        vector<struct vertice> vertices;
        vector<struct aresta> arestas;
        vector<struct face> faces;
        
    //metodos
    public:
        Objeto();
        //float** getMatrizBase();
        vector<struct vertice> getVertices();
        vector<struct aresta> getArestas();
        vector<struct face> getFaces();
        void inicializaMatrizBase();
        void imprimeMatrizBase();
        void imprimeNormal();
        void imprimeVertices();
        void escala(float Sx, float Sy, float Sz);
        void rotacaoX(double ang);
        void rotacaoY(double ang);
        void rotacaoZ(double ang);
        void cisalhamentoYX(double ang);
        void cisalhamentoXY(double ang);
        void cisalhamentoZY(double ang);
        void cisalhamentoYZ(double ang);
        void cisalhamentoZX(double ang);
        void cisalhamentoXZ(double ang);
        void translacao(float Tx, float Ty, float Tz);
        void espelhoYZ();
        void espelhoXZ();
        void espelhoXY();
        void calculaNormal(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3);
        void normaliza();
        void espelhoQualquer(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3);
        void rotacaoQualquer(double ang, float x1, float y1, float z1, float x2, float y2, float z2);
        void addVertice(float x, float y, float z);
        void aplica();
};

Objeto::Objeto(){
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
             i==j ? this->matrizBase[i][j] = 1 : this->matrizBase[i][j] = 0;
}

void Objeto::inicializaMatrizBase(){

    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
             i==j ? this->matrizBase[i][j] = 1 : this->matrizBase[i][j] = 0;

}

/*
float** Objeto::getMatrizBase(){
    return this->matrizBase;
}
*/

vector<struct vertice> Objeto::getVertices(){
    return vertices;
}

vector<struct aresta> Objeto::getArestas(){
    return arestas;
}

vector<struct face> Objeto::getFaces(){
    return faces;
}

void Objeto::imprimeMatrizBase(){
    printf("matrizBase\n");
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
             printf("%f ", matrizBase[i][j]);
        } printf("\n");
    } printf("\n");
}

void Objeto::escala(float Sx, float Sy, float Sz){
    for (int i=0; i<3; i++){
        matrizBase[i][0] = Sx*matrizBase[i][0];
        matrizBase[i][1] = Sy*matrizBase[i][1];
        matrizBase[i][2] = Sz*matrizBase[i][2];
    
    }
}

void Objeto::rotacaoX(double ang){
    for(int i=0; i<3; i++){
        float a = matrizBase[i][1];
        float b = matrizBase[i][2];
        matrizBase[i][1] = a*cos(ang*PI/180) + b*sin(ang*PI/180);  
        matrizBase[i][2] = -(a*sin(ang*PI/180)) + b*cos(ang*PI/180);
    }
}

void Objeto::rotacaoY(double ang){
    for(int i=0; i<3; i++){
        float a = matrizBase[i][0];
        float b = matrizBase[i][2];
        matrizBase[i][0] = a*cos(ang*PI/180) + -(b*sin(ang*PI/180));  
        matrizBase[i][2] = a*sin(ang*PI/180) + b*cos(ang*PI/180);
    }
    
}

void Objeto::rotacaoZ(double ang){
    for(int i=0; i<3; i++){
        float a = matrizBase[i][0];
        float b = matrizBase[i][1];
        matrizBase[i][0] = a*cos(ang*PI/180) + b*sin(ang*PI/180);  
        matrizBase[i][1] = -(a*sin(ang*PI/180)) + b*cos(ang*PI/180);
    }
}

void Objeto::cisalhamentoYX(double ang){
    for(int i=0; i<3; i++)
        matrizBase[i][1] = matrizBase[i][1] + matrizBase[i][0] * tan(ang*PI/180);
}

void Objeto::cisalhamentoXY(double ang){
    for(int i=0; i<3; i++)
        matrizBase[i][0] = matrizBase[i][0] + matrizBase[i][1] * tan(ang*PI/180);
}

void Objeto::cisalhamentoZY(double ang){
    for(int i=0; i<3; i++)
        matrizBase[i][2] = matrizBase[i][2] + matrizBase[i][1] * tan(ang*PI/180);
}

void Objeto::cisalhamentoYZ(double ang){
    for(int i=0; i<3; i++)
        matrizBase[i][1] = matrizBase[i][1] + matrizBase[i][2] * tan(ang*PI/180);
}

void Objeto::cisalhamentoZX(double ang){
    for(int i=0; i<3; i++)
        matrizBase[i][2] = matrizBase[i][2] + matrizBase[i][0] * tan(ang*PI/180);
}

void Objeto::cisalhamentoXZ(double ang){
    for(int i=0; i<3; i++)
        matrizBase[i][0] = matrizBase[i][0] + (matrizBase[i][2] * tan(ang*PI/180));
}

void Objeto::translacao(float Tx, float Ty, float Tz){
    //for (int i=0; i<3; i++)
    //    matrizBase[i][3] = Tx*matrizBase[i][0] + Ty*matrizBase[i][1] + Tz*matrizBase[i][2];   
    
    matrizBase[0][3] += Tx;
    matrizBase[1][3] += Ty;
    matrizBase[2][3] += Tz;
    
}

void Objeto::espelhoYZ(){
    matrizBase[0][0] = -matrizBase[0][0];
}

void Objeto::espelhoXZ(){
    matrizBase[1][1] = -matrizBase[1][1];
}

void Objeto::espelhoXY(){
    matrizBase[2][2] = -matrizBase[2][2];
}

void Objeto::calculaNormal(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3){
    
    struct vertice P1, P2, P3;
    P1.x = x1; P1.y = y1; P1.z = z1;
    P2.x = x2; P2.y = y2; P2.z = z2;
    P3.x = x3; P3.y = y3; P3.z = z3;

    normal[0] = (P2.y - P1.y)*(P3.z - P1.z) - ((P2.z - P1.z)*(P3.y - P1.y));
    normal[1] = (P2.z - P1.z)*(P3.x - P1.x) - ((P2.x - P1.x)*(P3.z - P1.z));
    normal[2] = (P2.x - P1.x)*(P3.y - P1.y) - ((P2.y - P1.y)*(P3.x - P1.x));
    normal[3] = 0;
    
}

void Objeto::imprimeNormal(){
    printf("normal\n");
    for(int i=0; i<4; i++)
        printf("normal[%d]: %f\n", i, normal[i]);
    printf("\n");
}

void Objeto::normaliza(){
    float modulo;
    modulo = sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]);
    //printf("%f\n", modulo);

    for(int i=0; i<3; i++)
        normal[i] /= modulo;

}

void Objeto::espelhoQualquer(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3){
    this->calculaNormal(x1, y1, z1, x2, y2, z2, x3, y3, z3);
    //this->imprimeNormal();
    this->normaliza();
    //this->imprimeNormal();

    float matrizEspelho[4][4];

    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
                i==j ? matrizEspelho[i][j] = 1 : matrizEspelho[i][j] = 0;

    for(int i=0; i<3; i++)
        for(int j=0; j<3; j++)
            matrizEspelho[i][j] -= 2 * normal[i] * normal[j];
    
    printf("matrizEspelho\n");
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            printf("%f ", matrizEspelho[i][j]);
        } printf("\n");
    } printf("\n");

    float matrizAux[4][4];
    for (int i = 0; i < 4; i = i + 1)
        for (int j = 0; j < 4; j = j + 1)
            matrizAux[i][j] = 0;

    for (int i = 0; i < 4; i = i + 1) //linha matriz 1 (=4)
        for (int j = 0; j < 4; j = j + 1) //coluna matriz 2 (=4)
            for (int k = 0; k < 4; k = k + 1) //coluna matriz 1 e linha matriz 2 (=4)
                matrizAux[i][j] += matrizBase[i][k] * matrizEspelho[k][j];

    
    for (int i = 0; i < 4; i = i + 1) 
        for (int j = 0; j < 4; j = j + 1) 
            matrizBase[i][j] = matrizAux[i][j];


}

void Objeto::rotacaoQualquer(double ang, float x1, float y1, float z1, float x2, float y2, float z2){
    
    ang /= 2;

    //vetor U
    qu[0] = x2 - x1;
    qu[1] = y2 - y1;
    qu[2] = z2 - z1;

    //calcula modulo de U
    float modulo;
    modulo = sqrt(qu[0]*qu[0] + qu[1]*qu[1] + qu[2]*qu[2]);

    //calcula U/|U|
    for(int i=0; i<3; i++)
        qu[i] /= modulo;
    
    //calcula u
    for(int i=0; i<3; i++)
        qu[i] *= sin(ang*PI/180);
    qu[3] = cos(ang*PI/180);

    //matriz L
    float L[4][4];
    L[0][0] = qu[3];     L[0][1] = -qu[2];    L[0][2] = qu[1];     L[0][3] = qu[0]; 
    L[1][0] = qu[2];     L[1][1] = qu[3];     L[1][2] = -qu[0];    L[1][3] = qu[1]; 
    L[2][0] = -qu[1];    L[2][1] = qu[0];     L[2][2] = qu[3];     L[2][3] = qu[2]; 
    L[3][0] = -qu[0];    L[3][1] = -qu[1];    L[3][2] = -qu[2];    L[3][3] = qu[3]; 

    //matriz R
    float R[4][4];
    R[0][0] = qu[3];     R[0][1] = -qu[2];    R[0][2] = qu[1];     R[0][3] = -qu[0]; 
    R[1][0] = qu[2];     R[1][1] = qu[3];     R[1][2] = -qu[0];    R[1][3] = -qu[1]; 
    R[2][0] = -qu[1];    R[2][1] = qu[0];     R[2][2] = qu[3];     R[2][3] = -qu[2]; 
    R[3][0] = qu[0];     R[3][1] = qu[1];     R[3][2] = qu[2];     R[3][3] = qu[3];
    
    //matriz final de rotacao qualquer
    float matrizRotacao[4][4];
    for (int i = 0; i < 4; i = i + 1)
        for (int j = 0; j < 4; j = j + 1)
            matrizRotacao[i][j] = 0;

    for (int i = 0; i < 4; i = i + 1) //linha matriz 1(L) (=4)
        for (int j = 0; j < 4; j = j + 1) //coluna matriz 2(R) (=4)
            for (int k = 0; k < 4; k = k + 1) //coluna matriz 1 e linha matriz 2 (=4)
                matrizRotacao[i][j] += L[i][k] * R[k][j];

    printf("matrizRotacao\n");
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            printf("%f ", matrizRotacao[i][j]);
        } printf("\n");
    } printf("\n");

    float matrizAux[4][4];
    for (int i = 0; i < 4; i = i + 1)
        for (int j = 0; j < 4; j = j + 1)
            matrizAux[i][j] = 0;

    for (int i = 0; i < 4; i = i + 1) //linha matriz 1 (=4)
        for (int j = 0; j < 4; j = j + 1) //coluna matriz 2 (=4)
            for (int k = 0; k < 4; k = k + 1) //coluna matriz 1 e linha matriz 2 (=4)
                matrizAux[i][j] += matrizBase[i][k] * matrizRotacao[k][j];

    for (int i = 0; i < 4; i = i + 1) 
        for (int j = 0; j < 4; j = j + 1) 
            matrizBase[i][j] = matrizAux[i][j];
                
}

void Objeto::addVertice(float x, float y, float z){
    struct vertice P;
    P.x = x; P.y = y; P.z = z;

    vertices.push_back(P);
}

void Objeto::imprimeVertices(){
    for(int i=0; i<vertices.size(); i++){
        printf("P%d: %f %f %f\n", i+1, vertices[i].x, vertices[i].y, vertices[i].z);
    } printf("\n");
}

void Objeto::aplica(){
    float a, b, c;
    for(int k=0; k<vertices.size(); k++){
        a = matrizBase[0][0]*vertices[k].x + matrizBase[0][1]*vertices[k].y + matrizBase[0][2]*vertices[k].z + matrizBase[0][3];
        b = matrizBase[1][0]*vertices[k].x + matrizBase[1][1]*vertices[k].y + matrizBase[1][2]*vertices[k].z + matrizBase[1][3];
        c = matrizBase[2][0]*vertices[k].x + matrizBase[2][1]*vertices[k].y + matrizBase[2][2]*vertices[k].z + matrizBase[2][3];
        vertices[k].x = a;
        vertices[k].y = b;
        vertices[k].z = c;
    }
}

#endif