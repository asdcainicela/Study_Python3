from typing import List

def sumar(a: int, b: int) -> int:
    return a + b

def saludar_personas(nombres: List[str]) -> List[str]:
    return [f"Hola {nombre}" for nombre in nombres]

def main() -> None:
    suma = sumar(4, 7)
    print("Suma:", suma)

    saludos = saludar_personas(["Ana", "Luis", "Pedro"])
    for saludo in saludos:
        print(saludo)

if __name__ == "__main__":
    main()
