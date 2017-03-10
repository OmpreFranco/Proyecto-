
import clase_Animal
import numpy as np

 
class Ambiente(object):
    """
    La clase **Ambiente** crea el universo donde van a interactuar los animalitos.
    
    """
    def __init__(self,lim=None,number_of_agents=None,agents=None):
        """
        Args: 
            lim (list): lista de dos elementos que define los bordes del universo bidimensional y plano.
            number_of_agents (int): umero de agentes que tiene el ambiente, por default es 10.
            agents (list): lista con los objetos que representan los animales, se puede pasar
                           al momento de instanciar la clase y si no por default llama a 
                           func:'self.add_agents' que agrega agentes de forma aleatoria.
        """
        self.lim=lim
        self.agents=agents
        self.number_of_agents=number_of_agents
        
        if lim is None:
            lim=[1.0,1.0]
        
        if agents is None:
            self.agents=[]
            if number_of_agents is None:
                self.number_of_agents=10
            self.add_agents()
    def limits(self):
        """
        Este metodo devuelve los valores limites del Ambiente        
        """
        return self.lim


        
    def time_step(self):
        """
        Este metodo adelanta la simulacion un paso llamando a :func:'self.detect_targets', 
        :func:'self.move_agents', :func:'self.update'
        """
        self.detect_targets_and_move()
        self.update()
        

    def detect_targets_and_move(self):
        """
        Este metodo llama a :func:'scout' de la clase Animal para cada agente de la lista.
        """
        for agent in self.agents:
            objetivo = agent.scout(self.agents)
            agent.move(objetivo,self)

    def update(self):
        """
        Este metodo busca todos los agentes cuya vida es igual a 0 y los elimina de la lista de agentes.
        """
#        while agent.life == 0 in self.agents: self.agents.remove(agent)
        for agent in self.agents:
            if (agent.life == 0):
                self.agents.remove(agent)

    def add_agents(self):
        """ 
        Este metodo agrega objetos de la clase Animal a la lista agents de la clase ambiente.
        Esta es una forma de agregar agentes al ambiente, puede haber alternativas. En este caso
        la posicion, el radio de vision y la velocidad se dan como numeros aleatorios entre 0 y 1.
        La vida (life) la inicializamos siempre en 1.0 y la agresividad puede tomar los valores 0 o 1.
        Es decir, los animales no son agresivos en absoluto (0) o son completamente agresivos (1). 
        En radio_vision le pongo un offset 0.01 para que no sea ciego el tipo.
        En vel le pongo el mismo offset y el numero aleatorio lo multiplico por radio_vision asi no
        camina mas distancia de la que ve.
        """
        for i in range(self.number_of_agents):
                radio_vision=np.random.random(1)+0.01
                position=[np.random.random(1)*self.lim[0],np.random.random(1)*self.lim[1]]
                vel=np.random.random(1)*radio_vision+0.01
                life=1.0
                agresividad=np.random.randint(0,2)
                agent=clase_Animal.Animal(radio_vision, position , vel,  life,  agresividad)
                self.agents.append(agent)
                