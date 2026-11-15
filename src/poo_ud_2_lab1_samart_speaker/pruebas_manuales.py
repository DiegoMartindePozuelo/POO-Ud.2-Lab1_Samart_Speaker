from altavoz import Altavoz

def main() -> None:
    print("--- Probando Casos Válidos (V01 - V10) ---")

    # V01, V02, V03, V04: Crear altavoz y consultar estado inicial, nombre y volumen
    altavoz = Altavoz("Salón", 30)
    print(f"V02 - Nombre: {altavoz.nombre}")     # Debe devolver "Salón"
    print(f"V03 - Volumen: {altavoz.volumen}")   # Debe devolver 30
    print(f"V04 - Estado inicial: {altavoz.estado}") # En booleano es False (apagado)

    # V05: Cambiar volumen a 50
    altavoz.volumen = 50
    print(f"V05 - Volumen cambiado a 50: {altavoz.volumen}")

    # V06: Cambiar volumen a 0 (límite inferior)
    altavoz.volumen = 0
    print(f"V06 - Volumen cambiado a 0 (mínimo): {altavoz.volumen}")

    # V07: Cambiar volumen a 100 (límite superior)
    altavoz.volumen = 100
    print(f"V07 - Volumen cambiado a 100 (máximo): {altavoz.volumen}")

    # V08: Ejecutar encender()
    altavoz.encender()
    print(f"V08 - Tras encender(): {altavoz.estado}") # True (encendido)

    # V09: Ejecutar apagar()
    altavoz.apagar()
    print(f"V09 - Tras apagar(): {altavoz.estado}") # False (apagado)

    # V10: Crear un altavoz con espacios exteriores " Cocina " y verificar que se almacena limpio "Cocina"
    altavoz_cocina = Altavoz(" Cocina ", 20)
    print(f"V10 - Nombre con espacios limpios: '{altavoz_cocina.nombre}'")

if __name__ == "__main__":
    main()

from altavoz import Altavoz

def probar_casos_invalidos():
    print("--- Probando Casos Inválidos (I01 - I08) ---")

    # I01: Crear un altavoz con nombre ""
    try:
        Altavoz("", 30)
    except Exception as e:
        print(f"I01 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I02: Crear un altavoz con nombre " "
    try:
        Altavoz(" ", 30)
    except Exception as e:
        print(f"I02 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I03: Crear un altavoz con nombre 25
    try:
        Altavoz(25, 30)
    except Exception as e:
        print(f"I03 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I04: Crear un altavoz con volumen -1
    try:
        Altavoz("Salón", -1)
    except Exception as e:
        print(f"I04 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I05: Crear un altavoz con volumen 101
    try:
        Altavoz("Salón", 101)
    except Exception as e:
        print(f"I05 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I06: Asignar altavoz.volumen = 25.5
    try:
        alt = Altavoz("Salón", 30)
        alt.volumen = 25.5
    except Exception as e:
        print(f"I06 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I07: Asignar altavoz.volumen = "alto"
    try:
        alt = Altavoz("Salón", 30)
        alt.volumen = "alto"
    except Exception as e:
        print(f"I07 -> Excepción lanzada: {type(e).__name__} ({e})")

    # I08: Asignar altavoz.estado = "encendido"
    try:
        alt = Altavoz("Salón", 30)
        alt.estado = "encendido"
    except Exception as e:
        print(f"I08 -> Excepción lanzada: {type(e).__name__} ({e})")

if __name__ == "__main__":
    probar_casos_invalidos()

   