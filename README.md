# Trabajo Práctico de Procesamiento del Lenguaje Natural

Repositorio del grupo para los trabajos prácticos de Procesamiento del Lenguaje Natural. Los notebooks y sus datos de entrada están organizados para ejecutarse después de clonar el repositorio.

## Estructura

```text
.
├── data/
│   ├── catalogo_tp3.jsonl
│   ├── ejemplo_preferencias.csv
│   ├── ejemplo_sospechosos.csv
│   ├── libros.csv
│   └── muestra_etiquetada.csv
├── docs/
│   ├── TP3/
│   │   ├── TP3_Recomendador_personalizado_de_libros.docx
│   │   └── TP3_Recomendador_personalizado_de_libros.pdf
│   ├── diseno_extraccion.md
│   └── superpowers/
│       ├── plans/
│       └── specs/
├── notebooks/
│   ├── TP1_ayala_cerana_colombo_ibarbia.ipynb
│   ├── TP2_ayala_cerana_colombo_ibarbia.ipynb
│   └── TP3_ayala_cerana_colombo_ibarbia.ipynb
├── src/
│   └── scraper.py
├── documentacion.md
├── informe.pdf
├── queries.json
├── README.md
└── requirements.txt
```

`data/modelos/` se crea durante el TP2 para los vectores descargados. Está excluida de Git por el tamaño de esos archivos.

## Requisitos e instalación

- Python 3.10 o superior.
- Git para clonar el repositorio.
- Conexión a Internet durante la primera ejecución del TP1 y TP2 para descargar los recursos de NLTK y los modelos que usan esos notebooks.

Desde la raíz del repositorio, crea y activa un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instala las dependencias compartidas por los tres trabajos:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`requirements.txt` es la lista completa y compartida: incluye JupyterLab, pandas, NumPy, NLTK, Gensim, scikit-learn, sentence-transformers, matplotlib, gdown, python-Levenshtein, langdetect, spaCy, Playwright y Beautiful Soup.

Dependencias principales por trabajo (todas se instalan con el mismo `requirements.txt`):

| Trabajo | Requerimientos principales |
| --- | --- |
| TP1 | pandas, NLTK, Gensim, sentence-transformers y scikit-learn |
| TP2 | pandas, NumPy, NLTK, Gensim, sentence-transformers, scikit-learn, matplotlib y gdown |
| TP3, Paso 1 y apartados 2.1 a 2.6 | pandas, python-Levenshtein, scikit-learn, langdetect, spaCy y sentence-transformers |
| `src/scraper.py` | Playwright y Beautiful Soup |

Para el apartado 2.4 del TP3, instala además el modelo de español de spaCy una vez:

```bash
python -m spacy download es_core_news_lg
```

El apartado 2.5 usa el modelo multilingüe `distiluse-base-multilingual-cased-v1`; sentence-transformers lo descarga al cargarlo por primera vez, por lo que esa ejecución requiere conexión a Internet.

## Ejecutar los trabajos prácticos

Ejecuta estos comandos desde la raíz del repositorio. JupyterLab abrirá el notebook; ejecuta sus celdas en orden.

### TP1 — Corpus y TF-IDF

```bash
python -m jupyter lab notebooks/TP1_ayala_cerana_colombo_ibarbia.ipynb
```

Usa `data/libros.csv` y `queries.json`. En la primera ejecución descarga `punkt`, `punkt_tab` y `stopwords` de NLTK, además del modelo SBERT `paraphrase-multilingual-MiniLM-L12-v2`.

### TP2 — Embeddings y búsqueda semántica

```bash
python -m jupyter lab notebooks/TP2_ayala_cerana_colombo_ibarbia.ipynb
```

Usa `data/libros.csv` y `queries.json`. En la primera ejecución descarga recursos de NLTK, el modelo SBW y el modelo SBERT. El archivo SBW se guarda en `data/modelos/` y no se versiona.

### TP3 — Recomendador personalizado de libros

```bash
python -m jupyter lab notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb
```

La versión incluida implementa el Paso 1 y los apartados 2.1 a 2.6 del Paso 2; lee `data/catalogo_tp3.jsonl` y `data/muestra_etiquetada.csv`. El apartado 2.3 usa `langdetect` para detectar mensajes en otro idioma dentro de las sinopsis. El apartado 2.4 usa spaCy con `es_core_news_lg` para comparar entidades de fragmentos contaminados con una cantidad similar de oraciones limpias. El apartado 2.5 compara clasificadores de oraciones con TF-IDF y embeddings. El apartado 2.6 revisa vecinos de sinopsis con TF-IDF, coseno y Jaccard para encontrar copias probables entre autores distintos. También están versionados `data/ejemplo_preferencias.csv` y `data/ejemplo_sospechosos.csv` para las consignas posteriores. El apartado 2.7 sigue pendiente. El enunciado está en `docs/TP3/`.

## Entregables existentes

- `notebooks/TP1_ayala_cerana_colombo_ibarbia.ipynb`
- `notebooks/TP2_ayala_cerana_colombo_ibarbia.ipynb`
- `notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb`
- `queries.json` e `informe.pdf`
