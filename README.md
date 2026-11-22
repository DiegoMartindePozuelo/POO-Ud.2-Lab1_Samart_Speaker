# Laboratorio: Smart Speaker

Ejercicio de encapsulación y validación mediante una clase `Altavoz` en Python.

## Funcionalidad

- Nombre obligatorio como texto, sin espacios exteriores.
- Volumen entero comprendido entre 0 y 100.
- Estado consultable, pero modificable únicamente con `encender()` y `apagar()`.

## Ejecución

```powershell
uv run python -m poo_ud_2_lab1_samart_speaker.main
uv run pytest -q
```