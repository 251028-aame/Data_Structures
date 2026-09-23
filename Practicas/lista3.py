frutas=["Manzana","platano","uva"]
primer_elemento=frutas[0]
#print(primer_elemento)
#Actualizar
frutas[1]= "pera"
#Agregar valores
frutas.append("sandia")
frutas.insert(2, "mango")
frutas.extend(["melon","fresa","kiwi"])

#Eliminar
retirado=frutas.pop(2)
#Elimina el ultimo elemento
ultimo=frutas.pop()
#Elimina elemento en su primera aparicion
frutas.remove("uva")
#Borrar casilla directamente
del frutas[0]
#print(frutas)

#Busqueda
#la f en python hace referencia a que dentro del texto se van a colocar variables usando llaves
if "sandia" in frutas:
    pos=frutas.index("sandia")
    print(f"La sandia esta en la casilla {pos}")
    print(frutas)