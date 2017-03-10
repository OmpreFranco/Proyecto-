
#import numpy as np 
from matplotlib import  pyplot as plt
#import math as mat
from matplotlib.animation import FuncAnimation
#from matplotlib.animation import ArtistAnimation
plt.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg'

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


fig, ax = plt.subplots()
xprey, yprey = [], []
xpred, ypred = [], []
data_prey, = ax.plot([], [], 'ro', markersize=5.0*xMax, animated=True)
data_pred, = ax.plot([], [], 'b+', markersize=5.0*xMax, animated=True)

ax.set_xlim([0,xMax])
ax.set_ylim([0,yMax])

def init_draw():
        data_prey.set_data([], [])
        data_pred.set_data([], [])
        return [data_prey, data_pred,]

def update(frame):
    ecosistema.time_step()
    for agent in range(len(ecosistema.agents)):
        if (ecosistema.agents[agent].agresividad == 1):
            xpred.append(ecosistema.agents[agent].position[0])
            ypred.append(ecosistema.agents[agent].position[1])
        else:
            xprey.append(ecosistema.agents[agent].position[0])
            yprey.append(ecosistema.agents[agent].position[1])
    data_prey.set_data(xprey,yprey)
    data_pred.set_data(xpred,ypred)
    data_prey.set_visible(True)
    data_pred.set_visible(True)
    return [data_prey, data_pred,]
    
######plt.plot(xdata, ydata, marker='+', markersize=100)
ani=FuncAnimation(fig, update, init_func=init_draw, frames=range(TiempoLimite), interval=20, blit=True, repeat=False)
#ani.save('Test.gif', dpi=80, writer='imagemagick')
plt.show()
 
#==============================================================================
# se trabajara las clases enn otros archivos que luego son importados 
#============================================================================== 