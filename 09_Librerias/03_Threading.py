# GITHUB: https://github.com/AlejandroMolinosEligio/CursoPythonCeroToAvanzado

############################
###       THREADING     ####
############################

### 1. Crear y ejecutar un hilo simple

import threading
import time

def tarea():
    print("Hilo iniciado")
    time.sleep(2)
    print("Hilo terminado")

# Crear un hilo
hilo = threading.Thread(target=tarea)

# Iniciar el hilo
hilo.start()

# Esperar a que el hilo termine
hilo.join()

print("Programa principal terminado")

### 2. Hilos con argumentos

def tarea(nombre, duracion):
    print(f"Hilo {nombre} iniciado")
    time.sleep(duracion)
    print(f"Hilo {nombre} terminado")

# Crear hilos con argumentos
hilo1 = threading.Thread(target=tarea, args=("A", 2))
hilo2 = threading.Thread(target=tarea, args=("B", 3))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Programa principal terminado")

### 3. Usar subclases de Thread

class MiHilo(threading.Thread):
    def __init__(self, nombre, duracion):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.duracion = duracion

    def run(self):
        print(f"Hilo {self.nombre} iniciado")
        time.sleep(self.duracion)
        print(f"Hilo {self.nombre} terminado")

# Crear instancias de la subclase de Thread
hilo1 = MiHilo("A", 2)
hilo2 = MiHilo("B", 3)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Programa principal terminado")

### 4. Usar Lock para evitar condiciones de carrera

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    with lock:
        local_contador = contador
        local_contador += 1
        time.sleep(0.1)
        contador = local_contador
        print(f"Contador incrementado a {contador}")

hilos = []

# Crear 10 hilos que incrementan el contador
for i in range(10):
    hilo = threading.Thread(target=incrementar)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print(f"Valor final del contador: {contador}")

### 5. Usar Semaphore para limitar el número de hilos concurrentes

semaforo = threading.Semaphore(3)

def tarea(id):
    with semaforo:
        print(f"Hilo {id} iniciado")
        time.sleep(2)
        print(f"Hilo {id} terminado")

hilos = []

# Crear 10 hilos
for i in range(10):
    hilo = threading.Thread(target=tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Programa principal terminado")

### 6. Usar Event para la sincronización entre hilos

evento = threading.Event()

def tarea():
    print("Esperando a que el evento sea activado")
    evento.wait()
    print("Evento activado, continuando con la tarea")

hilo = threading.Thread(target=tarea)
hilo.start()

time.sleep(3)
print("Activando el evento")
evento.set()

hilo.join()

print("Programa principal terminado")