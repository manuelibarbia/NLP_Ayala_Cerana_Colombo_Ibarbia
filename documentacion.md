# Documentación del proyecto <!-- Última modificación: 2026-10-27 -->
<!-- Última modificación: 2026-10-27 -->
## Alcance de esta entrega <!-- Última modificación: 2026-10-27 -->
- Se documenta el Paso 1 del TP3: cargar, limpiar y revisar el catálogo de libros. <!-- Última modificación: 2026-10-27 -->
- El proyecto es un trabajo de análisis en notebooks; esta entrega no agrega backend, API ni pantallas de interfaz. <!-- Última modificación: 2026-10-27 -->
## Feature: carga y revisión del catálogo <!-- Última modificación: 2026-10-27 -->
- Nombre: Paso 1, cargar y revisar libros. <!-- Última modificación: 2026-10-27 -->
- Ruta y acceso: abrir `notebooks/TP3_ayala_cerana_colombo_ibarbia.ipynb` en Jupyter y ejecutar sus celdas en orden. <!-- Última modificación: 2026-10-27 -->
- Propósito: preparar el catálogo para las consignas posteriores, conservando los datos originales salvo los registros eliminados por las reglas exactas indicadas aquí. <!-- Última modificación: 2026-10-27 -->
- Información mostrada: conteos de limpieza, grupos de sinopsis repetidas, registros disponibles y pares candidatos con títulos, autores compartidos y métricas de similitud. <!-- Última modificación: 2026-10-27 -->
- Acciones e interacciones: ejecutar la instalación de dependencias, cargar el archivo, inspeccionar los resultados y revisar manualmente cada candidato numerado. <!-- Última modificación: 2026-10-27 -->
- Navegación relacionada: el Paso 1 está al inicio del notebook; el Paso 2 todavía no forma parte de esta implementación. <!-- Última modificación: 2026-10-27 -->
- Permisos: no hay autenticación ni permisos de aplicación; la persona que ejecuta Jupyter debe poder leer el archivo de entrada local. <!-- Última modificación: 2026-10-27 -->
- Carga: la celda busca `data/catalogo_tp3.jsonl` desde la raíz o `../data/catalogo_tp3.jsonl` desde `notebooks/`; también acepta las rutas hermanas originales y un archivo cargado en Colab. <!-- Última modificación: 2026-10-27 -->
- Vacío: si no hay pares que superen los filtros, la tabla de candidatos queda vacía; los ejemplos de separación requieren que sus libros estén presentes en el catálogo. <!-- Última modificación: 2026-10-27 -->
- Error: si no se encuentra el archivo o falta una dependencia, la celda muestra el error de ejecución de Python/Jupyter y el notebook no continúa hasta corregirlo. <!-- Última modificación: 2026-10-27 -->
- Conexión con backend: no existe backend ni API; las celdas leen y transforman datos localmente con pandas. <!-- Última modificación: 2026-10-27 -->
## Datos y reglas implementadas <!-- Última modificación: 2026-10-27 -->
- Entrada: `data/catalogo_tp3.jsonl`, versionado en el repositorio; el notebook selecciona `slug`, `title`, `authors` y `synopsis`. <!-- Última modificación: 2026-10-27 -->
- Datos de apoyo: `data/muestra_etiquetada.csv`, `data/ejemplo_preferencias.csv` y `data/ejemplo_sospechosos.csv` quedan disponibles para las consignas posteriores del TP3. <!-- Última modificación: 2026-10-27 -->
- Documentación fuente: el enunciado DOCX y PDF se conserva en `docs/TP3/`; no hace falta para ejecutar los notebooks. <!-- Última modificación: 2026-10-27 -->
- Se normalizan espacios consecutivos de la sinopsis, sin quitar puntuación ni caracteres. <!-- Última modificación: 2026-10-27 -->
- Se descartan sinopsis vacías, slugs repetidos y sinopsis idénticas ya normalizadas, conservando el primer registro de cada caso repetido. <!-- Última modificación: 2026-10-27 -->
- En la corrida verificada se encontraron 1 sinopsis vacía, 0 slugs repetidos y 98 registros adicionales con sinopsis idéntica; quedaron 8.648 registros. <!-- Última modificación: 2026-10-27 -->
- Para revisión aproximada se comparan libros que comparten al menos un autor identificable; se excluyen las etiquetas genéricas `Varios Autores` y `Anónimo`. <!-- Última modificación: 2026-10-27 -->
- Levenshtein normalizado del título debe ser al menos 0,80 y Jaccard de palabras de la sinopsis al menos 0,75 para mostrar un par candidato. <!-- Última modificación: 2026-10-27 -->
- Los 66 pares resultantes son sugerencias para revisión manual; se aprobaron únicamente las fusiones de los candidatos 1, 8, 11 y 31. <!-- Última modificación: 2026-10-27 -->
- En cada fusión se conserva la primera ficha del catálogo y se elimina la segunda; la tabla del notebook muestra títulos, autores, puntajes y motivos. <!-- Última modificación: 2026-10-27 -->
- El candidato 7 se mantiene separado porque su título especifica Granada; comparte autor y palabras en la sinopsis (Jaccard = 1,00), aunque difieren algunas mayúsculas que la limpieza exacta conserva. <!-- Última modificación: 2026-10-27 -->
- El notebook presenta además dos pares separados por representar volúmenes o contenidos distintos y muestra cinco filas de ejemplo del catálogo final. <!-- Última modificación: 2026-10-27 -->
- En la corrida final se quitaron 1 sinopsis vacía, 0 slugs duplicados, 98 sinopsis exactas repetidas y 4 fichas por fusión aprobada; quedaron 8.644 libros. <!-- Última modificación: 2026-10-27 -->
## Operación y despliegue <!-- Última modificación: 2026-10-27 -->
- Dependencias: instalar las incluidas en `requirements.txt`, entre ellas `python-Levenshtein`, y abrir el notebook con Jupyter. <!-- Última modificación: 2026-10-27 -->
- Persistencia: el Paso 1 muestra los resultados dentro del notebook y no escribe cambios en el archivo de entrada. <!-- Última modificación: 2026-10-27 -->
- Seguridad e integraciones: no se envían datos a servicios externos ni se agregan credenciales. <!-- Última modificación: 2026-10-27 -->
- Despliegue: no aplica; el notebook se ejecuta localmente para la entrega académica. <!-- Última modificación: 2026-10-27 -->
