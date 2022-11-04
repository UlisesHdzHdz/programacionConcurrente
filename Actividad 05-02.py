import math
import threading
import queue
import time
from random import choice, randint

clientesRestaurante = 10
capacidadRestaurante = 5
meserosRestaurante = math.ceil(capacidadRestaurante * 0.1) if capacidadRestaurante <= 5 else round(capacidadRestaurante * 0.1)
cocinerosRestaurante = meserosRestaurante 
reservacionMaxima = round(capacidadRestaurante * 0.2)


class AdminLocal(object):
    def __init__(self, espacio):
        self.clientes = threading.Condition()
        self.mesero = threading.Condition()
        self.cocinero = threading.Condition()
        self.recepcion = threading.Condition()
        self.espacio = espacio
        self.aux = threading.Lock()
        self.reservaciones = queue.Queue(reservacionMaxima)
        self.nCustomers = queue.Queue(self.espacio)
        self.ordenes = queue.Queue()
        self.ordenes_plato = queue.Queue()
        self.comida = queue.Queue()
    # reserva un lugar en para el cliente
    def reservePlace(self, comensal):
        self.recepcion.acquire()
        if self.reservaciones.full():
            self.recepcion.wait()
        else:
            print(f"Comensal {comensal.id} hizo una reservación")
            self.reservaciones.put(comensal)
            time.sleep(1)
        self.aux.acquire()
        self.entrar(comensal)
        self.reservaciones.get()
        self.recepcion.notify()
        self.recepcion.release()
    # cola de clientes
    def cola(self, comensal):
        self.recepcion.acquire()
        print(f"Comensal {comensal.id} se formó en la cola")
        time.sleep(1)
        self.aux.acquire()
        self.entrar(comensal)
        self.recepcion.notify()
        self.recepcion.release()

   #entrada de clientes
    def entrar(self, comensal):
        self.clientes.acquire()
        if self.nCustomers.full():
            print(f"Comensal {comensal.id} esperando a que haya lugar")
            self.clientes.wait()
        else:
            print(f"Comensal {comensal.id} entra al restaurante")
            self.nCustomers.put(comensal)
            print(
                f"Comensal {comensal.id} se prepara para ordenar")
            self.mesero.acquire()
            self.mesero.notify()
            self.mesero.release()
            self.aux.release()
            self.clientes.release()
    #para que coma el cliente sus tamal
    def nowEat(self):
        if not self.comida.empty():
            comensal = self.comida.get()
            comensal_id = list(comensal.keys())[0]
            comensal_plato = list(comensal.values())[0]
            print(f"Comensal {comensal_id} está comiendo {comensal_plato}")
            time.sleep(randint(1, 5))
            print(f"Comensal {comensal_id} terminó de comer")
            print(f"Comensal {comensal_id} ha salido")
   #solicitud de tamales por los clientes
    def newOrden(self, mesero):
        while True:
            self.mesero.acquire()
            if self.nCustomers.empty():
                self.mesero.wait()
                print(f"Mesero {mesero} esta descansando")
            else:
                comensal = self.nCustomers.get()
                if comensal.orden == False:
                    plato = MenuTamales()
                    print(f"Mesero {mesero} tomo la orden del cliente {comensal.id} que comerá {plato.menuAlimentos}")
                    time.sleep(1)
                    self.ordenes.put({comensal.id: plato.menuAlimentos})
                    self.cocinero.acquire()
                    self.cocinero.notify()
                    self.cocinero.release()
                    comensal.orden = True
                    self.mesero.release()
                else:
                    self.mesero.release()
# cosina el tipo de tamal solicitado
    def nowCook(self, id):
        while True:
            self.cocinero.acquire()
            if self.ordenes.empty():
                self.cocinero.wait()
                print(f"Cocinero {id} esta descansando")
            else:
                comensal = self.ordenes.get()
                comensal_id = list(comensal.keys())[0]
                comensal_plato = list(comensal.values())[0]
                print(f"Cocinero {id} está cocinando la orden del comensal {comensal_id}: {comensal_plato}")
                time.sleep(1)
                self.comida.put(comensal)
                self.cocinero.release()

   # menu de tamales existentes
class MenuTamales():
    arryTamales = ["tamal de bola", "tamal de chipilin", "tamal de cambray","tamal de hoja de milpa", "tamal de elote", "Tamal de frijole"]

    def __init__(self):
        self.menuAlimentos = choice(self.arryTamales)

    # comensales o clientes 
class Comensal(threading.Thread):
    def __init__(self, id, AdminLocal):
        threading.Thread.__init__(self)
        self.id = id
        self.orden = False
        self.restaurant = AdminLocal

    def run(self):
        reserva = randint(0, 1)
        if reserva == 1:
            self.restaurant.reservePlace(self)
        if reserva == 0:
            self.restaurant.cola(self)
        self.restaurant.nowEat()

   #meseros 
class Mesero(threading.Thread):
    def __init__(self, id, AdminLocal):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = AdminLocal

    def run(self):
        self.restaurant.newOrden(self.id)

    #cosineros
class Cocinero(threading.Thread):
    def __init__(self, id, AdminLocal):
        threading.Thread.__init__(self)
        self.id = id
        self.restaurant = AdminLocal

    def run(self):
        self.restaurant.nowCook(self.id)


def main():
    restaurant = AdminLocal(capacidadRestaurante)
    clientes = []
    meseros = []
    cocineros = []

    for x in range(clientesRestaurante):
        clientes.append(Comensal(x+1, restaurant))
    for comensal in clientes:
        comensal.start()

    for x in range(meserosRestaurante):
        meseros.append(Mesero(x+1, restaurant))
    for mesero in meseros:
        mesero.start()

    for x in range(cocinerosRestaurante):
        cocineros.append(Cocinero(x+1, restaurant))
    for cocinero in cocineros:
        cocinero.start()


if __name__ == "__main__":
    main()

    