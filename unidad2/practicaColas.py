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

while cola_turnos:
    turno_actual=cola_turnos.popleft()
    print(f"Llamando a ventanilla: {turno_actual}")
    time.sleep(1) #(1) significa la duracion de un segundo para simular el turno
    print(f"Atención finalizada: {turno_actual}")
    print(f"(Clientes restantes en la fila: {len(cola_turnos)})")
    print("")
print("Se han atendido todos los turnos. Fila vacía")