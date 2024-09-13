"""
Resolución de ejercicio 1 --> Algoritmos
"""

#Defino la colección de números brindada en el enunciado
elements = [1,10,6,8,15,2]

#Defino una función común para poder imprimir los resultados de cada inciso del ejercicio
def print_results(title, result):
    print(f"\n{title}: ") 
    print(result)


# 1a) Determinar el número mayor de la colección y su posición sin usar funciones específicas del lenguaje
def max_num(elements):
    max = elements[0]
    pos = 0
    for i in range(1, len(elements)):
        if elements[i] > max:
            max = elements[i]
            pos = i
    return max, pos
  
max_number, position = max_num(elements)
print_results("1a) Mayor número y su posición (sin utilizar funciones específicas)", f"El número mayor es {max_number} y se encuentra en la posición {position}")


# 1b) Determinar el número mayor de la colección y su posición utilizando funciones específicas del lenguaje
max_number = max(elements)
position = elements.index(max_number)
print_results("1b) Mayor número y su posición (utilizando funciones específicas)", f"El número mayor es {max_number} y se encuentra en la posición {position}")


# 2) Ordenar la lista de números (elijo forma ascendente por default)
ordered_elements = sorted(elements) #No utilizo la función sort() para no modificar la lista original
print_results("2) Lista ordenada de forma ascendente", ordered_elements)

"""
Otra forma (más lógica) de resolver el ejercicio 2):

def order_list(elements):
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            if elements[i] > elements[j]:
                elements[i], elements[j] = elements[j], elements[i]
    return elements

print_results("2) Lista ordenada de forma ascendente", order_list(elements))
"""


# 3) Determinar cuáles números son pares y en qué posiciones se encuentran
def even_number(elements):
    even_numbers = []
    for i,num in enumerate(elements): #Utilizo la función específica de python enumerate para obtener el índice de cada número
        if num % 2 == 0:
            even_numbers.append((num, i))
    return even_numbers
  
even_numbers = even_number(elements)
print_results("3) Números pares y sus posiciones", even_numbers)


# 4) Crear un nuevo arreglo con todos los números pares
# Elijo utilizar el arreglo del inciso 3 para no tener que recorrer la lista original nuevamente
new_array = [num for num, _ in even_numbers] #Utilizo comprensión de listas para obtener los números pares, el _ es para no guardar el índice
print_results("4) Nuevo arreglo con todos los números pares", new_array)
