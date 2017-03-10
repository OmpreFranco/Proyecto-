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
    """	Descripcion de la clase Animal

    La clase **Animal** permite crear los animales que estaran en la simulacion

     - **Parametro de construccion**:
		:position, ``type <array>``: posicion asignada al animal dentro del ambiente
	        :perceptionRadio, ``type <float>``: radio de percepcion del animal
		:velocity, ``type <float>``: velocidad del animal en un paso de tiempo?????
	        :life, ``type <bool>``: Valor que determina si el animal esta vivo
		:type, ``type <:class:`TypeOfAnimal`>``: tipo que posee el animal (:class:`Hunter` o :class:`Victim`)

    """

    def __init__(self,radio_vision, position , vel,  life,  agresividad): 
        self.position = position
        self.perceptionRadio = radio_vision
        self.velocity = vel
        self.life = life
        self.agresividad = agresividad    #Creo que esto ya no iria
        tipo = clase_type.TypeOfAnimal(agresividad)
        self.type = tipo.getType(agresividad)  
	self.objetivo = 0

    # Metodo de clase para establecer la posicion 
    def return_Position(self):
	# self.position = position
        """ Metodo que retorna la posicion de un animal

        Este metodo retorna la posicion asignada al animal dentro del :class:`Ambiente` 

        **Parameters** 
		
`
        **Returns** 
		:position, type <array>

        """
        return self.position
   
   
   # Metodo para obtener la nueva posicion               
    
    def move(self,objetivo,Ambiente): # Ambiente es un objeto de la clase ambiente
       
        """ Metodo que indica calcula el movimiento del animal

        Este metodo determina el movimiento del animal de acuerdo al tipo que posee y a si 
        detecto un objetivo

        **Parameters** 
		:objective, type <:class:`Animal`>: el animal se mueve en relacion al objetivo que posee

        """   
	if self.objetivo != None :
	    otroEspecimen = self.type.actuar(self, self.objetivo)
	    if type(otroEspecimen) == type(self):	
	        #Ambiente.agents.append(otroEspecimen)
	        print("Nacio un animal!")		
	else:
    	    #Movete aleatoriamente
            print("nada por aqui")
            # if (self.agresividad==1):
            lim_animal = landscape.Ambiente.limits(Ambiente)
            a = np.random.random(1)*2*np.pi # Genero el angulo aleatorio 
            self.position[0] = self.position[0] + np.cos(a)*self.velocity # Marco el cambio de posicion en X e Y 
            self.position[1] = self.position[1] + np.sin(a)*self.velocity
            if self.position[0]<0:
                self.position[0] = 0
            if self.position[0] > lim_animal[0]:
                self.position[0] = lim_animal[0]
            if self.position[1]<0:
               self.position[1] = 0
            if self.position[1] > lim_animal[1]:
               self.position[1] = lim_animal[1]



        """
       #Creo un modo de que el animal vaya a la posicion de su objetivo si su agresividad es mayor        
        if self.objetivo != None and self.agresividad > self.objetivo.agresividad:


            #calculo la distancia entre el objetivo y el cazador 
            delta_x = self.objetivo.position[0]-self.position[0] # Distancia en x entre vicitima y cazador
            delta_y = self.objetivo.position[1]-self.position[1] # Distancia en y entre vicitima y cazador
            distancia = np.sqrt((delta_x)**2 + (delta_y)**2)

            if distancia > self.velocity:
                #defino el versor donde apunta la direccion que une ambos objetos
                r_versor = [delta_x,delta_y ] / distancia
                self.position[0] = self.position[0] + r_versor[0] * self.velocity 
                self.position[1] = self.position[1] + r_versor[1] * self.velocity 

                print("alla voy,preparate gil")
            
            else:    
                self.position = self.objetivo.position 
		self.objetivo.life = 0	
                print("vas a morir moe wiii")
                print("Faa, que rico asado")

        #Creo un modo de que el animal camine aleatoriamente
        else:
            print("nada por aqui")
           # if (self.agresividad==1):
            lim_animal = landscape.Ambiente.limits(Ambiente)
            a = np.random.random(1)*2*np.pi # Genero el angulo aleatorio 
            self.position[0] = self.position[0] + np.cos(a)*self.velocity # Marco el cambio de posicion en X e Y 
            self.position[1] = self.position[1] + np.sin(a)*self.velocity
            if self.position[0]<0:
                self.position[0] = 0
            if self.position[0] > lim_animal[0]:
                self.position[0] = lim_animal[0]
            if self.position[1]<0:
               self.position[1] = 0
            if self.position[1] > lim_animal[1]:
               self.position[1] = lim_animal[1]
       """                             
                
    #  Metodo para hacer que el animal sense su entorno    
    def scout(self,agentes): # Agentes seria la lista de animales en el ambiente
        """ Metodo que realiza la busqueda de un nuevo objetivo

        Este metodo retorna el objetivo encontrado en el :class:`Ambiente` 

        **Parameters** 
		:agents, type <array>		
`
        **Returns** 
		:position, type <array>

        """

        self.objetivo = None 
        minDistance = 9999
        for i in agentes:
            pos_agent = i.return_Position()
            distancia = np.sqrt((pos_agent[0]-self.position[0])**2 + (pos_agent[1]-self.position[1])**2)
            if distancia <= self.perceptionRadio and distancia != 0 and minDistance > distancia :#and self.type.esObjetivo(i):
                minDistance = distancia
                self.objetivo = i 
                print("detecte algo")       #Tenemos que ver que hace cuando detecto algo 
            # Aca mi animal no detecta nada  
        return self.objetivo
        
                 
            
      
                        
            
            

