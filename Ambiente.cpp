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

Ambiente::Ambiente(Position lim){
	indice=0;
	limite = lim;
}

/*
void Ambiente::timeStep(){
	detectarObjetivo();
	moverAnimales();
	actualizar();
	graficar();
}
*/
void Ambiente::detectarObjetivo(){
	for(int i=0; i<indice;i++){
		animales[i]->scout(animales, indice);
	}
}

void Ambiente::moverAnimales(){
	for(int i=0; i<indice;i++){
		animales[i]->move();
	}
}
void Ambiente::actualizar(){
	for(int i=0; i<indice;i++){
		if(!animales[i]->estaVivo())
			eliminarAnimal(i);
	}
}
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

