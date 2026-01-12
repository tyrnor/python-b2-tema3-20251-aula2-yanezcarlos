"""
Enunciado:

En este ejercicio, trabajarás con conceptos de programación funcional en Python, específicamente
con funciones lambda y la función map. Tu tarea será realizar una conversión de temperatura de
grados Celsius a Fahrenheit.

Se te proporciona una lista de temperaturas en grados Celsius. Deberás escribir una función lambda
que convierta cada temperatura a grados Fahrenheit. Luego, utilizarás la función map para aplicar
esta conversión a toda la lista. Finalmente, imprimirás ambas listas, la original en Celsius y
la convertida en Fahrenheit, para verificar los resultados.

Instrucciones:
    - Crea una función lambda que convierta temperaturas de Celsius a Fahrenheit. La fórmula para 
    la conversión es: F = (C * 9/5) + 32
    - Utiliza la función filter para seleccionar las temperaturas en Celsius menores a 60, ya que
    los registros mayores a 60 se deben a errores en la medición.
    - Utiliza la función map para aplicar tu función lambda a una lista de temperaturas en Celsius, 
    llamada: temperatures_celsius.
    - La función map te devolverá un objeto map. Convierte este objeto a una lista utilizando la
    función list.


Ejemplo de Salida Esperada:
    Temperatures in Celsius: [0, 10, 20, 35, 45, 60]
    Temperatures in Fahrenheit: [32.0, 50.0, 68.0, 95.0, 113.0, 140.0]
"""

temperatures_celsius = [54, 84, 38, 104, 101, 107, 55, 1, 38, 31, 109, 6, 91, 46, 16, 28, 74, 102, 20, 39]
filter_temperatures_celsius = list(filter(lambda x: x < 60, temperatures_celsius))
convert_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32
temperatures_fahrenheit = list(map(convert_to_fahrenheit, filter_temperatures_celsius))

# Para probar el código, descomenta las siguientes líneas
# print("Temperatures in Celsius:", temperatures_celsius)
# print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
