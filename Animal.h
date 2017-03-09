/*
 * Animal.h
 *
 *  Created on: 7/3/2017
 *  Author: Cristina Werenitzky
 */
#ifndef ANIMAL_H_
#define ANIMAL_H_

#include <iostream>
using namespace std;
#ifndef POSITION_
#define POSITION_
	struct Position{int x; int y;};
#endif

class TypeOfAnimal;
class Animal{
	struct Position position;
	float perceptionRadio;
	int velocity;
	int life;
	TypeOfAnimal *type;
	Animal *objetivo;
	float distance(Animal* a);

public:
	Animal(int radio, int vel, int life, int agresividad);
	void setPosition(Position pos);
	Position getPosition();
	void scout(Animal *animalsArray[], int cant);
	void setObjetivo(Animal *animal);
	TypeOfAnimal *getType();
	void move();
	bool estaVivo();
};


#endif
