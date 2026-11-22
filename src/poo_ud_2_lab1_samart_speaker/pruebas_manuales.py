<<<<<<< HEAD
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
=======
from poo_ud_2_lab1_samart_speaker.altavoz import Altavoz


def probar_casos_validos() -> None:
    print("--- Probando Casos Válidos (V01 - V10) ---")

    altavoz = Altavoz("Salón", 30)
    print("V01 - Altavoz creado: Sí")
    print(f"V02 - Nombre: {altavoz.nombre}")
    print(f"V03 - Volumen: {altavoz.volumen}")
    print(f"V04 - Estado inicial: {altavoz.estado}")

    altavoz.volumen = 50
    print(f"V05 - Volumen cambiado a 50: {altavoz.volumen}")

    altavoz.volumen = 0
    print(f"V06 - Volumen cambiado a 0 (mínimo): {altavoz.volumen}")

    altavoz.volumen = 100
    print(f"V07 - Volumen cambiado a 100 (máximo): {altavoz.volumen}")

    altavoz.encender()
    print(f"V08 - Tras encender(): {altavoz.estado}")

    altavoz.apagar()
    print(f"V09 - Tras apagar(): {altavoz.estado}")

    altavoz_cocina = Altavoz(" Cocina ", 20)
    print(
        "V10 - Nombre con espacios limpios: "
        f"'{altavoz_cocina.nombre}'"
    )


def probar_casos_invalidos() -> None:
    print("--- Probando Casos Inválidos (I01 - I09) ---")

>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        Altavoz("", 30)
    except Exception as e:
        print(f"I01 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I02: Crear un altavoz con nombre " "
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        Altavoz(" ", 30)
    except Exception as e:
        print(f"I02 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I03: Crear un altavoz con nombre 25
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        Altavoz(25, 30)
    except Exception as e:
        print(f"I03 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I04: Crear un altavoz con volumen -1
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        Altavoz("Salón", -1)
    except Exception as e:
        print(f"I04 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I05: Crear un altavoz con volumen 101
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        Altavoz("Salón", 101)
    except Exception as e:
        print(f"I05 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I06: Asignar altavoz.volumen = 25.5
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        alt = Altavoz("Salón", 30)
        alt.volumen = 25.5
    except Exception as e:
        print(f"I06 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I07: Asignar altavoz.volumen = "alto"
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        alt = Altavoz("Salón", 30)
        alt.volumen = "alto"
    except Exception as e:
        print(f"I07 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
    # I08: Asignar altavoz.estado = "encendido"
=======
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
    try:
        alt = Altavoz("Salón", 30)
        alt.estado = "encendido"
    except Exception as e:
        print(f"I08 -> Excepción lanzada: {type(e).__name__} ({e})")

<<<<<<< HEAD
if __name__ == "__main__":
    probar_casos_invalidos()

   
=======
    try:
        alt = Altavoz("Salón", 30)
        alt.volumen = True
    except Exception as e:
        print(f"I09 -> Excepción lanzada: {type(e).__name__} ({e})")


if __name__ == "__main__":
    probar_casos_validos()
    print()
    probar_casos_invalidos()
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)
