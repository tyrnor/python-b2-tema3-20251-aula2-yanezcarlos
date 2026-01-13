"""
Enunciado:

En este ejercicio práctico, aprenderás a utilizar el módulo itertools de Python, enfocándote
en la función product para generar combinaciones de contraseñas. Se te proveerá un conjunto
limitado de caracteres, incluyendo letras mayúsculas, minúsculas, dígitos y símbolos especiales.
Tu objetivo será utilizar estas letras para crear todas las posibles combinaciones de contraseñas
de una longitud específica.

Instrucciones:
    - Define una función generate_passwords() que acepte los siguientes parámetros: conjuntos de 
    caracteres que incluyan letras mayúsculas ('AZ'), letras minúsculas ('xy'), dígitos ('09') y
    símbolos especiales ('@#'), y la longitud deseada de las contraseñas.
    - Dentro de la función, utiliza la función product de itertools para generar todas las posibles 
    combinaciones de estos caracteres, formando contraseñas de la longitud especificada.
    - Convierte cada combinación de caracteres de las contraseñas generadas en una cadena y 
    almacénalas en una lista.
    - Retorna la lista de contraseñas generadas.
    - Fuera de la función, llama a generate_passwords() con los parámetros adecuados y almacena el 
    resultado.
    - Calcula y muestra el número total de contraseñas generadas.
    - Imprime las primeras 10 contraseñas de la lista para verificar tu solución.

Salida esperada:
    Number of passwords generated: 4096
    First 10 passwords generated: ['AAAA', 'AAAB', 'AAAC', 'AAAD', 'AAAx', 'AAAy', 'AAAz',
    'AAA0', 'AAA1', 'AAA2']
"""

import itertools
from typing import List


def generate_passwords(password_length: int) -> List[str]:
    uppercase_letters = 'AZ'
    lowercase_letters = 'xy'
    digits = '09'
    special_symbols = '@#'
    characters = uppercase_letters + lowercase_letters + digits + special_symbols
    possible_passwords = itertools.product(characters, repeat= password_length) 
    password_list_joined = [''.join(password) for password in possible_passwords]
    return password_list_joined


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     PASSWORD_LENGHT = 4
#     password_list = generate_passwords(PASSWORD_LENGHT)
#     print(f"Number of passwords generated: {len(password_list)}")
#     print("First 10 passwords generated:", password_list[:10])
