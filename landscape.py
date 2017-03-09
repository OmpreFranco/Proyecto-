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
 
class Ambiente(object):
    def __init__(self,lim,agents=None,number_of_agents=None):
        self.lim=lim
        if agents is None:
            if number_of_agents is None:
                number_of_agents=10
            for i in range(number_of_agents):
                self.agents=[]

    def time_step(self):
        self.detect_targets()
        self.move_agents()
        self.update()

    def detect_targets(self,self.agents):
        for agent in self.agents:
            agent.scout(self.agents)

    def move_agents(self,self.agents):
        for agent in self.agents:
            agent.move()

    def update(self,self.agents):
        if agent.life = 0 in self.agents: self.agent(agent)
                
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
            
            
            
            
            
            