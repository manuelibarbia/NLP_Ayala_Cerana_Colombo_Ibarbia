# Trabajo Práctico NLP - Extracción de texto

## Integrantes del grupo
* Ayala, Juan Manuel
* Cerana, Franco
* Colombo, Tomás
* Ibarbia, Manuel

## Categoría seleccionada

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
