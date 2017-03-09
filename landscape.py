# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:32:41 2017

@author: leandro


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

 """
import clase_Animal
import numpy as np
from np import random
 
class Ambiente(object):
    def __init__(self,lim,agents=None,number_of_agents=None):
        self.lim=lim
        self.agents=agents
        self.number_of_agents=number_of_agents
        
        if agents is None:
            self.agents=[]
            if number_of_agents is None:
                self.number_of_agents=10
            self.add_agents(self)
            
    def time_step(self):
        self.detect_targets()
        self.move_agents()
        self.update()

    def detect_targets(self):
        for agent in self.agents:
            agent.scout(self.agents)

    def move_agents(self):
        for agent in self.agents:
            agent.move()

    def update(self):
        while agent.life == 0 in self.agents: self.agents.remove(agent)
        #for agent in self.agents:
        #    if (agent.life == 0):
        #        self.agents.remove(agent)

    def add_agents(self):
        for i in range(self.number_of_agents):
                radio_vision=np.random()
                position=[np.random()*self.lim[0],np.random()*self.lim[1]]
                vel=np.random()
                life=1.0
                agresividad=np.random.randint(0,2)
                agent=clase_Animal.Animal(radio_vision, position , vel,  life,  agresividad)
                self.agents.append(agent)
             
"""
void Ambiente::graficar(){
	//Graficar ambiente
	//...

	for(int i=0; i< indice;i++){
		//Graficar cada animal
		//cout<< "Animal "<< i << " Posicion ( "<<animales[i]->getPosition().x<<" , "<<animales[i]->getPosition().y<<endl;
	}
}

"""
            
            
            
            
            
            