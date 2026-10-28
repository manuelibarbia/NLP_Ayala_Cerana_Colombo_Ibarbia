# TP3 Paso 2.3: detectar el idioma de cada oración

## Intención

Detectar mensajes en otros idiomas que quedan mezclados dentro de una sinopsis en español y medir el detector sin usar la partición de prueba para elegir sus parámetros.

## Alcance

- Usar `langdetect` y su función `detect_langs`, como permiten la consigna y la Unidad 3.
- Detectar primero el idioma principal de sinopsis completas en desarrollo y mostrar su relación con la etiqueta `contaminado`.
- Dividir las sinopsis con `re.split(r"(?<=[.!?])\s+|\n", texto)` y detectar el idioma principal de cada oración con `detect_langs`.
- Contar palabras como secuencias de letras Unicode, sin contar años ni otros números como palabras.
- Elegir una cantidad mínima de palabras y una probabilidad mínima mediante comparaciones en las 350 filas de desarrollo; usar `DetectorFactory.seed = 42` para repetir los resultados.
- Aplicar los valores elegidos a prueba una sola vez y mostrar precisión, recall, falsos positivos y ejemplos de oraciones detectadas.
- Aclarar que `contaminado` no identifica el idioma: las métricas evalúan coincidencia con la etiqueta de contaminación, no exactitud lingüística.
- Mantener intactos los textos originales, la partición 70/30, las regex y la normalización de los apartados previos.
- Actualizar `requirements.txt`, `README.md` y `documentacion.md`; documentar las métricas de desarrollo y prueba observadas.

## Enfoques

- `langdetect` con `detect_langs`: elegido porque aparece en la Unidad 3 y la consigna pide justificar un umbral de probabilidad. Usa una dependencia pequeña y permite ver las probabilidades por idioma.
- `fasttext-langdetect`: también está mencionado por la consigna, pero agrega un modelo distinto y no responde al pedido específico de justificar `detect_langs`.
- Detectar únicamente sinopsis completas: no detecta mensajes de otro idioma dentro de un texto largo español, por lo que se conserva solo como comparación y se agrega detección por oración.

## Valores elegidos con desarrollo

En la partición de desarrollo (350 libros), se compararon mínimos de 5, 7, 10, 12 y 15 palabras con probabilidades mínimas de 0,90 y 0,99. Con 7 palabras y 0,90, el detector marcó 12 de los 70 libros contaminados y 3 de los 280 limpios (precisión 0,80; recall 0,17). Con 10 palabras y 0,90 marcó 9 contaminados y 2 limpios (precisión 0,82; recall 0,13). Subir la probabilidad a 0,99 no cambió estos resultados. Con 15 palabras no se marcaron contaminados y hubo un falso positivo. Se elige 10 y 0,90 para reducir falsos positivos frente al mínimo anterior de 7, aceptando un recall menor; un mínimo de 15 elimina la detección útil.

La detección de sinopsis completas clasificó como español las 350 sinopsis de desarrollo, incluidas las 70 contaminadas. Esto muestra el límite de clasificar el texto largo cuando el mensaje insertado aparece dentro de una sinopsis española. Algunas oraciones españolas reciben una probabilidad cercana a 1,0 para otro idioma; la confianza no elimina esos falsos positivos y la etiqueta de contaminación tampoco confirma el idioma.

## Fuera de alcance

- Implementar NER, clasificación de texto promocional, similitud de libros o combinación final de detectores.
- Cambiar los detectores previos, quitar oraciones del catálogo o marcar un libro a partir de un solo nombre propio.
- Ajustar parámetros mirando las etiquetas o resultados de prueba.

## Verificación

Ejecutar el notebook completo y revisar manualmente las tablas de desarrollo y prueba, las oraciones marcadas y sus falsos positivos. No agregar pruebas formales ni aserciones, según la instrucción del usuario.
