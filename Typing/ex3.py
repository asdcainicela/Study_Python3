"""
Crea una función que reciba un Dict[str, Tuple[int, float]], donde:
La clave es el nombre del empleado.
El valor es una tupla (edad, sueldo).
La función debe retornar una lista de nombres de los empleados que:
Tienen más de 30 años
Y ganan más de 2500
"""

from typing import Dict, Tuple, List

def empleados_filtro(info : Dict[str, Tuple[int, float]]) -> List[str]:
    list_filtrada: List[str] = []
    for name, value in info.items():
        if value[0]>30 and value[1]> 2500.0:
            list_filtrada.append(name)
    return list_filtrada
    #return [name for name, (edad, sueldo) in info.items() if edad > 30 and sueldo > 2500.0]


empleados = {
    "Ana": (28, 2800.0),
    "Luis": (35, 2400.0),
    "Pedro": (40, 3000.0),
    "Maria": (45, 2600.0)
}
filtro = empleados_filtro(empleados)
print(filtro)
# Resultado esperado: ["Pedro", "Maria"]
