
import numpy as np 
from matplotlib import  pyplot as plt
import math as mat


#----------------------------------------------
#==============================================================================
# Importar las clases de los archivos .py 
#==============================================================================

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
ecosistema = landscape.Ambiente(limite,30) 


#Simulacion

for t in range(TiempoLimite):
     
# queda la estrucutura de lo que va a correr la simulacion. Debemos desarrollar los metodos      
	ecosistema.time_step() 

#==============================================================================
# se trabajara las clases enn otros archivos que luego son importados 
#==============================================================================
  
  
  
  
  
  
  
  
  
  
  
  