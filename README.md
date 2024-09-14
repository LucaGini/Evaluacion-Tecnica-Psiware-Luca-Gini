# Evaluacion-Tecnica-Psiware-Luca-Gini

Este repositorio contiene las soluciones a los dos ejercicios propuestos durante la entrevista técnica del día 13/09/2024 por la empresa Psiware realizados por el candidato Luca Gini. Los mismos cubren temas de algoritmos y modelado de objetos, y el desarrollo fue llevado a cabo utilizando el lenguaje Python.

## Estructura del Repositorio

- `Ejercicio_1_Algoritmos/ejercicio_1.py`: Contiene las soluciones al Ejercicio 1.
- `Ejercicio_2_Modelado/ejercicio_2.py`: Archivo principal para el Ejercicio 2.
- `Ejercicio_2_Modelado/classes.py`: Define las clases utilizadas en el Ejercicio 2.
- `Ejercicio_2_Modelado/db.py`: Maneja la interacción con la base de datos SQLite para el Ejercicio 2.

## Ejercicio 1: Algoritmos

Este ejercicio se enfoca en manipulación de listas y operaciones básicas de algoritmos.

### Funcionalidades implementadas:

1. Encontrar el número mayor y su posición:
   - Sin usar funciones específicas del lenguaje.
   - Usando funciones específicas del lenguaje.
2. Ordenar la lista de números.
3. Determinar los números pares y sus posiciones.
4. Crear un nuevo arreglo con todos los números pares.

### Cómo ejecutar:

```
python ejercicio_1.py
```

## Ejercicio 2: Modelado

Este ejercicio implementa un sistema simple de gestión de biblioteca utilizando la librería SQLite3 para persistencia de datos.

### Clases principales:

- `Book`: Representa un libro con atributos como ISBN, nombre, autor, género, precio y estante (integridad referencial).
- `Shelf`: Representa un estante con métodos para agregar libros, contar libros, calcular porcentaje de llenado, etc.
- `Database`: Maneja la interacción con la base de datos SQLite.

### Cómo ejecutar:

```
python ejercicio_2.py
```

### Funcionalidades:

- Creación y carga de estantes y libros desde/hacia la base de datos.
- Cálculo de estadísticas como número de libros, porcentaje de llenado, valor total de los libros.
- Búsqueda del libro más caro.
- Ordenamiento alfabético de libros.
- Filtrado de libros por género.

## Notas adicionales

- El sistema utiliza SQLite para la persistencia de datos, lo que permite mantener la información entre ejecuciones.
- Se han utilizado dataclasses para simplificar la definición de las clases `Book` y `Shelf`.
- El código incluye manejo básico de errores.

## Áreas de mejora

- Implementar más funcionalidades de búsqueda y filtrado.
- Agregar tests para asegurar el correcto funcionamiento de las clases y métodos.
- Mejorar la interfaz de usuario, posiblemente implementando una GUI simple.
