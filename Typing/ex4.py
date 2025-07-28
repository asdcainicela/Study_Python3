"""
Ejercicio 6: Buscar producto en inventario 
Instrucciones:
Crea una función que reciba un inventario:

inventario: Dict[str, int]
Y un producto a buscar. Devuelve:

"Disponible" si tiene unidades

"Agotado" si tiene 0

None si el producto no está en el inventario
"""

from typing import Dict, Optional

def buscar_producto(inventario: Dict[str, int], producto: str) -> Optional[str]:
    if producto not in inventario:
        return None
    cantidad = inventario[producto]
    return "Disponible" if cantidad > 0 else "Agotado"


inv = {"pan": 10, "leche": 0, "queso": 5}
print(buscar_producto(inv, "pan")) 
print(buscar_producto(inv, "leche"))  
print(buscar_producto(inv, "huevos"))  
