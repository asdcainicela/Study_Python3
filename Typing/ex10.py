"""
🧾 Ejercicio 12: Sistema de gestión de pacientes y consultas

🎯 Objetivo:
Desarrollar un sistema para gestionar pacientes, consultas médicas 
y guardar o recuperar los datos desde un archivo `.json`.

🧱 Estructura de datos:

1. Clase `Consulta`
   - fecha: str → fecha de la consulta (ej: "2025-07-28")
   - motivo: str → motivo de la consulta (ej: "Dolor de cabeza")
   - receta: Optional[str] → receta médica (si hay)

2. Clase `Paciente`
   - nombre: str
   - edad: int
   - consultas: List[Consulta] → lista de consultas que ha tenido el paciente

⚙️ Funciones a implementar:

A. agregar_consulta(paciente: Paciente, consulta: Consulta) -> None
   Agrega una consulta a la lista del paciente.

B. obtener_historial(paciente: Paciente) -> List[str]
   Devuelve el historial médico del paciente como una lista de cadenas con formato:
   - "28/07/2025: Dolor de cabeza (Receta: paracetamol)"
   - "10/06/2025: Control rutinario (Sin receta)"

C. pacientes_con_receta(pacientes: List[Paciente]) -> List[str]
   Devuelve una lista de nombres de pacientes que tienen 
   al menos una receta médica registrada.

D. guardar_pacientes(pacientes: List[Paciente], ruta: str) -> None
   Guarda la lista completa de pacientes y sus consultas en un archivo JSON.  
   Debe convertir objetos `Paciente` y `Consulta` a diccionarios usando `to_dict()`.

E. cargar_pacientes(ruta: str) -> List[Paciente]
   Lee un archivo JSON y reconstruye una lista de objetos `Paciente`, 
   con sus respectivas `Consulta`, utilizando `from_dict()`.

🧪 Simulación final:
1. Crear 3 pacientes con consultas variadas
2. Guardarlos en `pacientes.json` usando `guardar_pacientes`
3. Luego, cargarlos desde archivo con `cargar_pacientes`
4. Mostrar el historial de cada uno
5. Mostrar qué pacientes tienen recetas

💡 Extras técnicos:
- Uso de @dataclass para simplificar las clases
- Uso de Optional, List, staticmethod y typing
- Persistencia en disco con JSON
- Conversión entre clases y estructuras tipo dict
"""

from typing import List, Optional
from dataclasses import dataclass
import json

@dataclass
class Consulta:
    fecha: str
    motivo: str
    receta: Optional[str]

    def to_dict(self) -> dict:
        return {
            "fecha" : self.fecha,
            "motivo": self.motivo,
            "receta": self.receta
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Consulta":
        return Consulta(**data)

@dataclass
class Paciente:
    nombre: str
    edad: int
    consultas: List[Consulta]

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "consultas": [consulta.to_dict() for consulta in self.consultas]

        }
   
    @staticmethod
    def from_dict(data: dict) -> "Paciente":
        return Paciente(
            nombre=data["nombre"],
            edad=data["edad"],
            consultas=[Consulta.from_dict(c) for c in data["consultas"]]
        )
    
def agregar_consulta(paciente: Paciente, consulta: Consulta) -> None:
    paciente.consultas.append(consulta)


def guardar_pacientes(pacientes: List[Paciente], ruta: str) -> None:
    with open(ruta, "w") as f: 
        json.dump([paciente.to_dict() for paciente in pacientes], f, indent=2)

def cargar_pacientes(ruta: str) -> List[Paciente]:
    with open(ruta, "r") as f: 
        data = json.load(f)
        pacientes = [Paciente.from_dict(p) for p in data]
        return pacientes
          
def obtener_historial(paciente: Paciente) -> List[str]:
    return [
        f"{c.fecha}: {c.motivo} (Receta: {c.receta})" if c.receta else
        f"{c.fecha}: {c.motivo} (Sin receta)"
        for c in paciente.consultas
    ]


def pacientes_con_receta(pacientes: List[Paciente]) -> List[str]:
    list_paciente = []
    for paciente in pacientes:
        for consulta in paciente.consultas:
            if consulta.receta is not None:
                list_paciente.append(paciente.nombre)
                break
    return list_paciente   

def save_simulation() -> None:
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
    lista_de_pacientes = [juan, carlos, elva] 
    guardar_pacientes(lista_de_pacientes, "Typing/json/pacientes.json") 

    
 
def read_simulation():
    pacientes_lista=cargar_pacientes( "Typing/json/pacientes.json")
    for paciente in pacientes_lista :
        print("\n".join(obtener_historial(paciente)))
     
    print(" * "*10 + "Pacientes con recetas" + " * "*10 )
    print(pacientes_con_receta(pacientes_lista))  
 
if __name__ == "__main__":
    #save_simulation()
    read_simulation()