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
    # Atributos de la clase animal 
    def __init__(self,radio,  vel,  life,  agresividad):
		self.position_x = 0
		self.position_y = 0
		self.perceptionRadio = radio
		self.velocity = vel
		self.life = life
		self.objetivo = 0
		self.type = TypeOfAnimal(agresividad)
 
    # Metodo de clase para establecer la posicion 
    def setPosition(self ,pos):
        self.position = pos
    # Metodo para obtener la nueva posicion         
    def getPosition(self):
        return position # aca position no esta bien definido, de donde la obtengo ?
    #  Metodo para hacer que el animal camine y sense su entorno    
    def scout(self,agentes,cant): # Agentes seria la lista de animales en el ambiente
                        # no entiendo que seria lo que se implemento en c++ de Animal *animalsArray[], int cant que es cant?
        min_Distance = 9999 # Aca calramente , o no , deberia ser un numero menor esta puesto al azar creo CHEQUEAR !
        obj = agentes * 0 # Creo que aca crea una lista de ceros pero del mismo tamano que agentes
                            #Ver bien si agentes es la animalArray
        while i<cant:
            if ()       #No entiendo como es la estrucutura de este if ni cuales son las variables 
#==============================================================================
# A partir de aca voy a tratar de crear yo [Franco] los metodos de la clase viendo de tomar como guia lo que hizo cristina
# No entiendo muy bien la sintaxis de C++ es la primera vez que la veo [Franco]
#==============================================================================
        
    
    
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