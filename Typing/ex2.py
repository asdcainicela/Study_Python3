"""
Crea una función que reciba una lista de nombres y devuelva una lista de saludos.
Cada saludo debe ser: "Hola, <nombre>"
"""

from typing import List

def saludar_nombres(nombres : List[str]) -> List[str]:
    return [f" Hola, {nombre}" for nombre in nombres]

saludos = saludar_nombres(["Ana", "Luis", "Carlos"])

for saludo in saludos:
    print(saludo)

"""
Crea una función que reciba un nombre de usuario y devuelva el tipo de usuario si existe.
Si el usuario no existe, devuelve None.
"""

from typing import Optional

def buscar_usuario(nombre: str) -> Optional[str]:
    
    match nombre.lower():
        case "admin":
            return "Administrador"
        case "user":
            return "Usuario"
        case _:
            return None

bu1 = buscar_usuario("admin")  
bu2 = buscar_usuario("user")    
bu3 = buscar_usuario("otro")   
print(bu1)
print(bu2)
print(bu3)

"""
Crea una función que reciba un diccionario con nombres y notas de estudiantes,
 y retorne solo los que aprobaron (nota ≥ 13.0).
"""

from typing import Dict

def filtrar_aprobados(notas: Dict[str, float]) -> Dict[str, float]:
    return {name: nota for name, nota in notas.items() if nota >=13 }
        
notas = {"Ana": 14.5, "Luis": 12.0, "Pedro": 16.0}
print(filtrar_aprobados(notas)) 

"""
Crea una función que reciba dos coordenadas (x1, y1) y (x2, y2) y 
retorne la distancia Euclidiana entre ellas.
"""
from typing import Tuple

def distancia(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return ((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)**0.5
print(distancia((0,0), (3,4)))