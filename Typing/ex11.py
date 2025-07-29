"""
🧾 Ejercicio 13 (Versión Avanzada): Sistema académico con análisis estadístico de rendimiento

🎯 Objetivo:
Implementar un sistema completo para registrar estudiantes, cursos y evaluaciones,
y analizar matemáticamente su rendimiento académico individual y colectivo.

🧱 Estructuras:

1. Clase Evaluación
   - fecha: str (formato: "YYYY-MM-DD")
   - tipo: Literal["Examen", "Proyecto", "Tarea", "Quiz", "Otro"]
   - nota: float ∈ [0, 20]
   - observaciones: Optional[str]

2. Clase Curso
   - nombre: str
   - creditos: int ∈ ℕ+
   - evaluaciones: List[Evaluacion]

3. Clase Estudiante
   - nombre: str
   - edad: int ∈ ℕ+
   - cursos: Dict[str, Curso]  # clave: nombre del curso

🎯 Funciones requeridas:

 A. agregar_evaluacion(estudiante: Estudiante, curso_nombre: str, evaluacion: Evaluacion) -> None  
   - Agrega una evaluación a un curso dado del estudiante.
   - Crea el curso si no existe.

 B. promedio_ponderado(estudiante: Estudiante) -> float  
   - Calcula el promedio de todas las evaluaciones ponderadas por créditos de cada curso.
   - Fórmula:
     \[
     \bar{x} = \frac{\sum_i c_i \cdot \bar{n}_i}{\sum_i c_i}
     \]
     donde \( \bar{n}_i \) es el promedio de notas del curso \( i \), y \( c_i \) sus créditos.

 C. obtener_reporte(estudiante: Estudiante) -> str  
   - Devuelve un string ordenado con el historial completo:
     - Curso: "Matemáticas (5 créditos) — Promedio: 17.25"
     - Evaluaciones:
       - "2025-08-01 | Examen: 18.0 (Excelente)"
       - "2025-08-08 | Proyecto: 16.5 (Sin observaciones)"

 D. estudiantes_destacados(estudiantes: List[Estudiante]) -> List[str]  
   - Devuelve estudiantes con promedio_ponderado ≥ 16.0

 E. resumen_por_curso(estudiantes: List[Estudiante]) -> Dict[str, Tuple[int, float, float]]  
   - Retorna un resumen por curso:
     - clave: nombre del curso
     - valor: (número de estudiantes, promedio global del curso, desviación estándar de notas)

✅ F. guardar_estudiantes(estudiantes: List[Estudiante], ruta: str)  
✅ G. cargar_estudiantes(ruta: str)

🎯 Opcional:  
✅ H. análisis_matricula(estudiantes: List[Estudiante]) -> Dict[str, int]  
   - Devuelve cuántos estudiantes están matriculados en cada curso.

✅ I. top_n_estudiantes(estudiantes: List[Estudiante], n: int) -> List[str]  
   - Devuelve los `n` estudiantes con mayor promedio ponderado.

🧠 Requisitos matemáticos:
- Promedio simple
- Promedio ponderado
- Desviación estándar:
  \[
  \sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^N (x_i - \bar{x})^2 }
  \]

💡 Bonus:
- Validación de tipos usando `Literal` de `typing`
- Propiedad `.promedio` en Curso y Estudiante
- Decoradores como `@staticmethod`, `@property`

📂 Simulación sugerida:
1. Crear 4 estudiantes
2. Asignarles cursos y evaluaciones variadas
3. Guardar en JSON
4. Leer y mostrar:
   - Reporte individual
   - Estudiantes destacados
   - Ranking top 3
   - Estadísticas por curso

✍️ Herramientas clave:
- @dataclass
- typing: List, Dict, Optional, Tuple, Literal
- Funciones matemáticas: promedio, varianza
- json (serialización)
- Lógica condicional, comprensión de listas
"""
from typing import List, Dict, Optional, Literal, Tuple
from dataclasses import dataclass
from collections import defaultdict
import math
import json
import os

