# TP3 Paso 2.7 — Diseño

## Objetivo

Combinar las señales binarias construidas en los apartados 2.1 a 2.6, medir cada detector y la unión sobre la partición de prueba ya reservada, y aplicar la combinación al catálogo final del Paso 1.

## Enfoque

- Reutilizar los patrones, umbrales y clasificadores ya definidos; no ajustar nada con las etiquetas de prueba.
- Mostrar precisión, recall, cantidad marcada y falsos positivos para cada patrón de URL, correo y teléfono, sus combinaciones original y normalizada, la detección de idioma completa y por oración, los dos clasificadores y las copias probables revisadas en 2.6.
- Combinar con OR las señales binarias de esos detectores. NER no produce una decisión binaria por libro y en 2.4 se usa para describir fragmentos; no se inventa una regla para incluirlo.
- Para 2.6, marcar solo el `slug` que la revisión manual señaló como copia probable. Los dos pares no concluyentes no se marcan por esa señal.
- Ejecutar el mismo sistema sobre `catalogo_final`, que ya contiene el resultado del Paso 1, y guardar `data/sospechosos.csv` con `slug` y `motivo`, y `data/catalogo_limpio.csv` con las fichas restantes.

## Límites

La combinación OR puede aumentar el recall a costa de falsos positivos. Las métricas se calculan sobre 150 filas de prueba y no garantizan el resultado del catálogo completo. Las copias de 2.6 provienen de una revisión manual acotada a los candidatos de alta similitud; no son una regla general aprendida para encontrar cualquier copia nueva.

## Verificación

Ejecutar el notebook completo en orden, inspeccionar la tabla de métricas y las salidas CSV, confirmar sus columnas y cantidades, revisar que no haya errores de ejecución y comprobar `git diff --check`. No se agregan pruebas formales.
