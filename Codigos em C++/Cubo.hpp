#ifndef CUBO_H
#define CUBO_H
#include "Objeto.hpp"

using namespace std;

class Cubo:public Objeto{
    public:
        Cubo();
        Cubo(vertice v0, vertice v1, vertice v2, vertice v3, vertice v4, vertice v5, vertice v6, vertice v7);
};

Cubo::Cubo(){
    struct vertice v0, v1, v2, v3, v4, v5, v6, v7;
    
    v0.x=0; v0.y=0; v0.z=0;
    v1.x=1; v1.y=0; v1.z=0;
    v2.x=1; v2.y=1; v2.z=0;
    v3.x=0; v3.y=1; v3.z=0;
    v4.x=0; v4.y=0; v4.z=1;
    v5.x=1; v5.y=0; v5.z=1;
    v6.x=1; v6.y=1; v6.z=1;
    v7.x=0; v7.y=1; v7.z=1;

    vertices.push_back(v0);
    vertices.push_back(v1);
    vertices.push_back(v2);
    vertices.push_back(v3);
    vertices.push_back(v4);
    vertices.push_back(v5);
    vertices.push_back(v6);
    vertices.push_back(v7);

}

Cubo::Cubo(vertice v0, vertice v1, vertice v2, vertice v3, vertice v4, vertice v5, vertice v6, vertice v7){
    vertices.push_back(v0);
    vertices.push_back(v1);
    vertices.push_back(v2);
    vertices.push_back(v3);
    vertices.push_back(v4);
    vertices.push_back(v5);
    vertices.push_back(v6);
    vertices.push_back(v7);
}

#endif