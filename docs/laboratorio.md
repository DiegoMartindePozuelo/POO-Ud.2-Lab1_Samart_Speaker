# Laboratorio: Smart Speaker - Diseño Orientado a Objetos en Python

## 1.2. Identificamos los problemas planteados
Respuesta a las preguntas planteadas:
* **1.	¿Qué ocurre cuando el nombre está vacío?** No pasa nada. No hay incoherencia, es admitido, simplemente no hay una identificación del altavoz.
* **2.	¿Qué ocurre cuando el volumen es negativo?** Según el programa es ejecutable, aunque en la realidad un volumen negativo no tiene sentido. Debe ser un número entero (`int`) comprendido estrictamente entre 0 y 100 (ambos incluidos).
* **3.	¿Podemos asignar un texto al atributo encendido?** Si, se ha hecho con “quizás”. Python permite guardar un dato incorrecto (un texto) en un lugar donde solo debería haber un "sí" o "no" (un booleano). El altavoz comienza siempre apagado. Su valor se puede consultar externamente, pero **no** se permite su modificación mediante una asignación ordinaria. Las únicas vías autorizadas para alterar el estado son los métodos explícitos `encender()` y `apagar()`.
* **4.	¿Quién debería ser responsable de evitar estos valores: el código que utiliza la clase o la propia clase?** La propia clase (Altavoz) es responsable de su propio estado.
* **5.	¿Qué problemas podría provocar que cualquier parte del programa modificase directamente el estado del altavoz?** Trazabilidad para localizar errores de código.

## 1.3. Reglas de negocio identificadas
Durante la fase de análisis inicial, se establecieron los siguientes requisitos de negocio para el dispositivo:
* **Validación del Nombre:** Debe ser obligatoriamente una cadena de texto (`str`), no puede estar vacía ni compuesta exclusivamente por espacios en blanco. Los espacios exteriores deben eliminarse automáticamente antes de su almacenamiento (`.strip()`).
* **Validación del Volumen:** Debe ser un número entero (`int`) comprendido estrictamente entre 0 y 100 (ambos incluidos). Esta validación aplica tanto en el momento de la instanciación (creación) como en cualquier modificación posterior mediante asignación.
* **Control de Estado:** El altavoz comienza siempre apagado. Su valor se puede consultar externamente, pero **no** se permite su modificación mediante una asignación ordinaria. Las únicas vías autorizadas para alterar el estado son los métodos explícitos `encender()` y `apagar()`.
* **Interfaz Limpia:** Los usuarios interactúan exclusivamente con las propiedades públicas (`nombre`, `volumen`, `estado`) y los métodos de control, sin manipular directamente los atributos internos protegidos.

---

## 2.1. Tabla de diseño de la interfaz pública

| **Elemento** | **¿Público o interno?** | **¿Cómo debería utilizarse?** |
| :--- | :--- | :--- |
| `nombre del altavoz` | **Interno** (por convención: _nombre) | Consultar y modificar con validación: Consultar y modificar mediante una propiedad (@property) o métodos que validen que no esté vacío. |
| `volumen` | **Interno** (por convención: _volumen) | Consultar y modificar con validación: Consultar y modificar mediante una propiedad o métodos que validen que esté entre 0 y 100. |
| `estado de encendido` | **Interno** (por convención: _estado) | Consultar, pero no modificar directamente: Consultarse externamente (para saber si está encendido), pero **no modificarse de forma directa** (se altera únicamente a través de los métodos de control). |
| `Operación encender` | **Público** (encender()) | Cambiar el estado: Método accesible desde fuera para cambiar el estado del altavoz a encendido de forma controlada. |
| `Operación apagar` | **Público** (apagar()) | Cambiar el estado: Método accesible desde fuera para cambiar el estado del altavoz a apagado de forma controlada. |

---

## 3.	Explicación de las propiedades utilizadas
Para proteger los datos internos y mantener una interfaz limpia, se ha aplicado el principio de **encapsulación** mediante la convención de atributos protegidos (`_nombre`, `_volumen`, `_estado`) combinados con decoradores de Python:
* **Uso de `@property` (Getters):** Permiten exponer los atributos internos de forma controlada y transparente para que el usuario acceda a ellos como si fueran variables normales (`altavoz.nombre`), pero ejecutando lógica intermedia de lectura si fuera necesario.
* **Uso de Setters (`@nombre.setter`, `@volumen.setter`):** Interceptan cualquier intento de reasignación externa (ej. `altavoz.volumen = 50`) para someter el nuevo valor a filtros de validación de tipo y rango antes de guardarlo. Si el valor no es válido, se bloquea la operación lanzando una excepción.
* **Ausencia de setter en el estado:** Al no declarar una propiedad `@estado.setter`, Python bloquea por diseño cualquier intento de escritura externa (`altavoz.estado = True`), protegiendo la integridad del flujo de negocio y obligando al uso de los métodos de control.

