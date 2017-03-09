"""
/*
 * TypeOfAnimal.cpp
 *
 *  Created on: 7/3/2017
 *  Author: Cristina Werenitzky
 */

#include <iostream>
#include "TypeOfAnimal.h"
using namespace std;

"""
#Definicion de clase TypeOfAnimal

class TypeOfAnimal(object):

    def __init__(self, agresividad):
	self.agresividad = agresividad

# Este metodo permite construir un tipo de animal de acuerdo al nivel de 
# agresividad del mismo encapsulando la logica de creación al usuario.
# La agresividad esta pensada en un rango [0.1].

    def getType(self,agresividad):
        if(agresividad >= 0.5):
            return Hunter(agresividad)
        else:
            return Victim(agresividad)

##############################################
##Definicion de la clase Hunter


class Hunter(TypeOfAnimal):
    def __init__(self,agresividad):
        super(TypeOfAnimal, self).__init__(agresividad)

#Defino en metodo actuar-->cazar
    def actuar(self,animal_h,animal_v):
        pos_v = animal_v.return_Position()      
	animal_h.move(pos_v)
        if(animal_h.return_position() == pos_v):
            animal_v.life = 0
  

##############################################
##Definicion de la clase Victim

class Victim(TypeOfAnimal):

    def __init__(self,agresividad):
        super(TypeOfAnimal, self).__init__(agresividad)

#Defino en metodo actuar-->huir o quedarse
    def actuar(self,animal_h,animal_v):
        pass
    


