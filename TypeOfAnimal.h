/*
 * TypeOfAnimal.h
 *
 *  Created on: 7/3/2017
 *  Author: Cristina Werenitzky
 */

#ifndef TYPEOFANIMAL_H_
#define TYPEOFANIMAL_H_

#define UMBRAL 5

#include <iostream>
#include "Animal.h"
using namespace std;

//----------------------------------------------------------------------------------------------
// CLASE ABSTRACTA TypeOfAnimal

class TypeOfAnimal{
protected:
	int agresividad;
	TypeOfAnimal(int agr=0);
public:
	static TypeOfAnimal *getTypeOfAnimal(int agresividad);
	int getAgresividad(); //Retorna el nivel de agresividad de un animal

	//Estas funciones se redefinen en cada subclase con el comportamiento adecuado
	virtual bool esObjetivo(Animal *a1)=0;
	virtual void actuar(Animal *a1, Animal *a2)=0;
	virtual string descripcion()=0;//Solo para escribir mensaje
	//Destructor virtual
	virtual ~TypeOfAnimal();
};
//----------------------------------------------------------------------------------------------
// Subclase de TypeOfAnimal
class Hunter: public TypeOfAnimal{

	void cazar(Animal *cazador, Animal *presa);

public:
	Hunter(int agr);
	bool esObjetivo(Animal *presa);
	void actuar(Animal *cazador, Animal *presa);
	virtual string descripcion();
};

//----------------------------------------------------------------------------------------------
// Subclase de TypeOfAnimal

class Victim:public TypeOfAnimal{
	void huir(Animal* presa, Animal* cazador);

public:
	Victim(int agr);
	bool esObjetivo(Animal *presa);
	void actuar(Animal *presa, Animal *cazador);
	virtual string descripcion();
};

//----------------------------------------------------------------------------------------------
#endif /* TYPEOFANIMAL_H_ */
