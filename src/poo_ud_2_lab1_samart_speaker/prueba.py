from altavoz import Altavoz


def main() -> None:
    altavoz = Altavoz("Salón", 30)

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.estado)

    altavoz.encender()
    print(altavoz.estado)

    altavoz.apagar()
    print(altavoz.estado)


if __name__ == "__main__":
    main()
