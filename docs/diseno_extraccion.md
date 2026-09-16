# Diseño de la Extracción - Unidad 1

## 1. Categoría seleccionada

*   **Nombre de la categoría:** Drama
*   **URL de la categoría:** `https://ww3.lectulandia.co/genero/drama/`
*   **Cantidad de libros que se propone extraer:** 150 libros.
*   **Criterio utilizado para seleccionar las páginas:** Se recorrerán las páginas de la categoría siguiendo el orden alfabético provisto por la plataforma.

## 2. Datos que se extraerán

El dataset final se guardará en `libros.csv` y contendrá los siguientes campos:

| Campo | Descripción |
| :--- | :--- |
| **titulo** | Título del libro |
| **autores** | Autor o autores |
| **generos** | Género o géneros |
| **serie** | Serie a la que pertenece, si corresponde |
| **sinopsis** | Texto completo de la sinopsis |
| **url_libro** | Dirección de la ficha |
| **categoria_origen** | Categoría seleccionada por el grupo (Drama) |
| **fecha_extraccion** | Fecha en que se obtuvo el registro |

## 3. Localización de los datos



| Dato | Tipo de página | Etiqueta HTML | Selector propuesto |
| :--- | :--- | :--- | :--- |
| **Título** | Ficha individual | `h1` | `#title` |
| **Autores** | Ficha individual | `a` | `#autor a` |
| **Géneros** | Ficha individual | `a` | `#genero a` |
| **Sinopsis** | Ficha individual | `p` | `#sinopsis p` |

Los selectores definitivos serán validados exhaustivamente durante la fase de desarrollo para evitar falsos positivos.

## 4. Estrategia de extracción

Como estrategia general, se recorrerá la URL de la categoría para extraer los enlaces de los primeros 150 libros. A partir de ello, utilizaremos Playwright para iterar por cada uno de estos enlaces e ir enriqueciendo nuestro diccionario "Libro", extrayendo los datos necesarios con BeautifulSoup.

El procedimiento detallado que se implementará es el siguiente:

1. **Abrir la página de la categoría con Playwright:** Iniciar el navegador y acceder a la URL principal de Drama.
2. **Recorrer las páginas necesarias:** Navegar por la paginación alfabética hasta alcanzar la cuota deseada.
3. **Obtener el HTML mediante Playwright:** Capturar el código fuente de las páginas índice.
4. **Analizar ese HTML con BeautifulSoup:** Parsear el contenido para aislar los contenedores de los libros.
5. **Extraer las URL de las fichas de los libros:** Guardar en una lista todos los enlaces (`href`) que dirigen a las páginas individuales de cada obra.
6. **Visitar cada ficha con Playwright:** Iterar sobre la lista de URLs y navegar a cada ficha individual (implementando esperas para no saturar el servidor).
7. **Extraer los metadatos y la sinopsis con BeautifulSoup:** En la página de cada libro, utilizar los selectores definidos en el punto 3 para capturar el título, autor, géneros, etc.
8. **Limpiar y validar los datos:** Remover espacios extra, caracteres especiales no deseados y manejar los valores nulos (por ejemplo, si un libro no tiene serie).
9. **Eliminar libros duplicados:** Filtrar la lista final utilizando la URL de la ficha como identificador único.
10. **Guardar el resultado en un archivo CSV:** Exportar los datos procesados mediante pandas al archivo `data/libros.csv`.