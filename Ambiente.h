/*
 * Ambiente.h
 *
 *  Created on: 7/3/2017
 *  Author: Cristina Werenitzky
 */

#ifndef AMBIENTE_H_
#define AMBIENTE_H_
#define MAX 10
#include <iostream>
using namespace std;
#ifndef POSITION_
#define POSITION_
	struct Position{int x; int y;};
#endif

class Animal;

class Ambiente{

	Animal *animales[MAX];
	int indice;
	Position limite;
public:
	Ambiente(Position lim);
	void timeStep();
	void detectarObjetivo();
	void moverAnimales();
	void actualizar();
	void graficar();
	void agregarAnimal(Animal *a, Position pos);
	void eliminarAnimal(int idx);
};

#endif /* AMBIENTE_H_ */
