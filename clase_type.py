#Definicion de clase TypeOfAnimal

class TypeOfAnimal(object):

    """	Descripcion de la clase TypeOfAnimal

    Esta clase define el comportamiento general de
    los animales cazadores y presas


     - **Parametro de construccion**:
		:agresividad, ``type <bool>``: nivel de agresividad del animal
	
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
            :agresividad, ``type <bool>``
            
            **Returns** 
			:tipo_animal, type <:class:`Hunter` or :class:`Victim`>
      	"""
       
        if(agresividad >= 0.5):
            return Hunter(agresividad)
        else:
            return Victim(agresividad)

    def actuar(self,animal1, animal2):
        pass

##############################################
##Definicion de la clase Hunter

#import TypeOfAnimal

class Hunter(TypeOfAnimal):

    """	Descripcion de la clase Hunter

    Esta clase hereda el comportamiento de la clase :class:`TypeOfAnimal`.
    Define el comportamiento de los animales cazadores


     - **Parametro de construccion**:
		:agresividad, ``type <bool>``: nivel de agresividad del animal
	
    """


    def __init__(self,agresividad):
        super(Hunter, self).__init__(agresividad)

#Defino en metodo actuar-->cazar
    def actuar(self,animal_hunter,animal_victim):
        """ Metodo que implementa la estrategia de caza de un Hunter.
        
        **Parameters** 
        :animal_hunter, ``type <Animal>``
        
        :animal_victim, ``type <Animal>``
        
        """
        pos_v = animal_victim.return_position()      
        animal_hunter.move(pos_v)

        if(animal_hunter.return_position() == pos_v):
            animal_victim.vida = 0
  

##############################################
##Definicion de la clase Victim

class Victim(TypeOfAnimal):

    """	Descripcion de la clase Victim

    Esta clase hereda el comportamiento de la clase :class:`TypeOfAnimal`.
    Define el comportamiento de los animales victimas o presas


     - **Parametro de construccion**:
		:agresividad, ``type <bool>``: nivel de agresividad del animal
	
    """
    def __init__(self,agresividad):
        super(Victim, self).__init__(agresividad)

#Defino en metodo actuar-->huir o quedarse
    def actuar(self,animal_victim,animal_hunter):
        """ Metodo que implementa la estrategia de escape de un Victim.
        
        **Parameters** 
        :animal_victim, ``type <Animal>``
        
        :animal_hunter, ``type <Animal>``
        
        """

        pass
    


