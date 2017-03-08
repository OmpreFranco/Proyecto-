# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:32:41 2017

@author: leandro


/*
 * Ambiente.cpp
 *
 *  Created on: 7/3/2017
 *  Author: Cristina Werenitzky
 */


 
#include "Ambiente.h"
#include "TypeOfAnimal.h"
#include <iostream>
using namespace std;


 """
 
class.Ambiente(object):
    def __init__(self,lim):
        self.lim=lim
        self.agents=agents
         
Ambiente::Ambiente(Position lim){
	indice=0;
	limite = lim;
}

"""
/*
void Ambiente::timeStep(){
	detectarObjetivo();
	moverAnimales();
	actualizar();
	graficar();
}
"""
    def.time_step(self):
        self.detect_targets()
        self.move_agents()
        self.update()

"""       
void Ambiente::detectarObjetivo(){
	for(int i=0; i<indice;i++){
		animales[i]->scout(animales, indice);
	}
}
"""
    def.detect_targets(self,self.agents):
        for agent in self.agents:
            agent.scout(self.agents)

"""
void Ambiente::moverAnimales(){
	for(int i=0; i<indice;i++){
		animales[i]->move();
	}
}
"""
    def.move_agents(self,self.agents):
        for agent in self.agents:
            agent.move()

"""
void Ambiente::actualizar(){
	for(int i=0; i<indice;i++){
		if(!animales[i]->estaVivo())
			eliminarAnimal(i);
	}
}
"""

    def.update(self,self.agents):
        sorted(self.agents, key=lambda student: animal.life,reverse=True)

        for agent in self.agents:
            if (agent.life = 0):
                

void Ambiente::graficar(){
	//Graficar ambiente
	//...

	for(int i=0; i< indice;i++){
		//Graficar cada animal
		//cout<< "Animal "<< i << " Posicion ( "<<animales[i]->getPosition().x<<" , "<<animales[i]->getPosition().y<<endl;
	}
}
void Ambiente::agregarAnimal(Animal *a, Position pos){
	if (indice < MAX){
		//Asigno la posicion al animal
		a->setPosition(pos);
		//Agrego el animal en el arreglo
		animales[indice++] = a;
		cout<<"Ambiente.agregar "<<a->getType()->descripcion()<< " - posicion: ("<<pos.x<<","<<pos.y<<")"<<endl;
	}
}

void Ambiente::eliminarAnimal(int idx){
	if (0 <= idx && idx < indice){ //Controlo que sea un indice valido
		if (indice > 1) { //Si tengo mas de un animal
			animales[idx] = animales[indice-1]; //Cambio de lugar el ultimo animal insertado para que no me queden huecos en el arreglo
		}
		indice--;//"Elimino" el ultimo animal (xq ya lo pase a otra posicion)
	}
}