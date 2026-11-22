class Altavoz:
    def __init__(self, nombre: str, volumen: int):
        # Usamos las propiedades (setters) desde el constructor 
        # para validar el nombre y el volumen también al crear el objeto.
        self.nombre = nombre
        self.volumen = volumen
        self._estado = False  # Comienza apagado (interno)

    # --- REQUISITO 1: PROPIEDAD NOMBRE ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío ni formado solo por espacios.")
        # Limpiamos los espacios exteriores antes de guardarlo
        self._nombre = nuevo_nombre.strip()

    # --- REQUISITO 2: PROPIEDAD VOLUMEN ---
    @property
    def volumen(self) -> int:
        return self._volumen

    @volumen.setter
    def volumen(self, nuevo_volumen: int):
        if not isinstance(nuevo_volumen, int) or isinstance(nuevo_volumen, bool):
            raise TypeError("El volumen debe ser un número entero.")
        if not (0 <= nuevo_volumen <= 100):
            raise ValueError("El volumen debe estar comprendido entre 0 y 100.")
        self._volumen = nuevo_volumen

    # --- REQUISITO 3: CONTROL DE ESTADO ---
    @property
    def estado(self) -> bool:
        # Solo permite consultar el estado, pero NO modificarlo directamente 
        # (al no tener un @estado.setter, si intentan hacer altavoz.estado = True dará error).
        return self._estado

    def encender(self) -> None:
        self._estado = True

    def apagar(self) -> None:
        self._estado = False

