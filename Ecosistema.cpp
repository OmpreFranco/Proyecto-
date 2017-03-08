//============================================================================
// Name        : Ecosistema.cpp
// Author	   : Cristina Werenitzky
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<stdlib.h>
#include<time.h>
#include "Ambiente.h"
#include "TypeOfAnimal.h"

using namespace std;

int main() {

	//PARAMETROS DE LA SIMULACION
	int TiempoLimite = 100;
	int tiempo;

	//Inicializo el generador de nros aleatorios
	srand(time(NULL));

	//Creo el ecosistema
	int xMax=15, yMax=15;
	Position limite = {xMax, yMax};
	Ambiente ecosistema(limite);

	//Defino parametros de mis animales
	int radioL=3, radioG=2;
	int velL=2, velG=1;
	int lifeL=4, lifeG=5;
	int agrL=10, agrG=0;

	//Creo un animal de cada tipo
	Animal leon(radioL, velL, lifeL, agrL);
	Animal gacela(radioG, velG, lifeG, agrG);

	//Genero posiciones aleatorias x, y
	Position posL, posG;
	posL.x =  rand() % (xMax +1) ;
	posL.y = rand() % (yMax +1);
	posG.x =  rand() % (xMax +1) ;
	posG.y = rand() % (yMax +1);

	//Agrego los animales al ambiente
	ecosistema.agregarAnimal(&gacela, posG);
	ecosistema.agregarAnimal(&leon, posL);

	//Simulación
	for(tiempo = 0; tiempo<TiempoLimite; tiempo++){
			ecosistema.detectarObjetivo();
			ecosistema.moverAnimales();
			ecosistema.actualizar();
			ecosistema.graficar();
	}

	return 0;
}
