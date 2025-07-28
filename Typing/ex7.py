"""
Registro de cursos con clases y List[Tuple]

📋 Instrucciones:
Define una clase Curso con:
nombre: str
creditos: int
nota: float
Luego, crea una función que reciba una lista de cursos y devuelva:
La nota ponderada
El curso con mayor nota
"""

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Curso:
    nombre : str
    creditos: int
    nota: float

def resumen_cursos(cursos: List[Curso]) -> Tuple[float, Curso]:
    if not cursos:
        return (0.0, Curso("", 0, 0.0))  # retorno seguro por defecto
    
    mejor = max(cursos, key=lambda e: e.nota)
    sum_creditos = sum(e.creditos for e in cursos)
    ponderado = round(sum((e.nota * e.creditos) for e in cursos) / sum_creditos, 2)

    return (ponderado, mejor)

    
cursos = [
    Curso("Matemática", 4, 18.0),
    Curso("Historia", 3, 12.0),
    Curso("Física", 5, 16.5)
]

ponderado, mejor_curso = resumen_cursos(cursos)
print("Nota ponderada:", ponderado)
print("Mejor curso:", mejor_curso.nombre, "con", mejor_curso.nota)
