# crear una aplicasion con las suiguientes caracteristicas:
# existe uno o mas productores y uno o mas consumidores,todos almacenan y extraen productos de una misma bodega.
# el productor produce productos cada vez que lo necesita.

# problema:
# coordinar a los productores y consumidores, para que los productores no produzcan mas items  de los que se pueden 
# almacenar en el momento , y los consumidores no adquieran mas items de los que hay disponibles.

import threading
import random
import time

a = threading.Semaphore(5) 
b = threading.Semaphore(0) 
c = threading.Semaphore(1) 
d = 5

buffer = list()

def productor ():
    x = 0
    while x < d :
        dato = random.randint(1, 10)
        a.acquire()
        c.acquire()
        print("<------------------------------------")
        print("Agregando datos en la posision ( Productor ):", len(buffer)+1 )
        print(a._value, c._value)
        print("Dato guardado: ", dato )
        buffer.append(dato)
        x = x + 1
        c.release()
        b.release()
        #time.sleep(2)
        print("------------------------------------>")

def consumidor ():
    x = 0
    while x < d:
        b.acquire()
        c.acquire()
        print("")
        print("-> Eliminando datos en la posision ( Consumidor ):", len(buffer)-1)
        print(a._value, c._value)
        print("Dato eliminado: ", buffer.pop())
        x = x + 1
        c.release()
        a.release()
        

if __name__ == "__main__":

    threading_productor = threading.Thread(target=productor)
    threading_consumidor = threading.Thread(target=consumidor)
    threading_productor.start()
    threading_consumidor.start()
    