import numpy as np 
#from matplotlib import  pyplot as plt
#import math as mat
import clase_type

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
        #self.agresividad = agresividad    #Creo que esto ya no iria
        tipo = clase_type.TypeOfAnimal(agresividad)
        self.type = tipo.getType(agresividad)  


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
    
    def move(self,objetivo):
       
        """ Metodo que indica calcula el movimiento del animal

        Este metodo determina el movimiento del animal de acuerdo al tipo que posee y a si 
        detecto un objetivo

        **Parameters** 
		:objective, type <:class:`Animal`>: el animal se mueve en relacion al objetivo que posee

        """       
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
                print "alla voy,preparate gil"
            
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
        """ Metodo que realiza la busqueda de un nuevo objetivo

        Este metodo retorna el objetivo encontrado en el :class:`Ambiente` 

        **Parameters** 
		:agents, type <array>		
`
        **Returns** 
		:position, type <array>

        """

        objetivo = None 
        minDistance = 9999
        for i in agentes:
            pos_agent = i.return_Position()
            distancia = np.sqrt((pos_agent[0]-self.position[0])**2 + (pos_agent[1]-self.position[1])**2)
            if distancia <= self.perceptionRadio and distancia != 0 and minDistance > distancia:
                minDistance = distancia
                objetivo = i 
                print "detecte algo"        #Tenemos que ver que hace cuando detecto algo 
            # Aca mi animal no detecta nada  
        return objetivo
        
                 
            
      
                        
            
            
#==============================================================================
# A partir de aca voy a tratar de crear yo [Franco] los metodos de la clase viendo de tomar como guia lo que hizo cristina
# No entiendo muy bien la sintaxis de C++ es la primera vez que la veo [Franco]
#==============================================================================
