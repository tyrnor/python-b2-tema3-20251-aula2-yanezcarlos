"""
Enunciado:
Desarrolla un decorador de clase en Python que se encargue de registrar en un log cada vez
que una función es llamada, mostrando el nombre de la función, los argumentos con los que
se llamó y, opcionalmente, permitiendo desactivar estos logs mediante un parámetro. 

La clase decorador a desarrollar es: 
    - LogMethodCalls:
        Parámetros print_logs (bool): Indica si se deben imprimir los logs de las llamadas a las
        funciones decoradas.
        Métodos:
            - __init__(self, print_logs: bool): Constructor que recibe el parámetro print_logs.
            - __call__(self, func: Callable) -> Callable: Método que recibe una función y devuelve
            una función decorada que registra las llamadas a la función original.
            - __get__(self, instance, cls): Método que devuelve el decorador si se llama desde la
            clase y la función decorada si se llama desde una instancia de la clase.


Funciones existentes:
    - load_csv(filename: str) -> pd.DataFrame: Carga un archivo CSV en un DataFrame de Pandas.
    - load_and_describe_csv(filename: str) -> pd.DataFrame: Carga un archivo CSV en un DataFrame
    de Pandas y devuelve su descripción.

Ejemplo de Uso:
    dataframe = load_csv(filename)
    description = load_and_describe_csv(filename)

Salida esperada:
    INFO:root:Calling load_csv('data/german_credit_data.csv')
    INFO:root:Calling load_and_describe_csv('data/german_credit_data.csv')
"""

from pathlib import Path
import logging
from types import MethodType
from typing import Callable, Any
import pandas as pd

logging.basicConfig(level=logging.INFO)
PRINT_LOGS: bool = True


class LogMethodCalls(object):
    def __init__(self, print_logs: bool = True) -> None:
        self.print_logs: bool = print_logs

    def __call__(self, func: Callable) -> Callable:
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            if self.print_logs:
                args_repr: list[str] = [
                    repr(a) for a in args
                ]  # List of argument representations
                kwargs_repr: list[str] = [
                    f"{k}={v!r}" for k, v in kwargs.items()
                ]  # List of key=value representations
                signature: str = ", ".join(args_repr + kwargs_repr)
                logging.info("Calling %s (%s)", func.__name__, signature)
            return func(*args, **kwargs)

        return wrapped

    def __get__(self, instance: Any, cls: Any) -> Any:
        return self if instance is None else MethodType(self, instance)


@LogMethodCalls(print_logs=PRINT_LOGS)
def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


@LogMethodCalls(print_logs=PRINT_LOGS)
def load_and_describe_csv(filename: str) -> pd.DataFrame:
    dataframe: pd.DataFrame = pd.read_csv(filename)
    return dataframe.describe()


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     path_parent = Path(__file__).parent
#     FILENAME_PATH = path_parent / 'data/german_credit_data.csv'
#     dataframe_credit = load_csv(FILENAME_PATH)
#     print(dataframe_credit.head(1))
#     description = load_and_describe_csv(FILENAME_PATH)
#     print(description)
