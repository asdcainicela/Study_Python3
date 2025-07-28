"""
 Sistema de gestión de pacientes y consultas
Aplicar clases conectadas entre sí (composición), List, Optional, @dataclass, y lógica relacional realista.

📋 Instrucciones:
Crea dos clases: Paciente y Consulta.

1. Clase Consulta
2. Clase Paciente

🛠️ Funciones a implementar:
A. agregar_consulta(paciente: Paciente, consulta: Consulta) -> None
Agrega una consulta al paciente.
B. obtener_historial(paciente: Paciente) -> List[str]
Devuelve una lista con strings del tipo:

"28/07/2025: Dolor de cabeza (Receta: paracetamol)"
"10/06/2025: Control rutinario (Sin receta)"
C. pacientes_con_receta(pacientes: List[Paciente]) -> List[str]
Retorna los nombres de los pacientes que tienen al menos una receta registrada.

"""

from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Consulta:
    fecha: str           # Ej: "2025-07-28"
    motivo: str          # Ej: "Dolor de cabeza"
    receta: Optional[str]

@dataclass
class Paciente:
    nombre: str
    edad: int
    consultas: List[Consulta]

def agregar_consulta(paciente: Paciente, consulta: Consulta) -> None:
    if paciente is None or consulta is None:
        return None
    
    paciente.consultas.append(consulta)

def obtener_historial(paciente: Paciente) -> List[str]:
    list_history = []
    for consulta in paciente.consultas:
        if consulta.receta is None:
            list_history.append(f"{consulta.fecha}: {consulta.motivo} (Sin receta)")
        else:
            list_history.append(f"{consulta.fecha}: {consulta.motivo} (Receta: {consulta.receta})")
    return list_history 
        
def pacientes_con_receta(pacientes: List[Paciente]) -> List[str]:
    list_paciente = []
    for paciente in pacientes:
        for consulta in paciente.consultas:
            if consulta.receta is not None:
                list_paciente.append(paciente.nombre)
                break
    return list_paciente        
                

def main() -> None:
    juan = Paciente("Juan", 34, [])
    c1 = Consulta("2025-07-28", "Dolor de cabeza", "paracetamol")
    c2 = Consulta("2025-07-29", "Dolor muscular", None)

    carlos = Paciente("Carlos", 18, [])
    c3 = Consulta("2025-07-29", "Dolor Estomago", None)

    elva = Paciente("Elva", 56, [])
    c4 = Consulta("2025-07-29", "Gripe", "dormir")
    c5 = Consulta("2025-07-29", "Migrana", "forte")

    agregar_consulta(juan, c1)
    agregar_consulta(juan, c2)
    agregar_consulta(carlos, c3)
    agregar_consulta(elva, c4)
    agregar_consulta(elva, c5)

    print("\n".join(obtener_historial(juan)))
    print("\n".join(obtener_historial(carlos))) 
    print("\n".join(obtener_historial(elva)))
    pacientes = [juan, carlos, elva]
    print(pacientes_con_receta(pacientes))   

if __name__ == "__main__":
    main()