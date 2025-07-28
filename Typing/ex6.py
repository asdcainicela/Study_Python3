"""
Sistema de compras (Dict + Tuple + Optional)- Objetivo: Simular un carrito de compras simple.
 Instrucciones:
Tienes un inventario:
inventario: Dict[str, Tuple[float, int]]
# clave: nombre del producto
# valor: (precio unitario, cantidad disponible)
Crea una función que permita comprar un producto:
    Debe devolver el total pagado si la compra es posible, o None si:
    el producto no existe
    no hay suficiente cantidad 
    Al final, actualiza el inventario si se realiza la compra.
"""

from typing import Dict, Tuple, Optional

def comprar_producto(
    inventario: Dict[str, Tuple[float, int]],
    producto: str,
    cantidad: int
) -> Optional[float]:
    
    if producto not in inventario:
        return None

    precio, cantidad_disp = inventario[producto]
    
    if cantidad > cantidad_disp:
        return None

    inventario[producto] = (precio, cantidad_disp - cantidad)
    return round(precio * cantidad, 2)  # redondeo opcional


inv ={
    "leche": (3.5, 15),
    "azucar": (2.8, 50),
    "arroz": (3.8, 2)
}
print(inv)
total = comprar_producto(inv, "leche", 10)
print(total)
print(inv)