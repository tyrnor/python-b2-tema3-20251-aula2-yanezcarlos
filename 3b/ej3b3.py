"""
Enunciado:
Desarrolla una clase en Python que actúe como una fábrica de decoradores para el registro de
logs, diseñada para facilitar el monitoreo de diferentes aspectos de la ejecución de funciones.
Esta clase, llamada DecoratorFactoryLogs, debe ofrecer tres tipos de decoradores: uno para
registrar el inicio y fin de ejecuciones de funciones, otro para detalles de depuración, y un
tercer decorador que permite guardar los registros en un archivo de log personalizado.

Implementación de la Clase DecoratorFactoryLogs:
    - log_decorator: Crea un decorador que registre cuando una función inicia y termina su
    ejecución, incluyendo el nombre de la función, argumentos y valores de los argumentos pasados.
    - debug_log_decorator: Desarrolla un decorador que registre información detallada útil para
    la depuración, incluyendo una representación textual de los argumentos y valores de los kwargs
    pasados a la función.
    - save_log_decorator: Crea un decorador que registre información en un archivo personalizado,
    especificado a través de un parámetro en el decorador. Este decorador debe ser capaz de crear
    y utilizar un logger específico para la función decorada.

Uso de Decoradores:
    - Aplica el Log Decorator a la función creada llamada add(a, b) que suma dos números.
    - Utiliza el Debug Log Decorator en la función subtract(a, b) que resta el segundo número del primero.
    - Emplea el Save Log Decorator en una función multiply(a, b) que multiplica dos números y guarda los
    registros en un archivo de log personalizado.

Ejemplo de Uso:

factory = DecoratorFactoryLogs()
@factory.log_decorator(message="Log Decorator:")
def add(a, b):
    return a + b
    
Salida esperada:
    2021-08-25 12:00:00,000 - INFO - Log Decorator: Starting: add with args: (2, 3), kwargs: {}
    2021-08-25 12:00:00,000 - INFO - Log Decorator: Finishing: add
"""


import logging
from functools import wraps
from typing import Callable, Any
import os

# Ensuring the directory for logs exists
log_directory: str = "data/output/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_directory, "app.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DecoratorFactoryLogs:
    def log_decorator(self, message: str = "") -> Callable:
        """
        Decorator that logs the start and end of the execution of the function.
        """

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                logging.info(
                    f"{message} Starting: {func.__name__} with args: {args}, kwargs: {kwargs}"
                )
                result = func(*args, **kwargs)
                logging.info(f"{message} Finishing: {func.__name__}")
                return result

            return wrapper

        return decorator

    def debug_log_decorator(self, message: str = "") -> Callable:
        """
        Decorator that logs detailed information useful for debugging.
        """

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                signature = ",".join(args_repr + kwargs_repr)
                logging.debug(f"{message} Executing: {func.__name__}({signature})")
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def save_log_decorator(
        self,
        message: str = "",
        filepath: str = os.path.join(log_directory, "custom_log.log"),
    ) -> Callable:
        """
        Decorator that logs information to a custom log file.
        """

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                custom_logger = logging.getLogger(func.__name__)
                handler = logging.FileHandler(filepath)
                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
                handler.setFormatter(formatter)
                custom_logger.addHandler(handler)
                custom_logger.setLevel(logging.INFO)
                custom_logger.info(
                    f"{message} Executing: {func.__name__} with args: {args}, kwargs: {kwargs}"
                )
                result = func(*args, **kwargs)
                custom_logger.removeHandler(handler)  # Clean up handler
                handler.close()
                return result

            return wrapper

        return decorator


factory = DecoratorFactoryLogs()


@factory.log_decorator(message="Log Decorator:")
def add(a: int, b: int) -> int:
    return a + b


@factory.debug_log_decorator(message="Debug Decorator:")
def subtract(a: int, b: int) -> int:
    return a - b


@factory.save_log_decorator(
    message="Custom Log Decorator:",
    filepath=os.path.join(log_directory, "custom_operation.log"),
)
def multiply(a: int, b: int) -> int:
    return a * b

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     print("Addition:", add(2, 3))
#     print("Subtraction:", subtract(10, 5))
#     print("Multiplication:", multiply(2, 4))
#     print("Logs saved in:", log_directory)
