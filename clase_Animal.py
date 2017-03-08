# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:24:37 2017

@author: franco
"""
import numpy as np 
from matplotlib import  pyplot as plt
import math as mat

#==============================================================================
# definimos la clase animal
#==============================================================================
class Animal():
    
    def __init__(self,radio,  vel,  life,  agresividad):
		self.position_x = 0
		self.position_y = 0
		self.perceptionRadio = radio
		self.velocity = vel
		self.life = life
		self.objetivo = 0
		self.type = TypeOfAnimal(agresividad)
 

    def setPosition(pos):
        self.position = pos
        
    def getPosition(self):
        return position 
        
    def
#void Animal::setPosition(Position pos){
#	this->position = pos;
#}
#Position Animal::getPosition(){
#		return position;
#}
#
#void Animal::scout(Animal *animalsArray[], int cant){
#	//En cada busqueda puedo o no detectar un objetivo
#		int minDistance = 9999;
#		Animal *obj =NULL;
#		//Controlo TODOS los animales del ambiente para determinar cual es mi objetivo mas cercano
#		for(int i=0;i<cant;i++){
#			if(type->esObjetivo(animalsArray[i]) && minDistance > this->distance(animalsArray[i])){
#				minDistance = this->distance(animalsArray[i]);
#				obj = animalsArray[i];
#			}
#		}
#		this->setObjetivo(obj); //Guardo cual es mi objetivo, para poder moverme de acuerdo al mismo
#	}
#
#void Animal::setObjetivo(Animal *animal){
#		this->objetivo= animal;
#	}
#
#TypeOfAnimal *Animal::getType(){
#	//Esta funcion retorna el tipo al cual pertenece el animal para poder actuar en base a su tipo
#	return type;
#}
#
#void Animal::move(){
#	if(this->objetivo) {//Si tengo un objetivo -  (objetivo != NULL)
#		//Tengo un objetivo que perseguir, me muevo de acuerdo al objetivo
#		this->getType()->actuar(this, this->objetivo);
#	}
#	else{ //No detecte objetivo en mi busqueda
#		//Determino un movimiento aleatorio para el animal
#	}
#}
#
#bool Animal::estaVivo(){
#	return life > 0;
#}
#
#float Animal::distance(Animal* a){
#	Position P1 = this->getPosition();
#	Position P2 = a->getPosition();
#	float xVal = P2.x - P1.x;
#	float yVal = P2.y - P1.y;
#	return sqrt(xVal*xVal + yVal*yVal);
#}  