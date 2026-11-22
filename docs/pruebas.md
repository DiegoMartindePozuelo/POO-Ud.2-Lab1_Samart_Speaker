# Pruebas automatizadas de Smart Speaker

## Relación de requisitos comprobados

| Requisito | Prueba principal | Resultado |
|---|---|---|
| El nombre se almacena correctamente | `test_altavoz_se_crea_con_nombre_y_volumen_validos` | Cubierto |
| El volumen inicial se almacena | `test_altavoz_se_crea_con_nombre_y_volumen_validos` | Cubierto |
| El estado inicial está apagado | `test_altavoz_se_crea_con_nombre_y_volumen_validos` | Cubierto |
| Los espacios exteriores del nombre se eliminan | `test_nombre_se_guarda_sin_espacios_al_principio_ni_al_final` | Cubierto |
| Los espacios interiores se conservan | `test_nombre_permite_espacios_internos` | Cubierto |
| El nombre se puede modificar por su propiedad | `test_nombre_se_puede_modificar_mediante_su_setter` | Cubierto |
| El nombre vacío o compuesto por espacios se rechaza | Pruebas parametrizadas con `""`, `" "` y `"   "` | Cubierto |
| Los nombres que no son texto se rechazan | Pruebas parametrizadas con `123` y `None` | Cubierto |
| El volumen acepta 0 y 100 | Prueba parametrizada de límites | Cubierto |
| El volumen rechaza valores fuera del rango | Pruebas parametrizadas con `-1` y `101` | Cubierto |
| Los tipos incorrectos de volumen se rechazan | Pruebas con decimal, texto, `None` y booleanos | Cubierto |
| El estado no se puede asignar directamente | `test_estado_se_puede_consultar_pero_no_asignar_directamente` | Cubierto |
| `encender()` cambia el estado a encendido | `test_encender_cambia_el_estado_a_encendido` | Cubierto |
| `apagar()` cambia el estado a apagado | `test_apagar_cambia_el_estado_a_apagado` | Cubierto |
| Puede apagarse un altavoz después de encenderlo | `test_se_puede_apagar_el_altavoz_despues_de_encenderlo` | Cubierto |

## Casos principales

La batería prueba tanto casos positivos como negativos.

Los casos positivos comprueban la creación con datos válidos, el almacenamiento de nombre y volumen, los límites `0` y `100`, la limpieza de espacios exteriores y el funcionamiento de `encender()` y `apagar()`.

Los casos negativos comprueban:

- nombres vacíos o formados solo por espacios: `ValueError`;
- nombres con otro tipo: `TypeError`;
- volúmenes fuera de `[0, 100]`: `ValueError`;
- decimales, texto, `None` y booleanos como volumen: `TypeError`;
- asignación directa del estado: `AttributeError`.

Esta separación conserva el criterio técnico usado en el laboratorio anterior: los errores de tipo son `TypeError`, mientras que los valores válidos con contenido fuera del rango o vacíos son `ValueError`.

## Ejecución correcta

Comando utilizado:

```powershell
uv run pytest -q
```

Resultado obtenido:

```text
............................                                             [100%]
28 passed in 0.02s
```

Pytest está disponible mediante:

```text
pytest 9.2.0
```

## Prueba de robustez con fallo deliberado

Se modificó temporalmente `encender()` para conservar el estado en `False`:

```python
def encender(self) -> None:
    self._estado = False
```

Después se ejecutó:

```powershell
uv run pytest tests/test_altavoz.py::test_encender_cambia_el_estado_a_encendido -q
```

Resultado observado:

```text
FAILED tests/test_altavoz.py::test_encender_cambia_el_estado_a_encendido
assert False is True
1 failed in 0.03s
```

La prueba falló porque esperaba `True` después de llamar a `encender()`, pero recibió `False`. Esto demuestra que la batería detecta cambios incorrectos del estado.

Tras el experimento se restauró `self._estado = True`. Una nueva ejecución completa volvió a obtener `28 passed`.

## Revisión de las sugerencias de la IA

Se ha incorporado la sugerencia de rechazar explícitamente los valores booleanos como volumen. Python considera `bool` una subclase de `int`, por lo que sin esta comprobación `True` podría interpretarse como `1`.

También se han incorporado casos adicionales para:

- modificar el nombre mediante su setter;
- conservar espacios internos;
- rechazar `None` como nombre;
- comprobar asignaciones inválidas posteriores a la creación;
- comprobar nombres internos y externos al objeto.

No se ha incorporado la unificación automática de todas las excepciones a `ValueError`. Se mantiene `TypeError` para datos con tipo incorrecto y `ValueError` para datos de tipo válido fuera del rango o vacíos. Esta decisión ya se justificó en la primera fase del laboratorio y permite distinguir el tipo del error de su rango o contenido.
