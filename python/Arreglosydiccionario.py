
#Tupla-tuple: listas que no pueden modificar susu valores, agregar, quitar
amigos = ["Omar", "Beto", "German"] #los corchetes hacen que no sea tupla o sea listas
amigos.append("Clawas") 
#append agrega elementos a la lista

primerAmigo = amigos[1]
#para elegir que elemento imprimir de acuerdo a su posición

cantidadDeamigos = len(amigos)
#len muestra la cantidad de elementos en la lista (solo en py)

print(amigos[cantidadDeamigos-1]) # para imprimir el ultimo elemento sin saber cuantos hay
print(cantidadDeamigos) 
print(primerAmigo)

# Diccionarios
#Es necesario el uso de llaves

mejoresAmigos ={
    "Universidad": "Bizuet",
    "Trabajo": "Scarlett",
    "Vida": amigos
}

print(mejoresAmigos ["Vida"])