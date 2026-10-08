# Trabajo Práctico de Procesamiento del Lenguaje Natural

## TP2 — Embeddings y búsqueda semántica

**Integrantes:** Juan Manuel Ayala, Franco Cerana, Tomás Colombo y Manuel Ibarbia

**Corpus:** 150 sinopsis de libros de la categoría Drama de Lectulandia.

El trabajo compara embeddings de palabras y de oraciones para recuperar libros a partir de consultas en lenguaje natural. También evalúa los modelos con relevancias definidas por el grupo y explora Doc2Vec.

## Implementación

- El notebook conserva `texto_crudo` y crea `texto_limpio` para los modelos de palabras.
- Entrena Word2Vec Skip-gram y lo compara con los vectores preentrenados `SBW-vectors-300-min5`.
- Construye vectores de documento como promedio normalizado y calcula su cobertura.
- Genera embeddings con `distiluse-base-multilingual-cased-v1` e informa dimensión, límite de tokens y truncamiento.
- Compara rankings para tres consultas, distribuciones de similitud entre pares aleatorios y proyecciones PCA por género.
- Calcula Precision@3 para TF-IDF, Word2Vec promedio, SBW, SBERT y Doc2Vec, junto con el valor esperado al elegir al azar.
- Entrena Doc2Vec y compara su recuperación con el promedio Word2Vec.

El corpus es pequeño y las sinopsis son promocionales. La limpieza puede eliminar negaciones, los vectores promedio pierden orden y contexto, y SBERT trunca documentos que superan su límite de tokens. Los resultados deben interpretarse como evidencia para este corpus y estas consultas.

## Entregables

- `notebooks/TP2_ayala_cerana_colombo_ibarbia.ipynb`: notebook ejecutado con salidas visibles.
- `queries.json`: diez consultas con identificadores de libros relevantes.
- `informe.pdf`: síntesis de hasta tres páginas con resultados, limitaciones, un caso de fallo y declaración de uso de asistentes de IA.

## Instalación y ejecución

Se requiere Python 3.10 o superior. Desde la raíz del repositorio:

```bash
python -m venv venv
```

Activar el entorno virtual e instalar las dependencias:

```bash
# Windows
venv\Scripts\activate

# Linux o macOS
source venv/bin/activate

pip install -r requirements.txt
```

Abrir el notebook:

```bash
python -m jupyter lab notebooks/TP2_ayala_cerana_colombo_ibarbia.ipynb
```

La primera ejecución descarga recursos de NLTK y el modelo SBW, que se guarda en `data/modelos/` y no se incluye en Git por su tamaño.
