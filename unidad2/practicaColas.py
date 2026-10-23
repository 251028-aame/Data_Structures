from collections import deque
import time 
cola_turnos =deque()


cola_turnos.append(" Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append(" Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append(" Turno A03 - JUANA LAZCANO RODRIGUEZ")

print("Turnos emitidos en la fila del banco: ")
for turno in cola_turnos:
    print(" -", turno)
print("")
print("Iniciando atención en ventanilla")
print("")
#EL REPODUCTOR PROCESA LA COLA CANCION POR CANCION (DESENCOLAR)
while cola_turnos:
    turno_actual=cola_turnos.popleft()
    print(f"Llamando a ventanilla: {turno_actual}")
    time.sleep(1) #simula la duración dle tema
    print(f"Atención finalizada: {turno_actual}")
    #Muestran cunatas canciones quedan en la cola 
    print(f"(Clientes restantes en la fila: {len(cola_turnos)})")
    print("")
print("Se han atendido todos los turnos. Fila vacía")