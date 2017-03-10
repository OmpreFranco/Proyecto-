
import numpy as np 
#from matplotlib import  pyplot as plt
#import math as mat
import clase_type
import landscape
#==============================================================================
# definimos la clase animal
#==============================================================================
class Animal():
    # Atributos de la clase animal 
    """
    La clase **Animal** crea los animales que estaran en la simulacion.
    
    """
    def __init__(self,radio_vision, position , vel,  life,  agresividad): #position es un areglo de dos elementos [X,Y], de que objeto la obtengo ?
        self.position = position
        self.perceptionRadio = radio_vision
        self.velocity = vel
        self.life = life
        self.agresividad = agresividad
        tipo = clase_type.TypeOfAnimal(agresividad)
        self.type = tipo.getType(agresividad)  
    # Metodo de clase para establecer la posicion 
    def return_Position(self):
#        self.position = position
        return self.position
   
   
   # Metodo para obtener la nueva posicion               
    
    def move(self,objetivo,Ambiente): # Ambiente es un objeto de la clase ambiente
       
       
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

                print("alla voy,preparate gil")
            
            else:    
                self.position = objetivo.position 
                print("vas a morir moe wiii")
                print("Faa, que rico asado")

        #Creo un modo de que el animal camine aleatoriamente
        else:
            print("nada por aqui")

            lim_animal = landscape.Ambiente.limits()
            a = np.random.random(1)*2*np.pi # Genero el angulo aleatorio 
            self.position[0] = self.position[0] + np.cos(a)*self.velocity # Marco el cambio de posicion en X e Y 
            self.position[1] = self.position[1] + np.sin(a)*self.velocity
            if self.position[0]<0:
                self.position[0] = 0
            if self.position[0] > lim_animal[0]:
                self.position = lim_animal[0]
            if self.position[1]<0:
                self.position[1] = 0
            if self.position[1] > lim_animal[1]:
                self.position = lim_animal[1]
                                
                
    #  Metodo para hacer que el animal sense su entorno    
    def scout(self,agentes): # Agentes seria la lista de animales en el ambiente
        objetivo = None 
        minDistance = 9999
        for i in agentes:
            pos_agent = i.return_Position()
            distancia = np.sqrt((pos_agent[0]-self.position[0])**2 + (pos_agent[1]-self.position[1])**2)
            if distancia <= self.perceptionRadio and distancia != 0 and minDistance > distancia:
                minDistance = distancia
                objetivo = i 
                print("detecte algo")       #Tenemos que ver que hace cuando detecto algo 
            # Aca mi animal no detecta nada  
        return objetivo
        
                 
            
      
                        
            
            
#==============================================================================
# A partir de aca voy a tratar de crear yo [Franco] los metodos de la clase viendo de tomar como guia lo que hizo cristina
# No entiendo muy bien la sintaxis de C++ es la primera vez que la veo [Franco]
#==============================================================================
