
import clase_Animal
import numpy as np

from matplotlib import  pyplot as plt
from matplotlib.animation import FuncAnimation
 
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
        for agent in self.agents:
            agent.move(agent.objetivo,self)

        self.left_life()

    def update(self):
        """
        Este metodo busca todos los agentes cuya vida es igual a 0 y los elimina de la lista de agentes.
        """
#        while agent.life == 0 in self.agents: self.agents.remove(agent)
        for agent in self.agents:
            if (agent.life <= 0):
                self.agents.remove(agent)

    def left_life(self):
        for agent in self.agents:
            agent.life-= .5
	
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
                radio_vision=np.random.randint(1,6)#np.random.random(1)+0.01
                position=[np.random.random(1)*self.lim[0],np.random.random(1)*self.lim[1]]
                vel=np.random.random(1)*radio_vision+1
                life=np.random.randint(100,310)
                agresividad=np.random.randint(0,6)/4
                agent=clase_Animal.Animal(radio_vision, position , vel,  life,  agresividad)
                self.agents.append(agent)
                
    def run(self,TiempoLimite):
        
        fig, ax = plt.subplots()
        ax.set_xlim([0,self.lim[0]])
        ax.set_ylim([0,self.lim[1]])
        
        ani=FuncAnimation(fig, self.frame_update, frames=range(TiempoLimite), interval=20, blit=True, fargs=[ax])
        plt.show()
    
    def frame_update(self,frame,ax):
        self.time_step()  

        xprey, yprey = [], []
        xpred, ypred = [], []

        data_prey, = ax.plot([], [], 'ro', markersize=10.0, animated=True)
        data_pred, = ax.plot([], [], 'b+', markersize=10.0, animated=True)

        for agent in range(len(self.agents)):
            if (self.agents[agent].agresividad == 1):
                xpred.append(self.agents[agent].position[0])
                ypred.append(self.agents[agent].position[1])
            else:
                xprey.append(self.agents[agent].position[0])
                yprey.append(self.agents[agent].position[1])
        
        data_prey.set_data(xprey,yprey)
        data_pred.set_data(xpred,ypred)
        
        return [data_prey, data_pred,]
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        