@dataclass
class Evaluacion:
    fecha: str
    tipo: Literal["Examen", "Proyecto", "Tarea", "Quiz", "Otro"]
    nota: float 
    observaciones: Optional[str]

    @property
    def val_nota(self) -> bool:
        return 0 <= self.nota <= 20
    
    def to_dict(self) -> dict:
        return {
            "fecha": self.fecha,
            "tipo": self.tipo,
            "nota": self.nota,
            "observaciones": self.observaciones
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Evaluacion":
        return cls(
            fecha=data["fecha"],
            tipo=data["tipo"],
            nota=data["nota"],
            observaciones=data["observaciones"]
        )

@dataclass
class Curso:
    nombre: str
    creditos: int 
    evaluaciones: List[Evaluacion]
    promedio: Optional[float] = None

    @property
    def validacion_credito(self) -> bool:
        return self.creditos > 0 and isinstance(self.creditos, int)

    def actualizar_promedio(self) -> None:
        if self.evaluaciones:
            self.promedio = round(sum(e.nota for e in self.evaluaciones) / len(self.evaluaciones), 2)
        else:
            self.promedio = None

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "creditos": self.creditos,
            "evaluaciones": [e.to_dict() for e in self.evaluaciones],
            "promedio": self.promedio
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Curso":
        return cls(
            nombre=data["nombre"],
            creditos=data["creditos"],
            evaluaciones=[Evaluacion.from_dict(e) for e in data["evaluaciones"]],
            promedio=data.get("promedio")
        )

@dataclass
class Estudiante:
    nombre: str
    edad: int
    cursos: Dict[str, Curso]
    ponderado: Optional[float] = None

    @property
    def validacion_edad(self) -> bool:
        return self.edad > 0 and isinstance(self.edad, int)
    
    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "cursos": {name: curso.to_dict() for name, curso in self.cursos.items()},
            "ponderado": self.ponderado
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Estudiante":
        cursos = {}
        for nombre_curso, curso_data in data["cursos"].items():
            cursos[nombre_curso] = Curso.from_dict(curso_data)
        
        return cls(
            nombre=data["nombre"],
            edad=data["edad"],
            cursos=cursos,
            ponderado=data.get("ponderado")
        )

def agregar_evaluacion(estudiante: Estudiante, curso_nombre: str, evaluacion: Evaluacion) -> None:
    if not evaluacion.val_nota:
        print("Error: Nota inválida (debe estar entre 0 y 20)")
        return

    if curso_nombre not in estudiante.cursos:
        try:
            creditos = int(input(f"El curso {curso_nombre} no existe. Ingrese créditos para nuevo curso: "))
            if creditos <= 0:
                raise ValueError("Los créditos deben ser positivos")
            estudiante.cursos[curso_nombre] = Curso(nombre=curso_nombre, creditos=creditos, evaluaciones=[])
            print(f"Curso {curso_nombre} creado con {creditos} créditos")
        except ValueError as e:
            print(f"Error: {e}")
            return
    
    estudiante.cursos[curso_nombre].evaluaciones.append(evaluacion)
    estudiante.cursos[curso_nombre].actualizar_promedio()
    print(f"Evaluación agregada al curso {curso_nombre}")

def promedio_ponderado(estudiante: Estudiante) -> Optional[float]:
    valores = []
    
    for curso in estudiante.cursos.values():
        if curso.promedio is None:
            continue
            
        valores.append((curso.promedio, curso.creditos))
    
    if not valores:
        print("El estudiante no tiene cursos con evaluaciones")
        return None
    
    suma_ponderada = sum(p * c for p, c in valores)
    total_creditos = sum(c for _, c in valores)
    
    estudiante.ponderado = round(suma_ponderada / total_creditos, 2)
    return estudiante.ponderado

def obtener_reporte(estudiante: Estudiante) -> str:
    reporte = []
    reporte.append(f"\nReporte para: {estudiante.nombre} (Edad: {estudiante.edad})")
    reporte.append("="*50)
    
    for nombre_curso, curso in estudiante.cursos.items():
        reporte.append(f"\nCurso: {nombre_curso} ({curso.creditos} créditos) - Promedio: {curso.promedio or 'N/A'}")
        reporte.append("-"*50)
        
        if curso.evaluaciones:
            reporte.append("Evaluaciones:")
            for evaluacion in curso.evaluaciones:
                obs = evaluacion.observaciones or "Sin observaciones"
                reporte.append(f"  ▸ {evaluacion.fecha} | {evaluacion.tipo}: {evaluacion.nota}/20 - {obs}")
        else:
            reporte.append("No hay evaluaciones registradas")
    
    promedio_general = promedio_ponderado(estudiante)
    reporte.append("\n" + "="*50)
    reporte.append(f"PROMEDIO PONDERADO GENERAL: {promedio_general or 'N/A'}")
    
    return "\n".join(reporte)

def estudiantes_destacados(estudiantes: List[Estudiante]) -> List[Tuple[str, float]]:
    destacados = []
    print("\nEstudiantes con promedio ponderado >= 16.0")
    print("="*50)
    
    for i, estudiante in enumerate(sorted(estudiantes, key=lambda e: e.ponderado or 0, reverse=True), 1):
        if estudiante.ponderado and estudiante.ponderado >= 16:
            destacados.append((estudiante.nombre, estudiante.ponderado))
            print(f"{i}. {estudiante.nombre} - {estudiante.ponderado}")
    
    return destacados

def resumen_por_curso(estudiantes: List[Estudiante]) -> Dict[str, Tuple[int, float, float]]:
    resumen = defaultdict(lambda: {'estudiantes': 0, 'suma_notas': 0.0, 'notas': []})
    
    # Recolectar datos
    for estudiante in estudiantes:
        for curso in estudiante.cursos.values():
            if curso.promedio is not None:
                resumen[curso.nombre]['estudiantes'] += 1
                resumen[curso.nombre]['suma_notas'] += curso.promedio
                resumen[curso.nombre]['notas'].append(curso.promedio)
    
    # Calcular estadísticas
    resultado = {}
    for nombre, datos in resumen.items():
        cantidad = datos['estudiantes']
        promedio = round(datos['suma_notas'] / cantidad, 2) if cantidad else 0.0
        
        # Cálculo de desviación estándar corregido
        if cantidad > 1:
            varianza = sum((x - promedio) ** 2 for x in datos['notas']) / cantidad
            desviacion = round(math.sqrt(varianza), 2)
        else:
            desviacion = 0.0  # No se puede calcular con menos de 2 datos
        
        resultado[nombre] = (cantidad, promedio, desviacion)
    
    # Presentación de resultados
    print("\nRESUMEN ESTADÍSTICO POR CURSO")
    print("=" * 50)
    for curso, (cant, prom, desv) in sorted(resultado.items(), key=lambda x: x[1][0], reverse=True):
        print(f"\n{curso.upper():<15} [Estudiantes: {cant}]")
        print(f"  • Promedio: {prom}")
        print(f"  • Desviación estándar: {desv if cant > 1 else 'N/D (insuficientes datos)'}")
        print("-" * 50)
    
    return resultado
 

    print(f"\nEstudiante: {estudiante.nombre} (Edad: {estudiante.edad})")
    for nombre_curso, curso in estudiante.cursos.items():
        print(f"  Curso: {nombre_curso} ({curso.creditos} créditos)")
        for eval in curso.evaluaciones:
            print(f"    - {eval.fecha}: {eval.tipo} - Nota: {eval.nota}")

def guardar_estudiantes(estudiantes: List[Estudiante], ruta: str) -> None: 
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump([estudiante.to_dict() for estudiante in estudiantes], 
                 f, 
                 indent=2, 
                 ensure_ascii=False)

def cargar_estudiantes(ruta: str) -> List[Estudiante]: 
    with open(ruta, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return [Estudiante.from_dict(estudiante_data) for estudiante_data in data]
          
def analisis_matricula(estudiantes: List[Estudiante]) -> Dict[str, int]: 
    matricula = defaultdict(int)
    for estudiante in estudiantes:
        for nombre_curso in estudiante.cursos:
            matricula[nombre_curso] += 1
    
    return dict(sorted(matricula.items(), key=lambda x: x[1], reverse=True))

def top_n_estudiantes(estudiantes: List[Estudiante], n: int) -> List[Tuple[str, float]]: 
    # Filtrar estudiantes con promedio calculado
    estudiantes_con_promedio = [
        (est.nombre, est.ponderado) 
        for est in estudiantes 
        if est.ponderado is not None
    ]
    
    # Ordenar descendentemente por promedio
    estudiantes_ordenados = sorted(
        estudiantes_con_promedio, 
        key=lambda x: x[1], 
        reverse=True
    )
    
    # Retornar los primeros n
    return estudiantes_ordenados[:n]

def main() -> None:
    # Creación de estudiantes
    estudiantes = [
        Estudiante("Juan Pérez", 19, {}),
        Estudiante("María García", 20, {}),
        Estudiante("Carlos López", 18, {}),
        Estudiante("Ana Martínez", 21, {}),
        Estudiante("Luis Rodríguez", 22, {}),
        Estudiante("Patas González", 16, {}), 
        Estudiante("José Fernández", 17, {}),
        Estudiante("Sofía Díaz", 19, {}),
        Estudiante("Miguel Sánchez", 20, {}),
        Estudiante("Elena Ramírez", 18, {})
    ]

    # Creación de cursos
    cursos = {
        "Matemáticas": Curso("Matemáticas", 5, []),
        "Física": Curso("Física", 4, []),
        "Química": Curso("Química", 3, []),
        "Biología": Curso("Biología", 4, []),
        "Programación": Curso("Programación", 6, []),
        "Historia": Curso("Historia", 2, []),
        "Literatura": Curso("Literatura", 3, []),
        "Inglés": Curso("Inglés", 3, []),
        "Economía": Curso("Economía", 4, []),
        "Arte": Curso("Arte", 2, [])
    }

    # Asignación aleatoria de cursos (3-5 por estudiante)
    import random
    for estudiante in estudiantes:
        cursos_estudiante = random.sample(list(cursos.items()), k=random.randint(3, 5))
        for nombre_curso, curso in cursos_estudiante:
            estudiante.cursos[nombre_curso] = curso

    # Creación de evaluaciones (2-4 por curso)
    tipos_eval = ["Examen", "Proyecto", "Tarea", "Quiz"]
    observaciones = ["Excelente", "Buen trabajo", "Puede mejorar", None]
    
    for estudiante in estudiantes:
        for curso in estudiante.cursos.values():
            for _ in range(random.randint(2, 4)):
                evaluacion = Evaluacion(
                    fecha=f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                    tipo=random.choice(tipos_eval),
                    nota=round(random.uniform(10, 20), 1),
                    observaciones=random.choice(observaciones)
                )
                agregar_evaluacion(estudiante, curso.nombre, evaluacion)

    # Cálculo de promedios
    for estudiante in estudiantes:
        promedio_ponderado(estudiante)

    # 1. Reportes individuales
    print("\n" + "="*60)
    print("REPORTES INDIVIDUALES (3 primeros estudiantes)")
    print("="*60)
    for i in range(3):
        print(obtener_reporte(estudiantes[i]))
        print("\n" + "-"*60 + "\n")

    # 2. Análisis de matrícula
    print("\n" + "="*60)
    print("ANÁLISIS DE MATRÍCULA")
    print("="*60)
    matricula = analisis_matricula(estudiantes)
    for curso, cantidad in matricula.items():
        print(f"{curso:<15}: {cantidad:>2} estudiantes")

    # 3. Top estudiantes
    print("\n" + "="*60)
    print("TOP 5 ESTUDIANTES")
    print("="*60)
    top_5 = top_n_estudiantes(estudiantes, 5)
    for pos, (nombre, promedio) in enumerate(top_5, 1):
        print(f"{pos:>2}. {nombre:<20}: {promedio:.2f}")

    # 4. Resumen por curso
    print("\n" + "="*60)
    print("ESTADÍSTICAS POR CURSO")
    print("="*60)
    resumen = resumen_por_curso(estudiantes)
    
    # 5. Guardar datos
    guardar_estudiantes(estudiantes, "data/estudiantes.json")
    print("\n✅ Datos guardados en 'data/estudiantes.json'")

if __name__ == "__main__":
    main()