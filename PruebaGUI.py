#-*- coding:utf-8 -*-
from Tkinter import *
import os, sys
from PIL import Image
import time



#funciones de procesamiento
def simular():
    TiempoLimite =varTiempoLimite.get()
    xMax =varXmax.get()
    yMax =varYmax.get()
    cantAnimales = varCantAnimales.get()

    #Resto de la simulacion
    print(type(TiempoLimite))
    print(xMax)
    print(yMax)
    print(cantAnimales) 
    global ventana
    ventana.quit() 
	


#Programa principal

#Instancia de la clase Tk
ventana = Tk()
ventana.title('Simulacion SURVIVAL')
#ventana.configure(background='black')

#Variables que almacenarán los datos
varTiempoLimite = IntVar()
varXmax = IntVar()
varYmax = IntVar()
varCantAnimales = IntVar()

#generación de widgets
#TiempoLimite
etiqueta_TiempoLimite = Label(ventana, text='Tiempo Limite:')
entrada_TiempoLimite = Entry(ventana, textvariable=varTiempoLimite)
etiqueta_TiempoLimite.grid(row=1, column=1)
entrada_TiempoLimite.grid(row=1, column=2)


#xMax
etiqueta_xMax = Label(ventana, text='xMax')
entrada_xMax = Entry(ventana, textvariable=varXmax)
etiqueta_xMax.grid(row=2, column=1)
entrada_xMax.grid(row=2, column=2)

#yMax
etiqueta_yMax = Label(ventana, text='yMax')
entrada_yMax = Entry(ventana, textvariable=varYmax)
etiqueta_yMax.grid(row=3, column=1)
entrada_yMax.grid(row=3, column=2)

#cantAnimales
etiqueta_cantAnimales = Label(ventana, text='cantAnimales')
entrada_cantAnimales = Entry(ventana, textvariable=varCantAnimales)
etiqueta_cantAnimales.grid(row=4, column=1)
entrada_cantAnimales.grid(row=4, column=2)

#boton
botonSimular = Button(ventana, text='Simular', command=simular, width=20)
botonSimular.grid(row=8, column=3)




#ejecución de ventana
ventana.mainloop()
