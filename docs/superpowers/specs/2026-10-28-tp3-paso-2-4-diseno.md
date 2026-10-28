# TP3 Paso 2.4: reconocer entidades

## Intención

Comparar las entidades nombradas encontradas en las oraciones de fragmentos contaminados con las de una cantidad similar de oraciones limpias y responder si aportan detección o contexto explicativo.

## Alcance

- Usar spaCy y `es_core_news_lg`, nombrados por la consigna y mostrados en Unidad 3.
- Trabajar únicamente con la partición de desarrollo para no consultar la prueba.
- Separar el campo `fragmento` de los libros contaminados y obtener oraciones limpias de sinopsis con `contaminado=0`.
- Seguir la separación de la guía, conservar segmentos de al menos 15 caracteres y muestrear reproduciblemente la misma cantidad de oraciones limpias que las oraciones contaminadas disponibles.
- Mostrar las entidades reconocidas y sus etiquetas, comparar cadenas sin distinguir mayúsculas y responder con cautela si una entidad del fragmento no aparece en la muestra limpia.
- Usar el análisis como descripción cualitativa; no convertir la presencia de una entidad en una nueva regla automática para marcar libros.
- Actualizar `requirements.txt`, `README.md` y `documentacion.md`, anotando la descarga independiente del modelo `es_core_news_lg`.
- Verificar manualmente la ejecución completa del notebook; no agregar pruebas formales ni aserciones.

## Decisiones y límites

- Se elige spaCy porque `es_core_news_lg` aparece como alternativa directa en el enunciado y la Unidad 3 enseña cómo cargarlo y consultar `doc.ents`.
- La guía da como ejemplo filtrar segmentos de al menos 15 caracteres. Se reutiliza el separador ya usado en el Paso 2.3.
- Se usa el conjunto de desarrollo, con muestra limpia de tamaño igual al conjunto de oraciones de fragmentos contaminados. `random_state=42` permite repetir qué oraciones limpias se comparan.
- Unidad 3 advierte que el modelo español puede producir falsas detecciones y omitir entidades. La comparación no prueba que una entidad sea exclusiva del contenido contaminado.

## Fuera de alcance

- GLiNER, etiquetas personalizadas, entrenamiento o ajuste del modelo.
- Evaluar el NER como clasificador con las etiquetas de prueba.
- Cambiar los umbrales o resultados de los apartados 2.1 a 2.3.
- Exportar entidades o sospechosos fuera del notebook.
