# 1.- Ocho Personas están sentados en una mesa . Cada Persona tiene un plato  y un palillo a la izquierda de su plato. 
# 2.- Para comer  son necesarios dos palillos y cada persona sólo puede tomar el palillo que está a su izquierda y el de su derecha.
# 3.- Si cualquier persona toma un palillo y el otro está ocupado, se quedará esperando, con el palillo en la mano, hasta que pueda tomar el otro palillo, para luego empezar a comer. 
# 4.- El resto de personas que no está ni comiendo ni con un palillo en la mano está a la espera.



# Resultado: El problema consiste en inventar un algoritmo que permita comer a todas las personas y cada uno de ellos se vaya compartiendo un palillo.

# Nota: Para este examen tendrá que aplicar el concepto de acquire() y release()

from threading import Semaphore
import threading
import time
 
semaforo = Semaphore(1)
palillosList = [1,1,1,1,1,1,1,1] 
palillo = []

def comer():
    hilo = threading.current_thread().getName()
    while True:
        semaforo.acquire()
        if len(palillosList) != 0:
            print('El comensal ',hilo ,'tiene dos palillos')
            time.sleep(1)
            palillo.append(palillosList.pop())
            palillo.append(palillosList.pop())
        try:
            if len(palillo) == 2:
                print('El comensal ',hilo,'ha empezado a comer')
                time.sleep(2)
                palillosList.append(palillo.pop())
                palillosList.append(palillo.pop())
        finally:
            print('El comensal ',hilo,'ha terminado de comer')
            time.sleep(2)
            semaforo.release()
            break
    print(threading.active_count()-2,'comensal  esperando (cola)' )
    print()
    time.sleep(2)

if __name__ == '__main__':

    threading_1 = threading.Thread(name='ali', target=comer, args=())
    threading_2 = threading.Thread(name='Martha', target=comer, args=())
    threading_3 = threading.Thread(name='Luis', target=comer, args=())
    threading_4 = threading.Thread(name='Oliver', target=comer, args=())
    threading_5 = threading.Thread(name='Dorian', target=comer, args=())
    threading_6 = threading.Thread(name='Manuel', target=comer, args=())
    threading_7 = threading.Thread(name='Jose', target=comer, args=())
    threading_8 = threading.Thread(name='Alejandra', target=comer, args=())
 
    threading_1.start()
    threading_2.start()
    threading_3.start()
    threading_4.start()
    threading_5.start()
    threading_6.start()
    threading_7.start()
    threading_8.start()

    threading_1.join()
    threading_2.join()
    threading_3.join()
    threading_4.join()
    threading_5.join()
    threading_6.join()
    threading_7.join()
    threading_8.join()

