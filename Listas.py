print("")
print("Zamarripa Castro Erick Fabián")
print("Practica de listas: Probando distintos tipos de listas")
print("")

thislist = ["Dame", "Un", "Dedazo de ese chocolate"] # Crea una lista simple y la imprime
print(thislist)

thislist2 = ["Se", "Acabo", "Ese era el ultimo"] # Crea otra lista y muestra su longitud
print(len(thislist2))  # Imprime el número de elementos en thislist2

print("")

# Define varias listas de diferentes tipos de datos
list1 = ["Se", "Acabo", "Ese era el ultimo"]
list2 = [1, 2, 3]  # Lista de enteros
list3 = [True, True, True]  # Lista de booleanos
list4 = ["abc", 34, True, "male"]  # Lista con mezcla de tipos

# Imprime las listas creadas
print(list1)
print(list2)
print(list3)
print(list4)
print("")

thislist3 = list(("Pero", "Tenia tantas", "Ganas de comer chocolate")) # Crea una lista utilizando el constructor list() y la imprime
print(thislist3)
print("")

thislist5 = ["Enserio?", "Enserio", "No lo defraudare papá"] # Accede al segundo elemento de thislist5 y lo imprime
print(thislist5[1])  # Imprime "Enserio"

thislist6 = ["Enserio?", "Enserio", "No lo defraudare papá"] # Accede al último elemento de thislist6 y lo imprime
print(thislist6[-1])  # Imprime "No lo defraudare papá"

thislist7 = ["Enserio?", "Enserio", "No lo defraudare papá"] # Imprime un subarreglo de thislist7 desde el tercer al quinto elemento
print(thislist7[2:5])  # Imprime ["No lo defraudare papá"]


thislist8 = ["voy", "a hacer chocolate", "casero, me cree?"] # Imprime todos los elementos desde el inicio hasta el cuarto elemento de thislist8
print(thislist8[:4])  # Imprime todos los elementos

thislist9 = ["solo", "si", "lo veo"] # Imprime los elementos de thislist9 desde el tercer elemento en adelante
print(thislist9[2:])  # Imprime ["lo veo"]

thislist10 = ["solo", "si", "lo veo"] # Imprime el elemento en la posición -3 hasta -2 de thislist10
print(thislist10[-3:-2])  # Imprime ["solo"]

thislist11 = ["solo", "si", "lo veo"] # Verifica si el elemento "solo" está en thislist11 e imprime un mensaje
if "solo" in thislist11:
   print("Si, 'solo' esta en la lista")  # Mensaje afirmativo
