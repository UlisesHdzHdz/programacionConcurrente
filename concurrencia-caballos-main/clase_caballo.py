import threading
import time
import random
from multiprocessing.pool import ThreadPool

from PyQt5 import QtCore, QtGui, QtWidgets

bandera = False

val1 = ""
msg = 'Caballo ganador es: {}'
# Clase Caballo

class caballo(threading.Thread):
    
    def __init__(self, num, b1,resultado):
      global val1,bandera
      threading.Thread.__init__(self)
      bandera = False
      self.resultado = 20.0
      self.tiempo_inicio = time.time()
      self.tiempo_final = ""
      self.tiempo_total = ""
      self.num = num
      self.valor = 0
      self.boton = b1
      self.eleccion= ""


# Selecciona un valor aleatorio, 10 20 o 30
    def aleatorio(self):

        mylist = ["10","20","30","40"]

        self.eleccion = random.choice(mylist)
        
# Movimiento de los caballos

    def movimiento(self):

        self.p = self.boton.pos()
        self.p += QtCore.QPoint(int(self.eleccion), 0)

        self.valor += int(self.eleccion)

        self.boton.move(self.p)
        time.sleep(0.75)

    def retorno(self):
        self.resultado

# Hilos

    def run(self):
      global bandera
      while(True):

          if bandera == True:
            break
          else:

            self.aleatorio()
            self.movimiento()

          if self.valor >= 600:
            self.tiempo_final = time.time()
            self.resultado = self.tiempo_final-self.tiempo_inicio  
            print("\nEl caballo: " + str(self.num)+" cruzó la meta!!, Tiempo: "+str(self.resultado))
            bandera=True
            break

