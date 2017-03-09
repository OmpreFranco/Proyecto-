# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:15:11 2017

@author: franco
"""
#==============================================================================
# 
#==============================================================================
#----------------------------------------------
import numpy as np 
from matplotlib import  pyplot as plt
import math as mat


#----------------------------------------------
#==============================================================================
# Importar las clases de los archivos .py 
#==============================================================================
#import clase_Animal
#import clase_type
import landscape

#Programa principal 

##PARAMETROS DE LA SIMULACION
TiempoLimite = 100  

#Creo el ecosistema
xMax=15
yMax=15 
# Impongo el limite del ambiente
limite = [xMax, yMax]
# Creo el objeto ecosistema de la clase ambiente 
ecosistema = landscape.Ambiente(limite,100) 

##Defino parametros de mis animales
#radioL=3
#radioG=2 
#velL=2
#velG=1 
#lifeL=4
#lifeG=5 
#agrL=10
#agrG=0 
#
##Genero posiciones aleatorias x, y
#posL_x = np.random.random(1) * (xMax +1)  
#posL_y = np.random.random(1) * (yMax +1) 
#posG_x = np.random.random(1) * (xMax +1)  
#posG_y = np.random.random(1) * (yMax +1) 
#posL = [posL_x , posL_y] 
#posG = [posG_x , posG_y] 

##Creo un animal de cada tipo
#leon = Animal(radioL,posL ,velL, lifeL, agrL) 
#gacela = Animal(radioG, posL,velG, lifeG, agrG) 



##Agrego los animales al ambiente
## estoy llamando al metodo agregar animal de la clase ambiente 
#ecosistema.agregarAnimal(gacela, posG) 
#ecosistema.agregarAnimal(leon, posL) 

#Simulación

for t in range(TiempoLimite):
     
# queda la estrucutura de lo que va a correr la simulacion. Debemos desarrollar los metodos      
	ecosistema.time_step() 
#	ecosistema.moverAnimales() 
#	ecosistema.actualizar() 
##	ecosistema.graficar() 

#==============================================================================
# se trabajara las clases enn otros archivos que luego son importados 
#==============================================================================
  
  
  
  
  
  
  
  
  
  
  
  