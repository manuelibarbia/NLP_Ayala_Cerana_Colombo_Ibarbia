# Trabajo Práctico NLP - Extracción de texto

## Integrantes del grupo
* Ayala, Juan Manuel
* Cerana, Franco
* Colombo, Tomás
* Ibarbia, Manuel

## Categoría selected

- **Categoría:** Drama
- **URL:** https://ww3.lectulandia.co/genero/drama/

## Cantidad de libros extraídos

**150 libros** únicos (filtrados y sin duplicados).

## Modelo de datos

El dataset resultante se encuentra en `data/libros.csv` y contiene los siguientes campos:

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `titulo` | texto | Título del libro |
| `autores` | texto / lista | Autor o autores de la obra |
| `generos` | texto / lista | Género o géneros declarados en la ficha |
| `serie` | texto | Serie a la que pertenece (vacío si es autoconclusivo) |
| `sinopsis` | texto | Texto completo de la sinopsis |
| `url_libro` | texto | Dirección específica de la ficha del libro |
| `categoria_origen` | texto | Categoría seleccionada por el grupo (`Drama`) |
| `fecha_extraccion` | fecha | Fecha en que se obtuvo el registro (ISO 8601) |

## Instalación

Para ejecutar este proyecto, se requiere Python 3.10 o superior. 

1. Crear y activar un entorno virtual (recomendado):
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

2. Instalar las dependencias del proyecto:
```bash
pip install -r requirements.txt
```

3. Instalar el navegador para Playwright (Paso obligatorio para que el scraper funcione):
```bash
playwright install chromium
```

## Ejecución

Para iniciar la extracción, ejecutar desde la raíz del proyecto:

```bash
python src/scraper.py
```

### Comportamiento del Scraper
El script fue diseñado con una arquitectura robusta para evitar pérdidas de información y bloqueos:
- **Descubrimiento primero:** El script recorre primero la paginación de la categoría Drama para recolectar las 150 URLs.
- **Navegación controlada:** Utiliza Playwright (en modo *headless*) para visitar cada ficha individual, incorporando pausas aleatorias para no saturar el servidor de origen.
- **Tolerancia a fallos:** Se utilizan bloques `try/except` para los campos (como la "Serie") que pueden no estar presentes en todos los libros, evitando que el programa se detenga.

## Estructura del repositorio

```text
├── README.md                 # Documentación del proyecto
├── requirements.txt          # Dependencias de Python
├── src/
│   └── scraper.py            # Código fuente de la extracción
├── data/
│   └── libros.csv            # Dataset final
└── docs/
    └── diseno_extraccion.md  # Análisis previo y selectores
```

## Principales dificultades encontradas

- **Falsos positivos con libros relacionados:** La ficha de cada libro incluye recomendaciones en el panel lateral que utilizan las mismas clases HTML que el listado principal. Fue necesario ajustar los selectores de BeautifulSoup para apuntar estrictamente al contenedor de la obra principal.
- **URLs relativas:** Los enlaces extraídos de la grilla principal venían como rutas relativas (`/book/ejemplo/`). Se requirió concatenarlas con el dominio base antes de pasarle la orden de navegación a Playwright.
- **Inconsistencia en los metadatos:** Muchos libros autoconclusivos no renderizan la etiqueta de la "Serie". Se tuvo que implementar un manejo de excepciones para asignar un valor vacío en lugar de generar un error en la ejecución.
- **Manejo de saltos de línea en la sinopsis:** La extracción del texto de la sinopsis traía los elementos `<br>` pegados al texto. Se debió realizar una limpieza previa para reemplazarlos por espacios y mantener la legibilidad de los párrafos.