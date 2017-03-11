#Definicion de clase TypeOfAnimal
import numpy as np
import clase_Animal
class TypeOfAnimal(object):

    """	Descripcion de la clase TypeOfAnimal

    Esta clase define el comportamiento general de
    los animales cazadores y presas


     - **Parametro de construccion**:
		:agresividad, ``type <int>``: nivel de agresividad del animal
	
    """

    def __init__(self, agresividad):
        self.agresividad = agresividad

# Este metodo permite construir un tipo de animal de acuerdo al nivel de 
# agresividad del mismo encapsulando la logica de creacion al usuario.
# La agresividad esta pensada en un rango [0.1].

    def getType(self,agresividad):

        """ Factory Method que construye un tipo especifico de animal.
        
        Este metodo genera un tipo especifico de animal (:class:`Hunter` o :class:`Victim`) 
        dependiendo del nivel de agresividad
        
        **Parameters** 
                :agresividad, ``type <int>``
            
        **Returns** 
                :tipo_animal, type <:class:`Hunter` or :class:`Victim`>
        """
       
        if(agresividad >= 0.5):
            return Hunter(agresividad)
        else:
            return Victim(agresividad)

    def actuar(self,animal1, animal2):
        pass

        """ Metodo que le permite al animal actuar dependiendo del tipo de animal que es.
        
        **Parameters** 
            :animal1, ``type <Animal>``
            :animal2, ``type <Animal>``
         
      	"""
       
    def esObjetivo(self, animal):
	pass

        """ Metodo que le permite al animal saber cuales de los animales que puede 
            ver en su radio de busqueda son un objetivo o no.
        
        **Parameters** 
            :animal, ``type <Animal>``
         
      	"""

##############################################
##Definicion de la clase Hunter

#import TypeOfAnimal

class Hunter(TypeOfAnimal):

    """	Descripcion de la clase Hunter

    Esta clase hereda el comportamiento de la clase :class:`TypeOfAnimal`.
    Define el comportamiento de los animales cazadores


     - **Parametro de construccion**:
		:agresividad, ``type <int>``: nivel de agresividad del animal
	
    """


    def __init__(self,agresividad):
        super(Hunter, self).__init__(agresividad)

#Defino en metodo actuar-->cazar
    def actuar(self,animal_hunter,animal_victim):

        """ Metodo que implementa la estrategia de caza de un Hunter.
        
        **Parameters** 
                :animal_hunter, ``type <Animal>``
        
                :animal_victim, ``type <Animal>``
        
        **Returns** 
	        :otroEspecimen, type <:class:`Animal`>
        """

	otroEspecimen = None
        if animal_hunter.type.agresividad > animal_victim.type.agresividad:
            #calculo la distancia entre el objetivo y el cazador 
            delta_x = animal_victim.position[0]-animal_hunter.position[0] # Distancia en x entre vicitima y cazador
            delta_y = animal_victim.position[1]-animal_hunter.position[1] # Distancia en y entre vicitima y cazador
            distancia = np.sqrt((delta_x)**2 + (delta_y)**2)

            if distancia > animal_hunter.velocity:
                #defino el versor donde apunta la direccion que une ambos objetos
                r_versor = [delta_x,delta_y ] / distancia
                animal_hunter.position[0] = animal_hunter.position[0] + r_versor[0] * animal_hunter.velocity 
                animal_hunter.position[1] = animal_hunter.position[1] + r_versor[1] * animal_hunter.velocity 

                print("alla voy,preparate gil")
            
            else:    
                animal_hunter.position = animal_victim.position 
		animal_victim.life = 0	
		animal_hunter.life = 10
                print("vas a morir moe wiii")
                print("Faa, que rico asado")
	else:
            radio=animal_victim.perceptionRadio
	    otroEspecimen = clase_Animal.Animal(radio,animal_hunter.position, animal_hunter.velocity,300,1)			
        return otroEspecimen

    def esObjetivo(self, animal):

        """ Metodo que permite al animal saber si los animales que tiene en su radio de busqueda son objetivos 
        dependiendo de la diferencia de agresividad.  
        
        **Parameters** 
                :animal, ``type <Animal>``
        
        **Returns** 
                :comparacion entre las agresividades, ``type <comparacion>``
        """

	return self.agresividad > animal.agresividad
    



##############################################
##Definicion de la clase Victim

class Victim(TypeOfAnimal):

    """	Descripcion de la clase Victim

    Esta clase hereda el comportamiento de la clase :class:`TypeOfAnimal`.
    Define el comportamiento de los animales victimas o presas


     - **Parametro de construccion**:
		:agresividad, ``type <int>``: nivel de agresividad del animal
	
    """

    def __init__(self,agresividad):
        super(Victim, self).__init__(agresividad)

#Defino en metodo actuar-->huir o quedarse
    def actuar(self,animal_victim,animal_hunter):

        """ Metodo que implementa la estrategia de escape de un Victim.
        
        **Parameters** 
                :animal_victim, ``type <Animal>``
        
                :animal_hunter, ``type <Animal>``

        **Returns** 
                :otroEspecimen, type <:class:`Animal`>
        
        """

	otroEspecimen = None
	if animal_victim.type.agresividad == animal_hunter.type.agresividad:
            radio = animal_victim.perceptionRadio
	    otroEspecimen = clase_Animal.Animal(radio,animal_hunter.position, animal_hunter.velocity,300,0)		
	else:	

            #calculo la distancia entre el objetivo y el cazador 

            delta_x = animal_victim.position[0]-animal_hunter.position[0] # Distancia en x entre vicitima y cazador
            delta_y = animal_victim.position[1]-animal_hunter.position[1] # Distancia en y entre vicitima y cazador
            distancia = np.sqrt((delta_x)**2 + (delta_y)**2)

            #defino el versor donde apunta la direccion que une ambos objetos
            r_versor = [delta_x,delta_y ] / distancia
            animal_victim.position[0] = animal_victim.position[0] - r_versor[0]*np.random.random() * animal_victim.velocity 
            animal_victim.position[1] = animal_victim.position[1] - r_versor[1]*np.random.random() * animal_victim.velocity 

            print("Mamaaaaaa!!!")
        return otroEspecimen                
        

    def esObjetivo(self, animal):

        """ Metodo que permite al animal saber si los animales que tiene en su radio de busqueda son objetivos 
        dependiendo de la diferencia de agresividad.  
        
        **Parameters** 
                :animal, ``type <Animal>``
        
        **Returns** 
                :comparacion entre las agresividades, ``type <comparacion>``
        """

	return self.agresividad < animal.agresividad
    


