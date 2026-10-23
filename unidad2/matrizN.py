#Creacion de matriz de 3x3
matriz=[
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]
#Acceso a elementos matriz(fila)(columna)
#print(matriz[1][2]) #imprimiria fila indice 1, columna indice 2

#modificar un elemento
matriz[0][0]=100

#Recorrer la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()