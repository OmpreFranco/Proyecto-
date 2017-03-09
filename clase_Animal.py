# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:24:37 2017

@author: franco
"""
#==============================================================================
# 
#==============================================================================
import numpy as np 
#from matplotlib import  pyplot as plt
#import math as mat


#==============================================================================
# definimos la clase animal
#==============================================================================
class Animal():
    # Atributos de la clase animal 
    def __init__(self,radio_vision, position , vel,  life,  agresividad): #position es un areglo de dos elementos [X,Y], de que objeto la obtengo ?
		self.position = position
		self.perceptionRadio = radio_vision
		self.velocity = vel
		self.life = life
		self.agresividad = agresividad
  		self.type = tipo.TypeOfAnimal(agresividad) # Llamo al metodo de la clase TypeOfAnimal que me devuelve el tipo de animal que es. seguramente-
                                                      # -se llame de algun modo distinto

    # Metodo de clase para establecer la posicion 
    def return_Position(self):
#        self.position = position
        return self.position
    # Metodo para obtener la nueva posicion                 
    def move(self,objetivo):
        #Creo un modo de que el animal vaya a la posicion de su objetivo si su agresividad es mayor        
        if objetivo != None and self.agresividad != objetivo.agresividad:
            #calculo la distancia entre el objetivo y el cazador 
            delta_x = objetivo.position[0]-self.position[0] # Distancia en x entre vicitima y cazador
            delta_y = objetivo.position[1]-self.position[1] # Distancia en y entre vicitima y cazador
            distancia = np.sqrt((delta_x)**2 + (delta_y)**2)

            if distancia > self.velocity:
                #defino el versor donde apunta la direccion que une ambos objetos
                r_versor = [delta_x,delta_y ] / distancia
                self.position = self.position + r_versor * self.velocity 
                print "alla voy"
            else:    
                self.position = objetivo.position 
                print"vas a morir moe wiii"
        #Creo un modo de que el animal camine aleatoriamente
        else:
            print "nada por aqui"
            a = np.random.random(1)*2*np.pi # Genero el angulo aleatorio 
            self.position[0] = self.position[0] + np.cos(a)*self.velocity # Marco el cambio de posicion en X e Y 
            self.position[1] = self.position[1] + np.sin(a)*self.velocity

                
    #  Metodo para hacer que el animal sense su entorno    
    def scout(self,agentes): # Agentes seria la lista de animales en el ambiente
        objetivo = None    
        for i in agents:
            pos_agent = i.return_Postion()
            distancia = np.sqrt((pos_agent[0]-self.position[0])**2 + (pos_agent[1]-self.position[1])**2)
            if distancia < self.perceptionRadio and distancia != 0:
                objetivo = i 
                print "detecte algo"        #Tenemos que ver que hace cuando detecto algo 
            # Aca mi animal no detecta nada     
        
                 
            
      
                        
            
            
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