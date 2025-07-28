"""
Ejercicio 10: Historial de pacientes (Dict + Optional + Nested structures)
Instrucciones:
Tienes un historial de pacientes como:

historial: Dict[str, Dict[str, Optional[str]]]

Debe retornar una lista con los nombres de los pacientes que tienen alergias registradas.
"""

from typing import Dict, Optional, List

def listar_pacientes_con_alergias(historial: Dict[str, Dict[str, Optional[str]]]) -> List[str]:
    return [name for name, _ in historial.items() if  historial[name]["alergias"] is not None]

historial = {
"Ana": {"sangre": "A+", "alergias": None},
"Luis": {"sangre": "O-", "alergias": "penicilina"},
"Pedro": {"sangre": "B+", "alergias": "polvo"}
}

lista = listar_pacientes_con_alergias(historial)
print(lista)