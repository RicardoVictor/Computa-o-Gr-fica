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
    
    protected:
        float matrizBase[4][4];
        float normal[4];
        vector<struct vertice> vertices;
        vector<struct aresta> arestas;
        vector<struct face> faces;
        
    public:
        Objeto();
        //float** getMatrizBase();
        vector<struct vertice> getVertices();
        vector<struct aresta> getArestas();
        vector<struct face> getFaces();
        void imprimeMatrizBase();
        void escala(int Sx, int Sy, int Sz);
        void rotacaoX(double ang);
        void rotacaoY(double ang);
        void rotacaoZ(double ang);
        void cisalhamentoYX(double ang);
        void cisalhamentoXY(double ang);
        void cisalhamentoZY(double ang);
        void cisalhamentoYZ(double ang);
        void cisalhamentoZX(double ang);
        void cisalhamentoXZ(double ang);
        void translacao(int Tx, int Ty, int Tz);
        void espelhoYZ();
        void espelhoXZ();
        void espelhoXY();
        void calculaNormal(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3);
        void imprimeNormal();
};

Objeto::Objeto(){
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
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
             printf("%f ", matrizBase[i][j]);
        } printf("\n");
    } printf("\n");
}

void Objeto::escala(int Sx, int Sy, int Sz){
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

void Objeto::translacao(int Tx, int Ty, int Tz){
    for (int i=0; i<3; i++)
        matrizBase[i][3] = Tx*matrizBase[i][0] + Ty*matrizBase[i][1] + Tz*matrizBase[i][2];   
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
    for(int i=0; i<4; i++)
        printf("normal[%d]: %f\n", i, normal[i]);
}

#endif