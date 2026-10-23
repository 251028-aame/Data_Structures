historial_peliculas=[]
#OPREACION PARA APILAR PUSH
historial_peliculas.append("Mamma mia!")
historial_peliculas.append("Demolition")
historial_peliculas.append("Chihiro")
historial_peliculas.append("Mulan")
historial_peliculas.append("27 bodas")
historial_peliculas.append("Spider-Man")
historial_peliculas.append("La La Land")
historial_peliculas.append("Orgullo y prejuicio")
historial_peliculas.append("School of rock")
historial_peliculas.append("Y tu mamá también")
print("Historial de películas:", historial_peliculas)

#OPERACION (TOP-PEEK)
pelicula_actual=historial_peliculas[-1]
print("Pelicula pendiente:", pelicula_actual)
print()

#OPERACION PARA DESAPILAR (POP)

print("Pelicula vista:", historial_peliculas.pop())
print("Pelicula vista:", historial_peliculas.pop())
print("Pelicula vista:", historial_peliculas.pop())
print("Pelicula vista:", historial_peliculas.pop())

print()

#"OPERACION TAMAÑO (SIZE)"
total_peliculas=len(historial_peliculas)
print("películas por ver: ", total_peliculas)
print(historial_peliculas)
print()

#OPERACION VACIA (EMPTY)
sin_peliculas=len(historial_peliculas)==0
print("¿El historial esta vacio?: ", sin_peliculas)