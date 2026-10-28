# TP3 Paso 2.5: clasificar oraciones

## Intención

Aprender a reconocer texto promocional a partir de oraciones de fragmentos contaminados y oraciones de sinopsis limpias; comparar TF-IDF con embeddings a un objetivo común de precisión.

## Alcance

- Seguir la consigna: usar frases del campo `fragmento` de libros contaminados como positivas y oraciones de sinopsis limpias como negativas.
- Usar la separación de oraciones indicada en la ayuda del TP y conservar segmentos de al menos 15 caracteres.
- Separar los libros de desarrollo por `slug` en ajuste y calibración (70/30, `random_state=42`, estratificado). No dividir oraciones de un mismo libro entre ambos conjuntos.
- Entrenar regresión logística con `class_weight="balanced"` y `max_iter=1000` para TF-IDF y un SentenceTransformer multilingüe.
- Elegir umbral con `precision_recall_curve` sobre la probabilidad máxima por libro en la parte de calibración. Intentar precisión 0,90; si un modelo no llega, usar el objetivo común más alto alcanzable por ambos.
- Marcar un libro si al menos una oración de su sinopsis alcanza el umbral.
- Medir en la partición de prueba exterior, sin cambiar los umbrales.
- Mostrar positivos de prueba por detector y falsos positivos, incluyendo las oraciones de mayor puntuación para inspeccionar tipos de contaminación.
- Actualizar README y `documentacion.md`. La dependencia `sentence-transformers` ya existe en `requirements.txt`; el modelo se descarga en la primera carga.
- Ejecutar manualmente el notebook completo; no agregar pruebas formales ni aserciones.

## Representaciones

- TF-IDF con `TfidfVectorizer`, según la Unidad 3.
- Sentence embeddings con `distiluse-base-multilingual-cased-v1`, presentado en Unidad 2 y reutilizado en el TP2 para oraciones en español.
- Aplicar ambas representaciones a las mismas oraciones y usar la misma división por libros.

## Interpretación

- Comparar precisión y recall a nivel libro, ya que la consigna marca una sinopsis sospechosa cuando alguna de sus oraciones supera el umbral.
- Inspeccionar el campo `fragmento` en positivos de prueba para describir tipos de contaminación. El CSV no tiene etiquetas por tipo; las categorías se describen cualitativamente y no se presentan como métricas específicas.
- Explicar que embeddings pueden generalizar a frases nuevas con significado parecido y que TF-IDF conserva ventaja potencial para cadenas literales, sin asumir que el resultado empírico necesariamente favorece a uno.

## Fuera de alcance

- Modificar las regex, la normalización, detección de idioma o NER de los pasos 2.1 a 2.4.
- Usar etiquetas de prueba para elegir umbrales o parámetros.
- Clasificar sinopsis completas en vez de las frases prescritas.
- Exportar sospechosos: eso corresponde al apartado 2.7.