---

## 4. Resultados de las pruebas

### 4.1. Pruebas Válidas
| ID | Operación probada | Resultado obtenido | ¿Coincide con el esperado? |
| :--- | :--- | :--- | :--- |
| **V01** | Crear un altavoz con nombre "Salón" y volumen 30 | Objeto creado con éxito | **Sí** |
| **V02** | Consultar el nombre (`altavoz.nombre`) | `"Salón"` | **Sí** |
| **V03** | Consultar el volumen (`altavoz.volumen`) | `30` | **Sí** |
| **V04** | Consultar el estado inicial (`altavoz.estado`) | `False` (Apagado) | **Sí** |
| **V05** | Cambiar el volumen a 50 | `50` | **Sí** |
| **V06** | Cambiar el volumen a 0 (mínimo) | `0` | **Sí** |
| **V07** | Cambiar el volumen a 100 (máximo) | `100` | **Sí** |
| **V08** | Ejecutar `encender()` | Estado pasa a `True` ("encendido")| **Sí** |
| **V09** | Ejecutar `apagar()` | Estado pasa a `False` ("apagado")| **Sí** |
| **V10** | Crear altavoz con nombre `" Cocina "` | Almacena `'Cocina'` sin espacios exteriores | **Sí** |

### 4.2. Pruebas Inválidas
| ID | Operación probada | Excepción obtenida | ¿Coincide con el esperado? |
| :--- | :--- | :--- | :--- |
| **I01** | Crear altavoz con nombre `""` (vacío) | `ValueError` | **Sí** |
| **I02** | Crear altavoz con nombre `" "` (espacios) | `ValueError` | **Sí** |
| **I03** | Crear altavoz con nombre `25` (entero) | `TypeError` | **Sí** (Funcional)* |
| **I04** | Crear altavoz con volumen `-1` | `ValueError` | **Sí** |
| **I05** | Crear altavoz con volumen `101` | `ValueError` | **Sí** |
| **I06** | Asignar volumen `25.5` (decimal) | `TypeError` | **Sí** (Funcional)* |
| **I07** | Asignar volumen `"alto"` (texto) | `TypeError` | **Sí** (Funcional)* |
| **I08** | Asignar `altavoz.estado = "encendido"` | `AttributeError` | **Sí** |
| **I09** | Asignar volumen `True` (booleano) | `TypeError` | **Sí** |

*\*Nota técnica:* Las pruebas I03, I06 e I07 devuelven `TypeError` debido al uso de validaciones de tipos estrictas en Python, lo cual constituye una buena práctica de desarrollo para distinguir errores de tipado frente a errores de rango numérico (`ValueError`).

---

## 5. Recomendaciones de la IA y decisiones tomadas

* **Recomendación 1: Validación estricta de tipos booleanos frente a enteros**
  * **¿La acepto?:** Sí.
  * **Justificación:** En Python, los booleanos (`bool`) son técnicamente una subclase de los enteros (`int`), por lo que un valor como `True` pasaría el filtro numérico equivalente a `1`. Implementar una comprobación explícita que rechace tipos booleanos aporta robustez profesional al código.
  * **Verificación:** Probado mediante análisis estricto de tipos en el setter de volumen.

* **Recomendación 2: Unificación de excepciones a `ValueError`**
  * **¿La acepto?:** No (se prioriza el criterio técnico).
  * **Justificación:** Aunque la especificación inicial agrupaba los errores bajo `ValueError`, mantener la distinción entre `TypeError` (para errores de tipo) y `ValueError` (para errores de rango o lógica) ofrece una realimentación de depuración mucho más precisa y limpia para el desarrollador.

---

## 6. Reflexión final: ¿Qué ventajas tiene que la clase controle sus propias reglas?
Permitir que la clase `Altavoz` encapsule y gestione de manera autónoma sus propias reglas de negocio aporta ventajas:
1. **Integridad del Estado:** Se elimina por completo la posibilidad de que el objeto quede corrompido o adopte valores absurdos (como un volumen negativo o un nombre vacío), ya que cualquier intento externo de manipulación incorrecta es interceptado y bloqueado de inmediato en la fuente.
2. **Mantenibilidad y Centralización:** Si en el futuro las reglas cambian (por ejemplo, permitir un volumen máximo de 120), el cambio se realiza en un único lugar (el setter de la clase) sin necesidad de modificar el código repartido por el resto de la aplicación.
3. **Desacoplamiento y Seguridad:** El código externo ("cliente") no necesita conocer los detalles internos de cómo se almacenan los datos (`_nombre`, `_volumen`). Esto protege los datos internos de modificaciones accidentales y garantiza un contrato de uso limpio, seguro y predecible a través de la interfaz pública.