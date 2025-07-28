"""
Resumen de estudiantes con @dataclass
Crea una clase Estudiante con:
    nombre: str
    nota: float
Luego, crea una función que reciba una lista de estudiantes y devuelva:
El nombre del mejor alumno
La nota promedio
"""
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

@dataclass
class Estudiante:
    nombre : str
    nota: float

def resumen_estudiantes(estudiantes: List[Estudiante]) -> Tuple[str, float]:
    sum_notas = 0
    j=0
    name = ""
    mean_notas = 0
    notas_max=0
    for estudiante in estudiantes:
        j+=1
        sum_notas += estudiante.nota
        if notas_max < estudiante.nota:
            notas_max = estudiante.nota
            name = estudiante.nombre
             
    try:
        mean_notas = round(sum_notas/j,2)
    except :
        print("Error")
    return (name, mean_notas)

alumnos = [
    Estudiante("Ana", 18.0),
    Estudiante("Luis", 12.5),
    Estudiante("Pedro", 15.0),
]

print(resumen_estudiantes(alumnos)) 
