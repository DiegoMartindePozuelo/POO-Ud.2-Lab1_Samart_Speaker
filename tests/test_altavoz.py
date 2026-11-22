import pytest

from poo_ud_2_lab1_samart_speaker.altavoz import Altavoz


# PRUEBAS DE CREACION

def test_altavoz_se_crea_con_nombre_y_volumen_validos():
    altavoz = Altavoz("Salón", 30)

    assert altavoz.nombre == "Salón"
    assert altavoz.volumen == 30
    assert altavoz.estado is False


# PRUEBAS DE PROPIEDADES

def test_nombre_se_guarda_sin_espacios_al_principio_ni_al_final():
    altavoz = Altavoz("  Cocina  ", 30)

    assert altavoz.nombre == "Cocina"


def test_nombre_permite_espacios_internos():
    altavoz = Altavoz("Salón Principal", 30)

    assert altavoz.nombre == "Salón Principal"


def test_nombre_se_puede_modificar_mediante_su_setter():
    altavoz = Altavoz("Salón", 30)

    altavoz.nombre = "  Dormitorio  "

    assert altavoz.nombre == "Dormitorio"


@pytest.mark.parametrize("nombre", ["", " ", "   "])
def test_nombre_vacio_o_con_espacios_lanza_value_error(nombre):
    with pytest.raises(ValueError):
        Altavoz(nombre, 30)


@pytest.mark.parametrize("nombre", [123, None])
def test_nombre_que_no_es_cadena_lanza_type_error(nombre):
    with pytest.raises(TypeError):
        Altavoz(nombre, 30)


def test_nombre_asignado_incorrectamente_lanza_value_error():
    altavoz = Altavoz("Salón", 30)

    with pytest.raises(ValueError):
        altavoz.nombre = " "


@pytest.mark.parametrize("volumen", [0, 100])
def test_volumen_acepta_los_limites_incluidos(volumen):
    altavoz = Altavoz("Sala", volumen)

    assert altavoz.volumen == volumen


@pytest.mark.parametrize("volumen", [-1, 101])
def test_volumen_fuera_del_rango_lanza_value_error(volumen):
    with pytest.raises(ValueError):
        Altavoz("Sala", volumen)


@pytest.mark.parametrize("volumen", [25.5, "alto", None])
def test_volumen_que_no_es_entero_lanza_type_error(volumen):
    with pytest.raises(TypeError):
        Altavoz("Sala", volumen)


@pytest.mark.parametrize("volumen", [True, False])
def test_volumen_booleano_lanza_type_error(volumen):
    with pytest.raises(TypeError):
        Altavoz("Sala", volumen)


@pytest.mark.parametrize(
    ("volumen", "error"),
    [
        (-1, ValueError),
        (101, ValueError),
        (25.5, TypeError),
        ("50", TypeError),
        (True, TypeError),
    ],
)
def test_asignacion_invalida_de_volumen_lanza_excepcion(volumen, error):
    altavoz = Altavoz("Sala", 30)

    with pytest.raises(error):
        altavoz.volumen = volumen


def test_estado_se_puede_consultar_pero_no_asignar_directamente():
    altavoz = Altavoz("Sala", 50)

    assert altavoz.estado is False

    with pytest.raises(AttributeError):
        altavoz.estado = True

# PRUEBAS DE COMPORTAMIENTO

def test_encender_cambia_el_estado_a_encendido():
    altavoz = Altavoz("Sala", 50)

    altavoz.encender()
    assert altavoz.estado is True


def test_apagar_cambia_el_estado_a_apagado():
    altavoz = Altavoz("Sala", 50)

    altavoz.apagar()
    assert altavoz.estado is False


def test_se_puede_apagar_el_altavoz_despues_de_encenderlo():
    altavoz = Altavoz("Sala", 50)

    altavoz.encender()
    altavoz.apagar()

    assert altavoz.estado is False
