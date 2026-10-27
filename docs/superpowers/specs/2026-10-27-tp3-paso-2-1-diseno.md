# Diseño del TP3 — Paso 2.1: expresiones regulares

## Intención

Agregar al notebook la primera auditoría automática de contaminación con patrones para URLs, correos y teléfonos. La persona que estudie el TP podrá comparar las señales y ver sus falsos positivos antes de usar detectores posteriores.

## Alcance

- Implementar solo el apartado 2.1 y la partición común de la muestra que utilizarán los subpasos posteriores.
- Leer `data/muestra_etiquetada.csv` y conservar la división fija de libros: 70 % desarrollo y 30 % prueba, `random_state=42` y `stratify=muestra["contaminado"]`.
- Usar la columna `synopsis` y medir precisión y recall de cada patrón y de su combinación OR sobre `prueba`.
- Mostrar los falsos positivos combinados de prueba. Si no hay ninguno, mostrar aparte un ejemplo limpio detectado en desarrollo y aclarar que no entra en las métricas.
- Explicar que la muestra tiene 20 % de contaminación y que su precisión no representa directamente la prevalencia del catálogo completo.
- Actualizar `documentacion.md` y el alcance de TP3 en `README.md`.
- Ejecutar el notebook para verificar el resultado; no agregar celdas de tests ni aserciones.

## Fuera de alcance

- Normalización previa de texto (2.2), detección de idioma, NER, clasificadores, vecinos por similitud, combinación final de detectores o exportación de `sospechosos.csv`; pertenecen a apartados posteriores.
- Ajustar patrones mirando la partición de prueba.
- Agregar dependencias: `re` pertenece a la biblioteca estándar y pandas/scikit-learn ya están declarados.

## Enfoques considerados

1. Una sola regex con alternativas para las tres señales: es compacta, pero no permite observar cuál patrón explica el resultado.
2. Un patrón por tipo y un detector combinado: fue elegido por el usuario porque facilita comparar URLs, correos y teléfonos y responde qué señales detecta mejor.

## Diseño propuesto

- Agregar los apartados `Paso 2 Auditar el catálogo` y `2.1 Expresiones regulares` al notebook del grupo.
- Definir tres patrones independientes: URL `re.compile(r"https?://|www\.", re.IGNORECASE)` de la guía del TP; correo `re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", re.IGNORECASE)` de la Unidad 1; teléfono `re.compile(r"\+\d(?:[\s().-]?\d){7,14}")`, que requiere prefijo `+` y acepta entre 8 y 15 dígitos con separadores habituales para cubrir formatos como `+54 9 11 5217-8319` del conjunto de desarrollo.
- Marcar un libro por patrón si su sinopsis contiene una coincidencia; el detector combinado marca el libro si cualquiera de los tres lo marca.
- Presentar una tabla con precisión, recall y cantidad de libros marcados por patrón y combinación, calculadas con las etiquetas de `prueba` usando `precision_score` y `recall_score`; mostrar los falsos positivos de prueba con `slug`, título y señales. Si la tabla está vacía, acompañar un ejemplo limpio de desarrollo con URL legítima, etiquetado como exploratorio y excluido de las métricas, y explicar el costo de borrar un libro legítimo.
- Mantener `desarrollo` y `prueba` disponibles para los apartados siguientes. La regex mínima no detectará las variantes disimuladas que se tratarán en 2.2.
- Registrar la metodología y límites en `documentacion.md`; cambiar README para indicar que TP3 contiene Paso 1 y Paso 2.1. Guardar este incremento con el commit `feat: Paso 2.1`.

## Límites

La regex telefónica propuesta requiere el prefijo `+`; puede omitir teléfonos nacionales sin prefijo. Las menciones reales de sitios, correos o números en sinopsis legítimas pueden generar falsos positivos. Ambos casos se medirán y se explicarán, sin ajustar los patrones con la partición de prueba.
