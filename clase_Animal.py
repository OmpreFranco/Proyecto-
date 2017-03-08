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
		self.position.x = 0
		self.position.y = 0
		self.perceptionRadio = radio
		self.velocity = vel
		self.life = life
		self.objetivo = 0
		self.type = TypeOfAnimal::getTypeOfAnimal(agresividad)
  
  