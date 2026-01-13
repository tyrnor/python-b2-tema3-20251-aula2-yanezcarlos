"""
Descripción:
Implementarás una función que aplica descuentos a precios de productos. Utilizando functools.partial,
crearás dos versiones especializadas de esta función: una para clientes VIP con un descuento del 20%,
y otra para nuevos clientes con un descuento del 10%. Este ejercicio te enseñará cómo simplificar tu
código y hacerlo más reutilizable con partial.

Instrucciones:
    - Crear Función de Descuento: Define apply_discount(), que toma un precio y un porcentaje de descuento,
    retornando el precio después del descuento.
    - Especializar con partial: Usa partial para crear vip_discount y new_customer_discount, preconfigurados 
    on descuentos del 20% y 10% respectivamente.
    - Demostrar su Uso: Calcula y muestra los precios finales para un cliente VIP y un nuevo cliente,
    partiendo de un precio original de 100.

Salida Esperada:
    Original Price: 100
    VIP Price: 80
    New Customer Price: 90
"""


from functools import partial


def apply_discount(price: float, discount: float) -> float:
    """Applies a discount to the price and returns the final price."""
    # Write here your code
    return price * (1 - discount / 100)


vip_discount = partial(apply_discount, discount= 20)
new_customer_discount = partial(apply_discount, discount= 10)


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     original_price = 100
#     vip_price = vip_discount(original_price)
#     new_customer_price = new_customer_discount(original_price)

#     print(f"Original Price: {original_price}")
#     print(f"VIP Price: {vip_price}")
#     print(f"New Customer Price: {new_customer_price}")
