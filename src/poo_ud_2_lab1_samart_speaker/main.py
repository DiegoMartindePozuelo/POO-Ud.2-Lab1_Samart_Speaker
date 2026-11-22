<<<<<<< HEAD
from altavoz import Altavoz
=======
from poo_ud_2_lab1_samart_speaker.altavoz import Altavoz
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)


def main() -> None:
    altavoz = Altavoz("Salón", 30)

    print(altavoz.nombre)
    print(altavoz.volumen)
<<<<<<< HEAD
    print(altavoz.encendido)

    altavoz.nombre = ""
    altavoz.volumen = -50
    altavoz.encendido = "quizá"

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.encendido)
=======
    print(altavoz.estado)

    altavoz.encender()
    print(altavoz.estado)

    altavoz.apagar()
    print(altavoz.estado)
>>>>>>> 6dbad62 (Implementar y documentar Smart Speaker)


if __name__ == "__main__":
    main()


