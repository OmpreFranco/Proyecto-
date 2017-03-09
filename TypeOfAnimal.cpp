/*
 * TypeOfAnimal.cpp
 *
 *  Created on: 7/3/2017
 *  Author: Cristina Werenitzky
 */

#include <iostream>
#include "TypeOfAnimal.h"
using namespace std;

//----------------------------------------------------------------------------------------------
//Definicion de los metodos de la clase TypeOfAnimal

TypeOfAnimal::TypeOfAnimal(int agr){
		agresividad=agr;
}

TypeOfAnimal * TypeOfAnimal::getTypeOfAnimal(int agresividad){ //Fatory Method
	//Este metodo permite construir un tipo de animal de acuerdo al nivel de agresividad del mismo
	//encapsulando la logica de creación al usuario
		if(agresividad > UMBRAL){
			return new Hunter(agresividad);
		}
		else
			return new Victim(agresividad);
}

int TypeOfAnimal::getAgresividad(){
	return agresividad;
}

TypeOfAnimal::~TypeOfAnimal(){}

//----------------------------------------------------------------------------------------------
//Definicion de los metodos de la clase Hunter

Hunter::Hunter(int agr):TypeOfAnimal(agr){}

void Hunter::cazar(Animal *cazador, Animal *presa){
		//Estrategia de caza
}

bool Hunter::esObjetivo(Animal *presa){
	//El cazador SIEMPRE caza si su presa tiene menor nivel de agresividad
	return (this->agresividad > presa->getType()->getAgresividad());
}

void Hunter::actuar(Animal *cazador, Animal *presa){
		cazar(cazador, presa);
}

string Hunter::descripcion(){
		return "CAZADOR";
}

//----------------------------------------------------------------------------------------------
//Definicion de los metodos de la clase Victim

Victim::Victim(int agr):TypeOfAnimal(agr){}

void Victim::huir(Animal* presa, Animal* cazador){
	//Feature: Estrategia de huida
}

bool Victim::esObjetivo(Animal *presa){
	return (false); //Feature: la victima detecta a su cazador como objetivo y huye
}

void Victim::actuar(Animal *presa, Animal *cazador){
	huir(presa, cazador);
}

string Victim::descripcion(){
	return "VICTIMA";
}
//----------------------------------------------------------------------------------------------
