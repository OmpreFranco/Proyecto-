#----------------------------------------------
#==============================================================================
# Importar las clases de los archivos .py 
#==============================================================================
import landscape
import clase_Animal
#==============================================================================
#==============================================================================
#Programa principal 
#==============================================================================
#==============================================================================

# Impongo el limite del ambiente
limite = [30, 30]

#Ejemplo de creacion de animales a mano:
#animales=[clase_Animal.Animal(100.0, [4.0,4.0], 2.0, 1.0, 1.0), clase_Animal.Animal(1.0, [10.0,10.0],1.0,1.0, 0.0)]

# Creo el objeto ecosistema de la clase ambiente 
ecosistema = landscape.Ambiente(limite,30)#agents=animales) 
ecosistema.run(TiempoLimite=500)

#for i in range(300):
#    ecosistema.time_step()