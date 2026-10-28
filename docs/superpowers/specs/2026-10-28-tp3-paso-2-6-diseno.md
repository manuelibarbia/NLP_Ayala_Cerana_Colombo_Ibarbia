# Diseño del TP3, Paso 2.6: vecinos de sinopsis

## Objetivo

Buscar en el catálogo libros cuyas sinopsis se parecen mucho aunque sus autores sean distintos, y revisar manualmente cuál parece reutilizar el texto de otro libro.

## Método

- Usar `catalogo_final` del Paso 1 y el campo `synopsis`.
- Crear una matriz TF-IDF con `TfidfVectorizer` y consultar `NearestNeighbors(metric="cosine")` para obtener el vecino más cercano de cada libro, excluyendo el propio registro.
- Conservar para revisión los pares con autores identificables y diferentes; tratar un autor genérico o ausente como no identificable.
- Deduplicar los pares no dirigidos y calcular la similitud de coseno como `1 - distancia`.
- Calcular Jaccard sobre conjuntos de palabras con la función `jaccard_palabras` ya usada en el Paso 1.
- Mostrar para revisión los pares con coseno de al menos 0,90, sus autores, métricas y comienzos de las dos sinopsis. El corte solo acota la revisión manual y no determina si un registro es copia.
- Registrar para cada candidato una dirección probable de copia o una decisión no concluyente, con evidencia textual completa. Distinguir las copias probables de pares que solo comparten vocabulario. No modificar ni eliminar filas del catálogo.

## Límites

- La similitud no determina la dirección de una copia ni demuestra plagio; la conclusión se basa en comparar títulos, autores y texto visible.
- El vecino más próximo puede no ser una copia. Libros legítimos pueden compartir temas o texto de una misma serie; los pares del mismo autor se excluyen de esta revisión.
- No se agregan dependencias ni un clasificador automático.

## Fuentes permitidas

- Consigna y guía de ayuda del TP3.
- Unidad 3 de Cátedra para TF-IDF, coseno y Jaccard.
